# 行业项目产品经理 Loop Skill

这是一个面向复杂行业、ToB产品、平台产品和解决方案项目的完整产品经理Skill。

它解决的不是“帮我写一份PRD”，而是：

> 面对一个陌生行业或项目，从行业研究、痛点发现和商业验证开始，持续推进到立项、需求、交付、上线和复盘，并自动检查材料是否完整、结论是否有证据、下一步应该做什么。

## 1. 能力范围

- 行业和价值链研究
- 项目机会与痛点分析
- BP、BRD、MRD和商业模式
- 客户研究、购买委员会、Persona、JTBD和用户旅程
- 具体产品级竞品分析
- Build / Buy / Integrate决策
- Project Brief、PID、RACI和Roadmap
- 需求池、优先级和版本规划
- 总体解决方案与产品架构
- PRD、规则、权限、数据字典和埋点
- SRS、SRD、SID和工程交付准备
- 测试、UAT、上线、回滚和培训
- 运营、价值验证和项目复盘
- 文档完整度自动审计
- 循环推进和停止条件判断

## 2. Skill结构

```text
industry-project-product-manager-loop/
├── SKILL.md                         # 核心执行说明
├── README.md                        # 使用说明
├── references/
│   ├── lifecycle-map.md             # 生命周期和文档地图
│   ├── loop-protocol.md             # 循环工程协议
│   ├── research-evidence-standard.md# 研究和证据标准
│   └── quality-gates.md             # 质量门与退出条件
├── templates/
│   ├── project-manifest.json        # 项目基本信息
│   ├── project-state.json           # Loop状态和记忆
│   ├── deliverable-index.md         # 交付物索引
│   └── gap-analysis.md              # 缺口分析模板
├── examples/
│   └── aidc-project-manifest.json   # AIDC示例
├── scripts/
│   └── audit_project_docs.py        # 文档完整度审计脚本
└── tests/
    └── scenarios.md                 # 行为测试场景
```

## 3. 推荐使用方式

### 新行业项目

示例指令：

```text
使用industry-project-product-manager-loop Skill。
行业：工业机器人。
项目：面向中型制造企业的机器人运维平台。
目标：形成大型ToB解决方案项目文档。
现有资料：docs/research目录。
先盘点资料，然后从缺口最大的阶段开始推进。
```

### 审计已有项目

```text
使用industry-project-product-manager-loop Skill，检查当前项目的痛点、商业、竞品、用户、PID、PRD、工程、测试、上线和复盘材料是否齐全。不要只根据文件名判断，要检查正文质量，并生成缺口矩阵和下一步优先级。
```

### 面试作品集

```text
将当前项目按Interview Portfolio完成档位整理。重点检查业务问题、用户证据、产品决策、PRD深度、交付过程、结果指标和复盘是否能形成完整故事。
```

## 4. Loop工作方式

Skill每一轮执行：

```text
观察现状
  → 识别缺口和冲突
  → 选择最高价值动作
  → 创建或更新材料
  → 执行质量检查
  → 更新项目状态
  → 继续、升级人工决策或停止
```

Loop不会因为“已经生成文件”就判定完成。只有内容通过质量门，且上下游可追溯，才会进入下一阶段。

## 5. 完成档位

- `lightweight_feature`：小型功能迭代
- `medium_product`：中型产品项目
- `large_tob_solution`：大型ToB解决方案
- `interview_portfolio`：产品经理面试作品集

档位决定哪些文档和质量门是必选项。

## 6. 自动审计

在项目目录执行：

```bash
python skills/industry-project-product-manager-loop/scripts/audit_project_docs.py \
  --project-root AIDC算力中心知识库 \
  --profile large_tob_solution
```

输出包括：

- 各阶段材料命中情况
- 必选项缺口
- 当前完成度
- 可能只有标题、内容不足的文件
- 下一步建议

脚本只能检查结构和基础内容信号，不能替代产品判断。最终仍需按照质量门检查证据、逻辑和可执行性。

## 7. 与普通提示词的区别

普通提示词通常只完成一次任务；这个Skill保存的是完整工作方法，包括：

- 固定生命周期
- 标准交付物
- 项目状态
- 证据规则
- 质量门
- 工具策略
- 风险升级机制
- 停止条件
- 自动审计
- 项目结束后的方法论回灌

因此它更接近一个可持续运行的产品经理工作系统，而不是一段长Prompt。

## 8. 平台兼容思路

该Skill采用`SKILL.md + references + templates + scripts + tests`的可移植目录结构。核心工作流不依赖特定模型；具体工具调用可根据ChatGPT、Codex、Claude或企业Agent平台的能力调整。