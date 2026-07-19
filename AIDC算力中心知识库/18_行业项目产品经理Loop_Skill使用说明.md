# 行业项目产品经理Loop Skill使用说明

## 1. Skill定位

仓库新增：

```text
skills/industry-project-product-manager-loop/
```

该Skill将产品经理面对一个陌生行业或复杂项目时需要完成的工作，封装为可重复执行的全生命周期工作流。

它不是单独生成某份PRD，而是持续推进：

```text
行业研究
→ 痛点与机会
→ 商业和市场
→ 客户与用户研究
→ 竞品与差异化
→ 立项与Roadmap
→ 总体方案与PRD
→ 工程、接口与交付
→ 测试、上线和回滚
→ 运营数据与复盘
```

## 2. 为什么需要Loop

普通产品工作经常出现：

- 已经写了PRD，但不知道为什么做；
- 竞品分析只有功能列表，不能指导取舍；
- 用户画像没有购买者和决策者；
- Roadmap只是功能排期；
- 上线后没有数据验证；
- 文档很多，但互相冲突；
- 缺什么材料需要依赖人工反复提醒。

Loop机制每一轮都会：

1. 检查现有材料；
2. 识别缺口、冲突和证据不足；
3. 选择最高价值的下一步；
4. 创建或更新材料；
5. 执行质量门；
6. 更新项目状态；
7. 判断继续、请求人工决策或停止。

## 3. AIDC项目使用方式

建议指令：

```text
使用industry-project-product-manager-loop Skill。
项目目录：AIDC算力中心知识库。
项目类型：大型ToB解决方案。
先审计当前行业、痛点、商业、竞品、用户、立项、PRD、工程、测试、上线和复盘材料。
不要只看文件名，要检查内容质量、证据和上下游一致性。
生成缺口矩阵，选择最高价值的下一步并更新项目状态。
```

## 4. 当前AIDC项目对应关系

| Skill阶段 | AIDC现有材料 |
|---|---|
| 行业与机会 | 01、02、11 |
| 商业与市场 | 12 |
| 用户研究 | 04、06、14 |
| 竞品分析 | 03、13 |
| 立项规划 | 10、15 |
| 总体方案 | 05、09 |
| PRD | 16 |
| 工程和交付模板 | 08、17 |
| 运维知识 | 07、09、16 |

当前知识库已经具备完整方法框架，但仍需真实项目证据补强：

- 客户访谈记录；
- 招标文件或采购需求；
- 真实集群和GPU利用率数据；
- 真实故障和工单记录；
- 项目预算和团队配置；
- 竞品POC和价格信息；
- UAT和上线结果；
- 实际收益和复盘数据。

## 5. 自动审计

```bash
python skills/industry-project-product-manager-loop/scripts/audit_project_docs.py \
  --project-root AIDC算力中心知识库 \
  --profile large_tob_solution \
  --output AIDC算力中心知识库/项目文档结构审计结果.md
```

支持档位：

- `lightweight_feature`
- `medium_product`
- `large_tob_solution`
- `interview_portfolio`

审计器主要检查文件、关键词、内容长度和基础结构。它不能判断客户证据是否真实，也不能替代产品、架构、安全和项目负责人的正式评审。

## 6. 核心文件

- `SKILL.md`：完整执行流程和停止条件；
- `references/lifecycle-map.md`：生命周期和文档关系；
- `references/loop-protocol.md`：Loop Engineering协议；
- `references/research-evidence-standard.md`：研究和证据规则；
- `references/quality-gates.md`：八道质量门；
- `templates/project-manifest.json`：项目基本信息；
- `templates/project-state.json`：持续记忆和状态；
- `scripts/audit_project_docs.py`：结构审计；
- `tests/scenarios.md`：行为测试。

## 7. 最终目标

Skill的目标不是生产最多的文档，而是建立一套完整的决策系统：

```text
证据
→ 痛点
→ 用户任务或业务需求
→ 产品能力
→ 功能和规则
→ 验收标准
→ 上线指标
→ 实际结果
→ 下一轮决策
```

产品经理可以将它用于新行业调研、ToB解决方案、平台产品立项、客户项目交付和面试作品集整理。