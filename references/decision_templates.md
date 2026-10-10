# Decision Gate Templates & Matrix Patterns

Use these patterns to ensure uniform, high-density decision gates that satisfy Phase 3 and Phase 4 constraints.

---

## Pattern 1: Architecture & System Design Template

```markdown
### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected

**Input Analysis**: The request involves building [System/Feature], which can be organized under divergent architectural paradigms.

---

#### [Option A]: [Monolithic / Embedded / In-Process Approach]
- **Philosophy**: Optimize for zero external dependencies, rapid startup, and local runtime simplicity.
- **Deliverable**: Self-contained module in [Language/Framework] with unit tests.
- **Trade-off**: **Pro**: Minimal setup and deployment complexity | **Con**: Single-node capacity and ephemeral state.

#### [Option B]: [Distributed / Microservice / Decoupled Approach]
- **Philosophy**: Optimize for independent horizontal scalability, persistence, and multi-tenant isolation.
- **Deliverable**: Modular service interface with client SDK and container configuration.
- **Trade-off**: **Pro**: Robust fault-isolation and elastic scale | **Con**: Increased operational and network overhead.

#### [Option C]: [Event-Driven / Asynchronous Queue Approach]
- **Philosophy**: Optimize for decoupled producer-consumer processing and burst handling.
- **Deliverable**: Worker consumer pipeline with queue broker integration.
- **Trade-off**: **Pro**: Resilient to traffic spikes | **Con**: Eventual consistency and tracing overhead.

---

### Decision Matrix

| Option | Paradigm | Deliverable Shape | Core Advantage |
| :--- | :--- | :--- | :--- |
| **[Option A]** | In-Process | Single module | Zero operational overhead |
| **[Option B]** | Distributed | Service + Client SDK | Independent horizontal scaling |
| **[Option C]** | Event-Driven | Worker pipeline | Decoupled asynchronous handling |

**Next Step**: Please select **[Option A]**, **[Option B]**, **[Option C]**, or request a hybrid combination.
```

---

## Pattern 2: Algorithm & Modeling Trade-Off Template

```markdown
### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected

**Input Analysis**: Implementing [Algorithm/Model] presents divergent optimization trade-offs between mathematical rigor, execution performance, and development speed.

---

#### [Option A]: Exact / Analytical Formulation
- **Philosophy**: Prioritize absolute theoretical accuracy and deterministic guarantees.
- **Deliverable**: Closed-form algorithm implementation with precision validation tests.
- **Trade-off**: **Pro**: Zero approximation error | **Con**: Computational complexity scales poorly ($O(N^2)$ or worse).

#### [Option B]: Approximate / Heuristic / Sampling
- **Philosophy**: Prioritize throughput and sub-linear scaling by trading negligible precision.
- **Deliverable**: Approximate nearest-neighbor / probabilistic estimation routine.
- **Trade-off**: **Pro**: Fast sub-millisecond execution on large inputs | **Con**: Stochastic bounds with bounded epsilon error.

---

### Decision Matrix

| Option | Method | Deliverable Shape | Trade-Off |
| :--- | :--- | :--- | :--- |
| **[Option A]** | Exact Analytical | High-precision solver | Exact accuracy; high compute cost |
| **[Option B]** | Heuristic Approximation | Fast probabilistic routine | Sub-linear speed; bounded approx error |

**Next Step**: Which computational regime fits your use case? Reply with **[Option A]** or **[Option B]**.
```

---

## Pattern 3: Code Refactoring / Implementation Depth Template

```markdown
### ⚠️ Request Disambiguation Gate: Aleatoric Uncertainty Detected

**Input Analysis**: Refactoring [Target Component] can range from targeted cosmetic patching to foundational architectural restructuring.

---

#### [Option A]: Surgical Fix (Minimal Blast Radius)
- **Philosophy**: Address the immediate pain point with zero API breakage and minimal code churn.
- **Deliverable**: Targeted patch across 1–2 files preserving existing public interfaces.
- **Trade-off**: **Pro**: Safest path with lowest regression risk | **Con**: Leaves underlying structural tech debt intact.

#### [Option B]: Architectural Overhaul (Clean Room Redesign)
- **Philosophy**: Eliminate structural tech debt by re-architecting the component around modern design patterns.
- **Deliverable**: Refactored core module with modernized type definitions and deprecation shims.
- **Trade-off**: **Pro**: Extensible, future-proof design | **Con**: Higher review burden and migration overhead.

---

### Decision Matrix

| Option | Scope | Deliverable Shape | Risk vs Benefit |
| :--- | :--- | :--- | :--- |
| **[Option A]** | Surgical Patch | In-place bugfix (<30 LOC) | Minimal risk; preserves technical debt |
| **[Option B]** | Structural Overhaul | Clean component rewrite | Long-term maintainability; higher churn |

**Next Step**: Do you prefer the surgical fix (**[Option A]**) or the structural rewrite (**[Option B]**)?
```
