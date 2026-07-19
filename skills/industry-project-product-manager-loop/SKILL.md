---
name: industry-project-product-manager-loop
description: Use when a product manager needs to research an unfamiliar industry, define a project opportunity, build a complete ToB or platform product document system, audit missing materials, and iteratively drive the project from opportunity analysis through PRD, delivery, launch, and post-launch review. Suitable for industry solutions, enterprise software, infrastructure platforms, AI platforms, cloud products, and complex project-based product work.
---

# Industry Project Product Manager Loop

## Purpose

Turn an unfamiliar industry or project idea into a complete, evidence-backed, executable product project.

This skill does not merely generate a PRD. It drives the full chain:

```text
Industry understanding
  → opportunity and pain points
  → business and market validation
  → customer and user research
  → competitive strategy
  → project initiation and scope
  → product architecture and PRD
  → engineering and delivery documents
  → launch and operations
  → data review and next iteration
```

The skill operates as a loop. It repeatedly audits evidence, deliverables, scope, risks, and quality gates until the project meets its termination criteria or requires a human decision.

## When to use

Use this skill when the user asks to:

- understand a new industry from a product manager perspective;
- prepare a complete project-level product plan;
- build a product manager document system rather than a single PRD;
- audit whether project materials are complete;
- generate BP, BRD, MRD, PID, PRD, SRS, SID, roadmap, UAT, launch, or review documents;
- transform research notes into a structured ToB solution;
- create an interview portfolio for a complete product project;
- build an industry solution playbook or reusable product methodology;
- continue improving a project until all required deliverables pass quality checks.

Do not use this skill for a tiny copy change, isolated UI adjustment, or a simple feature request that does not require project-level discovery and planning.

## Operating principles

1. Start from the business problem, not from a feature list.
2. Separate facts, customer evidence, assumptions, hypotheses, targets, and product commitments.
3. Distinguish buyer, decision-maker, user, administrator, influencer, and beneficiary.
4. Treat project documents as one traceable system rather than independent files.
5. Every feature must trace back to a pain point, user job, business objective, or compliance obligation.
6. Every claimed value must have a measurement method.
7. Mark missing evidence explicitly; never fabricate customer interviews, market sizes, prices, or product results.
8. Define in-scope and out-of-scope early.
9. Prefer build, buy, or integrate decisions over blindly rebuilding all capabilities.
10. Stop high-risk automation when human approval is required.

## Required inputs

Collect as many of the following as available. Do not block the workflow when some are missing; record them as assumptions or evidence gaps.

- industry or domain;
- project or product name;
- project type: internal platform, commercial SaaS, private deployment, solution project, marketplace, consumer product, infrastructure product, or other;
- organization and strategic context;
- target customers and users;
- current systems and processes;
- known pain points;
- desired business outcomes;
- constraints: budget, timeline, team, compliance, deployment, region, technology;
- available source materials, links, files, repositories, meeting notes, tickets, or data;
- expected output depth;
- target audience: executive, product, engineering, sales, customer, investor, or interview panel.

## Project state

Maintain a project state file using `templates/project-state.json`.

At minimum track:

- project identity and scope;
- current phase;
- completed deliverables;
- evidence inventory;
- assumptions and unresolved questions;
- risks and dependencies;
- quality-gate results;
- next recommended actions;
- human decisions required;
- stop condition status.

Update the state after every major phase.

## Core loop

Run the following loop until a stop condition is met.

### 1. Observe

Inspect all available materials and determine:

- what is already known;
- what is missing;
- what has changed;
- which claims are unsupported;
- which documents already exist;
- whether documents conflict with one another;
- whether the current project stage is correctly identified.

### 2. Plan

Choose the smallest set of actions that materially advances the project.

Prioritize:

1. missing decisions that block downstream work;
2. missing evidence behind high-impact assumptions;
3. incomplete mandatory deliverables;
4. inconsistencies between strategy, requirements, and delivery;
5. quality-gate failures;
6. lower-priority enrichment.

### 3. Act

Create, update, or reorganize the necessary deliverables using the lifecycle defined below.

Reuse existing materials. Do not duplicate content across documents unless the new document serves a different audience or decision.

### 4. Verify

Check:

- evidence quality;
- internal consistency;
- traceability;
- scope control;
- technical plausibility;
- commercial plausibility;
- measurable acceptance criteria;
- delivery readiness;
- launch and rollback readiness.

Use `references/quality-gates.md` and, when files are available, run `scripts/audit_project_docs.py`.

### 5. Update memory

Update project state, decision log, evidence gaps, risks, and next actions.

### 6. Continue, escalate, or stop

- Continue when an important deliverable or gate remains incomplete and can be advanced with available evidence.
- Escalate when a decision requires the user, customer, legal, security, finance, architecture, or executive owner.
- Stop when the selected completion profile passes all mandatory gates, or when no further grounded progress is possible without missing external evidence.

## Lifecycle phases

Read `references/lifecycle-map.md` for the complete document map.

### Phase 0: Intake and project classification

Determine:

- the industry and value chain;
- the project type;
- target customer and deployment pattern;
- project maturity;
- expected document profile;
- whether this is a product, solution, implementation, research, or portfolio exercise.

Outputs:

- project brief;
- initial scope;
- stakeholder map;
- evidence inventory;
- project-state file;
- document completion profile.

### Phase 1: Industry and opportunity research

Analyze:

- industry structure and value chain;
- market drivers and constraints;
- policies and standards when relevant;
- customer operating model;
- existing alternatives;
- why the problem matters now;
- problem severity and affected roles.

Outputs:

- industry research report;
- opportunity analysis;
- pain-point map;
- assumptions and research backlog.

### Phase 2: Business and market validation

Build only the documents appropriate to the project:

- BP for business viability and company-building logic;
- BRD for internal investment and business requirements;
- MRD for market segments, demand, positioning, and go-to-market;
- business model and pricing hypothesis;
- ROI and value-measurement model.

Do not present unverified estimates as facts.

### Phase 3: Customer and user research

Distinguish:

- account or customer segment;
- purchasing committee;
- operational users;
- administrators;
- affected business teams.

Outputs:

- research plan and interview guide;
- evidence-backed findings;
- Persona;
- JTBD;
- user journeys;
- service blueprint when cross-organization delivery is involved;
- prioritized needs.

### Phase 4: Competitive and alternative analysis

Analyze direct competitors, adjacent products, internal alternatives, manual processes, open-source components, and system integrators.

Outputs:

- competitor selection logic;
- product-level capability matrix;
- positioning map;
- strengths and weaknesses;
- commercial and delivery comparison;
- build, buy, partner, integrate, or avoid decision;
- differentiated product strategy.

Competitor analysis must end with product decisions, not a feature inventory.

### Phase 5: Product strategy and project initiation

Outputs:

- product vision and positioning;
- Project Brief;
- PID or project charter;
- goals and measurable success metrics;
- in-scope and out-of-scope;
- stakeholder and RACI matrix;
- roadmap;
- milestone plan;
- requirement pool and prioritization;
- risk and dependency register.

### Phase 6: Solution and product definition

Outputs as required:

- overall solution document;
- product capability map;
- information architecture;
- business process and exception flows;
- page inventory;
- PRD;
- business rules;
- permission matrix;
- data dictionary;
- analytics and event tracking plan;
- non-functional requirements;
- acceptance criteria.

For infrastructure or platform products, explicitly address:

- system boundaries;
- integration strategy;
- observability;
- security and audit;
- multi-tenancy;
- availability and disaster recovery;
- capacity and performance;
- upgrade, compatibility, and rollback;
- operational ownership.

### Phase 7: Engineering and integration readiness

Work with technical roles to prepare or audit:

- SRS or SRD;
- HLD and LLD expectations;
- SID or interface specification;
- deployment architecture;
- environment and configuration plan;
- data migration plan;
- security design;
- implementation plan;
- test strategy;
- engineering dependency list.

Do not invent detailed technical implementation when architecture evidence is absent. Clearly label product requirements versus technical design decisions.

### Phase 8: Delivery, test, and launch

Outputs:

- version scope;
- test cases and test matrix;
- UAT plan;
- launch checklist;
- rollout or gray-release plan;
- migration plan;
- monitoring plan;
- rollback conditions and steps;
- release notes;
- training and user documentation;
- support and incident process.

### Phase 9: Operations and review

Outputs:

- adoption and customer-success plan;
- product metric dashboard definition;
- business value report;
- issue and feedback loop;
- incident and defect trends;
- project review;
- next-version roadmap;
- lessons added back into the skill or industry knowledge base.

## Completion profiles

Choose one profile at project start.

### Lightweight feature

Mandatory:

- background and goal;
- affected users;
- scope;
- simplified PRD;
- prototype or interaction notes;
- rules and exceptions;
- analytics;
- acceptance criteria;
- launch and rollback notes.

### Medium product project

Mandatory:

- opportunity or BRD;
- user research;
- competitor analysis;
- Persona and journey;
- product strategy;
- roadmap;
- PRD;
- information architecture;
- permissions and data requirements;
- UAT;
- launch plan;
- post-launch review plan.

### Large ToB solution

Mandatory:

- industry and opportunity research;
- BP, BRD, or equivalent commercial proposal;
- MRD;
- customer research;
- purchasing committee and Persona;
- competitive strategy;
- PID;
- overall solution;
- product architecture;
- PRD;
- SRS or SRD expectations;
- SID and integration plan;
- security and deployment plan;
- implementation plan;
- test and UAT;
- training and operations plan;
- acceptance and review.

### Interview portfolio

Mandatory:

- project context and problem;
- user and customer insight;
- evidence and prioritization;
- business value;
- solution architecture;
- one or two deep PRD examples;
- trade-offs and scope decisions;
- delivery process;
- results or clearly labeled target metrics;
- reflection and next steps.

## Evidence rules

Read `references/research-evidence-standard.md` before making external claims.

For every important claim, label it as one of:

- verified fact;
- customer evidence;
- internal data;
- industry reference;
- inference;
- hypothesis;
- product target;
- unresolved question.

Never convert a hypothesis or target into a historical result.

## Traceability rules

Maintain the following trace chain:

```text
Evidence
  → pain point
  → affected role and scenario
  → JTBD or business requirement
  → product capability
  → feature requirement
  → acceptance criterion
  → launch metric
  → observed result
```

Any P0 feature without a traceable upstream need must be challenged.

Any strategic objective without downstream metrics must be challenged.

## Quality gates

The project cannot move forward merely because a document exists.

At each gate verify content quality.

- Gate A: opportunity is real and important;
- Gate B: customer, buyer, and user are understood;
- Gate C: strategy and differentiation are coherent;
- Gate D: project scope and success metrics are approved;
- Gate E: requirements are testable and traceable;
- Gate F: engineering, security, integration, and operations are feasible;
- Gate G: launch, monitoring, rollback, and support are ready;
- Gate H: results are measured and lessons captured.

See `references/quality-gates.md` for detailed checks.

## Tool use

Use tools deliberately.

- Web research: current market, competitor, policy, standard, and product facts.
- File and repository search: inspect existing project documents before creating new ones.
- Spreadsheets: requirement pools, competitor matrices, budgets, ROI, timelines, and metrics.
- Documents: formal BRD, PRD, solution, and research reports.
- Slides: executive, sales, kickoff, review, and interview presentations.
- Diagram tools: architecture, process, journey, topology, and data flow.
- GitHub or document repositories: version all reusable artifacts and maintain change history.

When tools are unavailable, produce a grounded plan and clearly identify what cannot be verified.

## Output structure

For a new project, create a project folder similar to:

```text
project-name/
├── 00_project-state.json
├── 01_project-brief.md
├── 02_industry-opportunity.md
├── 03_business-market.md
├── 04_user-research.md
├── 05_competitor-analysis.md
├── 06_pid-roadmap.md
├── 07_solution-architecture.md
├── 08_prd/
├── 09_data-permission-rules/
├── 10_engineering-integration/
├── 11_test-uat-launch/
├── 12_operations-review/
└── evidence/
```

Adapt the folder to project scale. Do not create empty documents solely to satisfy the structure.

## Final response requirements

When finishing a run, report:

1. what was inspected;
2. what was created or updated;
3. current lifecycle phase;
4. completion score by phase;
5. important evidence gaps;
6. unresolved human decisions;
7. next highest-value action;
8. whether the loop should continue or stop.

## Stop conditions

Stop when one of the following is true:

### Successful completion

- the chosen completion profile passes every mandatory quality gate;
- all P0 requirements are traceable and testable;
- project scope, ownership, risks, launch plan, and measurement plan are explicit;
- unsupported claims are clearly labeled;
- no critical document conflict remains.

### Human decision required

Stop and escalate when progress depends on:

- budget approval;
- legal or compliance interpretation;
- architecture ownership;
- security exception;
- commercial pricing decision;
- customer confirmation;
- irreversible production action;
- prioritization conflict with no defined owner.

### Evidence exhausted

Stop when additional work would only repeat assumptions or fabricate missing facts. Provide a research or interview plan instead.

## Continuous improvement

After each completed project:

- identify recurring missing inputs;
- record useful research queries;
- add validated industry patterns to references;
- update templates based on delivery lessons;
- add new test scenarios;
- remove duplicated or low-value steps;
- version the skill and document the change.

The goal is not to produce the maximum number of documents. The goal is to produce the minimum complete evidence and decision system required to make, build, launch, and improve the right product.