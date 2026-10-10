---
name: aleatoric-uncertainty-resolver
description: Disambiguate inherently uncertain, under-specified, or high-entropy user requests by decomposing divergent interpretations, simulating expected outcomes for each path, and providing a structured decision gate before execution.
---

# Aleatoric Uncertainty Resolver

A decision-gating skill designed to resolve aleatoric uncertainty (intrinsic divergence/entropy in goals, specifications, or problem formulations) before costly generation or execution occurs.

## Overview & Core Philosophy

In machine learning and decision theory, **aleatoric uncertainty** represents irreducible randomness or inherent divergence—where multiple valid, mutually exclusive states or outcomes exist given the same initial observation. When applied to user prompts, aleatoric uncertainty arises when a request is high-entropy: several distinct, architecturally incompatible target regimes are equally plausible.

Defaulting to a single arbitrary guess often leads to massive downstream rework, wasted tokens, and cognitive fatigue. The **Aleatoric Uncertainty Resolver** enforces a structured circuit breaker: it halts downstream execution, atomizes the divergent paths, simulates expected deliverables under strict brevity constraints, and presents a deterministic decision gate to the user.

---

## Core Invariants

1. **Downstream Execution Hold**: If semantic entropy is high (≥ 2 distinct target regimes), halt all heavy generation, full-file scaffolding, and implementation immediately until the gate is resolved.
2. **Strict Brevity Guardrail**: Simulated branches must not exceed 2 to 3 sentences. No walls of text. Total gate output should be scannable in under 30 seconds.
3. **Deterministic Keys**: Always assign predictable, clean identifiers (`[Option A]`, `[Option B]`, `[Option C]`, `[Option D]`).
4. **Symmetric Fairness**: Present alternative interpretations neutrally without preemptive bias unless the user explicitly signaled a constraint.
5. **Actionable Closure**: Always end with a clean, single-line prompt enabling the user to choose directly, hybridize, or add constraints.

---

## When to Use

- **High Semantic Entropy**: The user prompt allows multiple plausible, mutually incompatible interpretations (e.g., "Build an indexing system" -> InMemory trie vs. vector DB vs. distributed inverted index).
- **Ambiguous Objective Functions**: Architectural, modeling, or system engineering tasks where the core trade-off (e.g., latency vs. accuracy, simplicity vs. extensibility) is unstated.
- **Under-Specified Output Shape**: Unclear deliverable modality (e.g., formal mathematical formulation vs. minimal working prototype vs. production enterprise service).
- **High Blast Radius**: Requests where guessing wrong causes substantial token waste, deep refactoring, or flawed foundations.

### When NOT to Use
- **Low Entropy / Single-Peaked Intent**: Clear, specific, unambiguous instructions (e.g., "Add a unit test for function `calc_mean` in `stats.py`").
- **Pure Epistemic Deficits**: The user asks for a factual answer or documentation that can be resolved via search/reading rather than a divergence in goals.

---

## Operational Workflow

```
       [User Raw Input]
              │
              ▼
  ┌────────────────────────┐
  │ Phase 1: Entropy Check │
  └───────────┬────────────┘
              │
      Entropy ≥ 2 regimes?
     ┌────────┴────────┐
     │ No              │ Yes
     ▼                 ▼
[Execute Task]  ┌─────────────────────────────────┐
                │ Phase 2: Divergent Path Enumerate│ (2-4 paths)
                └────────────────┬────────────────┘
                                 │
                                 ▼
                ┌─────────────────────────────────┐
                │ Phase 3: Generative Simulation  │ (≤3 sentences each)
                └────────────────┬────────────────┘
                                 │
                                 ▼
                ┌─────────────────────────────────┐
                │ Phase 4: Decision Gate Matrix   │ ([Option A], [Option B]...)
                └─────────────────────────────────┘
```

---

### Phase 1: Request Definition & Entropy Check

1. **Formalize Raw Input**:
   - Extract core technical verbs, constraints, entities, and unstated assumptions.
2. **Evaluate Aleatoric Uncertainty**:
   - Identify active divergence dimensions:
     - **Paradigm / Level of Abstraction**: High-level conceptual architecture vs. low-level bare-metal code.
     - **Modality**: Theoretical proof / mathematical framework vs. runnable implementation vs. benchmark harness.
     - **Engineering Trade-offs**: Speed / low latency vs. accuracy / memory footprint vs. rapid developer velocity.
     - **Ecosystem / Stack**: Lightweight zero-dependency script vs. heavy framework integration.
3. **Entropy Gating**:
   - **Low Entropy (Single-peaked)**: Proceed directly with task execution.
   - **High Entropy (Multi-peaked, ≥ 2 regimes)**: Activate Phases 2–4 immediately. Halt generation.

---

### Phase 2: Divergent Path Enumeration

Identify 2 to 4 principal interpretation candidates that span the possibility space. For each path, establish:
- **Path Label & Philosophy**: A concise label and the underlying design thesis or objective function driving this interpretation.
- **Implicit Assumptions**: What this branch assumes regarding scope, runtime constraints, target audience, and dependencies.

---

### Phase 3: Generative Outcome Simulation (Strictly Brief)

To prevent cognitive overload and token waste, apply strict constraints:
- **Length Constraint**: Strictly 2 to 3 sentences per branch. No lengthy prose.
- **Simulated Deliverable Shape**: Exactly one line declaring deliverable format and methodology (e.g., `"Deliverable: Standalone Python 3.11 script using numpy and pytest"`).
- **Primary Trade-off**: 1 bullet point highlighting the core pro/con.
- **Illustrative Micro-Snippet**: Optional, strictly capped at 1 to 3 lines (e.g., function signature or configuration stub).

---

### Phase 4: Structured Selection Gate

Synthesize the paths into a clean, high-density decision matrix:

1. **Deterministic Identifiers**: Tag each path clearly as `[Option A]`, `[Option B]`, `[Option C]`.
2. **Summary Matrix**: A unified Markdown table or structured bullet list displaying:
   - Option identifier & title
   - Target goal / philosophy
   - Deliverable shape
   - Core trade-off
3. **Closing Prompt**: End with a single, clear interactive question:
   > *"Which option aligns with your objective? (Reply with `Option A`, `Option B`, hybridize, or specify custom constraints)."*

---

## Reference Output Format

When high entropy is triggered, structure the response using this template:

```markdown
### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected

**Input Analysis**: [1 sentence summarizing the core request and the identified ambiguity]

---

#### [Option A]: [Descriptive Title]
- **Philosophy**: [1 sentence on thesis / objective function]
- **Deliverable**: [1 line declaring format and scope]
- **Trade-off**: **Pro**: [benefit] | **Con**: [limitation]
```python
# (Optional micro-snippet, ≤ 3 lines)
```

#### [Option B]: [Descriptive Title]
- **Philosophy**: [1 sentence on thesis / objective function]
- **Deliverable**: [1 line declaring format and scope]
- **Trade-off**: **Pro**: [benefit] | **Con**: [limitation]
```python
# (Optional micro-snippet, ≤ 3 lines)
```

---

### Decision Matrix

| Option | Approach | Deliverable Shape | Primary Advantage |
| :--- | :--- | :--- | :--- |
| **[Option A]** | [Name] | [Format] | [Key pro] |
| **[Option B]** | [Name] | [Format] | [Key pro] |

**Next Step**: Please select **[Option A]**, **[Option B]**, suggest a hybrid, or provide specific constraints to begin execution.
```

---

## Detailed Example Walkthrough

### Example Request: "Help me implement semantic caching for my LLM pipeline"

#### Agent Gating Response:

```markdown
### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected

**Input Analysis**: "Semantic caching for LLM pipeline" has multiple incompatible architectural implementations depending on latency budgets, infrastructure footprint, and embedding accuracy requirements.

---

#### [Option A]: Embedded In-Memory Vector Cache (Zero-Dependency)
- **Philosophy**: Minimize operational overhead and latency with an in-process embedding buffer and cosine thresholding.
- **Deliverable**: Single self-contained Python module using `numpy` + local embedding model.
- **Trade-off**: **Pro**: Ultra-low latency, zero external servers | **Con**: Process-bound memory limit, no cross-worker cache sharing.
```python
class InMemorySemanticCache:
    def get(self, query_emb: np.ndarray, threshold: float = 0.92) -> Optional[str]: ...
```

#### [Option B]: Distributed Vector DB Tier (Redis / Qdrant)
- **Philosophy**: Production-scale distributed caching shared across multiple stateless LLM worker pods.
- **Deliverable**: Production client wrapper with Redis VSS or Qdrant integration, TTL support, and connection pooling.
- **Trade-off**: **Pro**: Scalable, persistent, distributed | **Con**: Requires external vector database infrastructure.
```python
class DistributedSemanticCache:
    def __init__(self, redis_client: redis.Redis, index_name: str = "llm_cache"): ...
```

#### [Option C]: Hybrid Exact-Match + Approximate Cluster Hierarchy
- **Philosophy**: Tiered caching optimizing for cost: exact MD5 string match first, hierarchical cluster lookup second.
- **Deliverable**: Two-tier caching pipeline with metric logging and cache-invalidation policies.
- **Trade-off**: **Pro**: Maximum hit rate at minimal embedding compute | **Con**: Higher implementation complexity.

---

### Decision Matrix

| Option | Architecture | Deliverable Shape | Key Trade-off |
| :--- | :--- | :--- | :--- |
| **[Option A]** | In-Memory (Numpy) | Python module (`numpy`) | Zero external infrastructure; ephemeral |
| **[Option B]** | Distributed (Redis/Qdrant) | Client class + Docker Compose | Production multi-worker; requires infra |
| **[Option C]** | Two-Tier (MD5 + Vector) | Layered cache orchestrator | Maximizes hit rate; higher complexity |

**Next Step**: Which option matches your architecture? Reply with **[Option A]**, **[Option B]**, **[Option C]**, or state your specific constraints.
```

---

## Integration with Agent Tools & Slash Commands

- **Slash Commands**:
  - `/plan`: Recommend `/plan` when the chosen path involves multi-step architecture or complex migration.
  - `/grill-me`: Recommend `/grill-me` if the user wants an interactive question-and-answer session to flesh out all system boundaries.
- **Interactive UI Tools**:
  - When running in an environment with the `ask_question` tool, you can present the decision gate directly as an interactive UI modal with deterministic radio options (`[Option A]`, `[Option B]`, `[Option C]`).

## Reference Documents & Tools
- For theoretical taxonomy on semantic entropy and uncertainty modeling: see [references/entropy_taxonomy.md](references/entropy_taxonomy.md).
- For pre-built decision gate templates across problem archetypes: see [references/decision_templates.md](references/decision_templates.md).
- For terminal and script-based gate validation: run [scripts/gate_formatter.py](scripts/gate_formatter.py).
