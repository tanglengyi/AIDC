#!/usr/bin/env python3
"""Audit product-project document completeness.

The script checks file names and readable text content for lifecycle deliverables.
It is intentionally dependency-free and only performs structural checks.
Use the quality-gate checklist for semantic review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TEXT_EXTENSIONS = {".md", ".txt", ".rst", ".json", ".yaml", ".yml", ".csv"}
KNOWN_EXTENSIONS = TEXT_EXTENSIONS | {
    ".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"
}


@dataclass(frozen=True)
class DeliverableRule:
    key: str
    label: str
    phase: str
    patterns: tuple[str, ...]
    content_signals: tuple[str, ...] = ()
    minimum_chars: int = 300


RULES: tuple[DeliverableRule, ...] = (
    DeliverableRule(
        "project_brief",
        "Project Brief / 项目简报",
        "phase_0_intake",
        ("project.?brief", "项目简报", "项目概述", "项目简介"),
        ("项目目标", "目标用户", "范围"),
    ),
    DeliverableRule(
        "industry_opportunity",
        "行业与机会分析",
        "phase_1_industry_opportunity",
        ("行业", "市场判断", "机会分析", "痛点", "problem", "opportunity"),
        ("行业背景", "痛点", "机会"),
    ),
    DeliverableRule(
        "business_market",
        "BP / BRD / MRD / 商业市场方案",
        "phase_2_business_market",
        (r"\bbp\b", r"\bbrd\b", r"\bmrd\b", "商业计划", "商业需求", "市场需求", "商业模式"),
        ("商业模式", "目标客户", "业务价值"),
    ),
    DeliverableRule(
        "user_research",
        "用户研究 / Persona / JTBD / 用户旅程",
        "phase_3_user_research",
        ("persona", "jtbd", "用户研究", "用户画像", "用户旅程", "客户访谈"),
        ("用户", "场景", "痛点"),
    ),
    DeliverableRule(
        "competitor_analysis",
        "竞品深度分析",
        "phase_4_competitive_strategy",
        ("竞品", "竞争分析", "benchmark", "competitive"),
        ("竞品", "差异化", "定位"),
    ),
    DeliverableRule(
        "pid_roadmap",
        "PID / Roadmap / 立项规划",
        "phase_5_initiation_planning",
        (r"\bpid\b", "roadmap", "路线图", "立项", "项目章程", "项目规划", "需求池"),
        ("项目目标", "范围", "里程碑"),
    ),
    DeliverableRule(
        "solution",
        "总体解决方案 / 产品架构",
        "phase_6_solution_prd",
        ("总体解决方案", "解决方案", "产品架构", "能力地图", "总体架构"),
        ("总体架构", "核心模块", "部署"),
    ),
    DeliverableRule(
        "prd",
        "PRD / 产品需求文档",
        "phase_6_solution_prd",
        (r"\bprd\b", "产品需求", "需求文档"),
        ("用户角色", "功能需求", "验收标准"),
        minimum_chars=600,
    ),
    DeliverableRule(
        "data_permission_rules",
        "权限 / 数据 / 规则 / 埋点",
        "phase_6_solution_prd",
        ("权限矩阵", "数据字典", "业务规则", "埋点", "指标文档"),
        ("权限", "字段", "规则"),
    ),
    DeliverableRule(
        "engineering_integration",
        "SRS / SRD / SID / 工程集成",
        "phase_7_engineering_integration",
        (r"\bsrs\b", r"\bsrd\b", r"\bsid\b", "系统需求", "接口文档", "接口设计", "集成方案", "部署方案"),
        ("接口", "部署", "安全"),
    ),
    DeliverableRule(
        "test_launch",
        "测试 / UAT / 上线 / 回滚",
        "phase_8_test_launch",
        ("测试", r"\buat\b", "上线方案", "发布方案", "回滚", "release"),
        ("验收", "上线", "回滚"),
    ),
    DeliverableRule(
        "operations_review",
        "运营 / 数据分析 / 复盘",
        "phase_9_operations_review",
        ("运营方案", "数据分析", "复盘", "postmortem", "review", "效果评估"),
        ("实际结果", "问题", "下一步"),
    ),
)

PROFILES: dict[str, tuple[str, ...]] = {
    "lightweight_feature": (
        "project_brief", "user_research", "prd", "data_permission_rules", "test_launch"
    ),
    "medium_product": (
        "project_brief", "industry_opportunity", "user_research", "competitor_analysis",
        "pid_roadmap", "solution", "prd", "data_permission_rules", "test_launch",
        "operations_review"
    ),
    "large_tob_solution": tuple(rule.key for rule in RULES),
    "interview_portfolio": (
        "project_brief", "industry_opportunity", "business_market", "user_research",
        "competitor_analysis", "pid_roadmap", "solution", "prd", "test_launch",
        "operations_review"
    ),
}


@dataclass
class Match:
    path: str
    filename_match: bool
    content_match: bool
    characters: int
    signals_found: list[str]
    quality_hint: str


@dataclass
class AuditItem:
    key: str
    label: str
    phase: str
    mandatory: bool
    status: str
    matches: list[Match]


def iter_files(root: Path) -> Iterable[Path]:
    ignored = {".git", "node_modules", ".venv", "venv", "__pycache__"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored for part in path.parts):
            continue
        if path.suffix.lower() in KNOWN_EXTENSIONS:
            yield path


def read_text(path: Path) -> str:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def normalize(value: str) -> str:
    return value.lower().replace("_", " ").replace("-", " ")


def find_matches(root: Path, rule: DeliverableRule) -> list[Match]:
    matches: list[Match] = []
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in rule.patterns]

    for path in iter_files(root):
        relative = str(path.relative_to(root))
        filename_value = normalize(relative)
        text = read_text(path)
        searchable = normalize(text[:200_000])

        filename_match = any(pattern.search(filename_value) for pattern in compiled)
        content_match = bool(text) and any(pattern.search(searchable) for pattern in compiled)
        if not (filename_match or content_match):
            continue

        signals_found = [
            signal for signal in rule.content_signals if signal.lower() in searchable
        ]

        if not text:
            quality_hint = "filename_only"
        elif len(text.strip()) < rule.minimum_chars:
            quality_hint = "thin_content"
        elif rule.content_signals and len(signals_found) < max(1, len(rule.content_signals) // 2):
            quality_hint = "needs_semantic_review"
        else:
            quality_hint = "structurally_substantial"

        matches.append(
            Match(
                path=relative,
                filename_match=filename_match,
                content_match=content_match,
                characters=len(text.strip()),
                signals_found=signals_found,
                quality_hint=quality_hint,
            )
        )

    return sorted(
        matches,
        key=lambda item: (
            item.quality_hint != "structurally_substantial",
            -item.characters,
            item.path,
        ),
    )


def status_for(matches: list[Match]) -> str:
    if not matches:
        return "missing"
    if any(match.quality_hint == "structurally_substantial" for match in matches):
        return "present_review_required"
    if any(match.quality_hint in {"thin_content", "needs_semantic_review"} for match in matches):
        return "partial"
    return "filename_only"


def audit(root: Path, profile: str) -> dict:
    mandatory_keys = set(PROFILES[profile])
    items: list[AuditItem] = []
    for rule in RULES:
        matches = find_matches(root, rule)
        items.append(
            AuditItem(
                key=rule.key,
                label=rule.label,
                phase=rule.phase,
                mandatory=rule.key in mandatory_keys,
                status=status_for(matches),
                matches=matches[:10],
            )
        )

    mandatory_items = [item for item in items if item.mandatory]
    present_count = sum(item.status == "present_review_required" for item in mandatory_items)
    partial_count = sum(item.status in {"partial", "filename_only"} for item in mandatory_items)
    missing_count = sum(item.status == "missing" for item in mandatory_items)
    completion_score = round(
        (present_count + partial_count * 0.5) / max(1, len(mandatory_items)) * 100,
        1,
    )

    next_actions = []
    for item in mandatory_items:
        if item.status == "missing":
            next_actions.append(f"Create or locate: {item.label}")
        elif item.status != "present_review_required":
            next_actions.append(f"Deepen and review: {item.label}")
    if not next_actions:
        next_actions.append("Run semantic quality gates and traceability review.")

    return {
        "project_root": str(root),
        "profile": profile,
        "structural_completion_score": completion_score,
        "summary": {
            "mandatory": len(mandatory_items),
            "present_review_required": present_count,
            "partial_or_filename_only": partial_count,
            "missing": missing_count,
        },
        "items": [
            {
                **{key: value for key, value in asdict(item).items() if key != "matches"},
                "matches": [asdict(match) for match in item.matches],
            }
            for item in items
        ],
        "next_actions": next_actions[:8],
        "warning": (
            "This is a structural audit. A present file does not mean the quality gate passes. "
            "Review evidence, consistency, traceability, feasibility, and acceptance criteria manually."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Product Project Document Audit",
        "",
        f"- Project root: `{report['project_root']}`",
        f"- Profile: `{report['profile']}`",
        f"- Structural completion score: **{report['structural_completion_score']}%**",
        "",
        "## Summary",
        "",
        "| Mandatory | Present | Partial | Missing |",
        "|---:|---:|---:|---:|",
        (
            f"| {report['summary']['mandatory']} | "
            f"{report['summary']['present_review_required']} | "
            f"{report['summary']['partial_or_filename_only']} | "
            f"{report['summary']['missing']} |"
        ),
        "",
        "## Deliverables",
        "",
        "| Phase | Deliverable | Mandatory | Status | Best match |",
        "|---|---|---:|---|---|",
    ]

    for item in report["items"]:
        best_match = item["matches"][0]["path"] if item["matches"] else ""
        lines.append(
            f"| {item['phase']} | {item['label']} | "
            f"{'Yes' if item['mandatory'] else 'No'} | {item['status']} | {best_match} |"
        )

    lines.extend(["", "## Next actions", ""])
    lines.extend(
        f"{index}. {action}" for index, action in enumerate(report["next_actions"], 1)
    )
    lines.extend(["", f"> {report['warning']}", ""])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit lifecycle document completeness for a product project."
    )
    parser.add_argument(
        "--project-root",
        required=True,
        type=Path,
        help="Project directory to scan.",
    )
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES),
        default="large_tob_solution",
        help="Completion profile.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output file. Prints to stdout when omitted.",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help="Exit with status 2 when structural score is below this percentage.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.project_root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: project root is not a directory: {root}", file=sys.stderr)
        return 1

    report = audit(root, args.profile)
    output = (
        json.dumps(report, ensure_ascii=False, indent=2)
        if args.format == "json"
        else render_markdown(report)
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)

    if args.fail_under is not None and report["structural_completion_score"] < args.fail_under:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
