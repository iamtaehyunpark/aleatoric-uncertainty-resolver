# Entropy & Uncertainty Taxonomy in Agent Interactions

## 1. Epistemic vs. Aleatoric Uncertainty

In artificial intelligence and statistical learning:

| Dimension | Epistemic Uncertainty | Aleatoric Uncertainty |
| :--- | :--- | :--- |
| **Origin** | Lack of knowledge, data, or facts | Intrinsic divergence, multi-modal probability density, underspecification |
| **Reducibility** | Reducible by gathering more data, reading files, searching documentation | Irreducible without an external decision or user preference injected |
| **Agent Action** | Call search/read tools, inspect code, lookup APIs | **Halt downstream execution; activate decision gate** |
| **Failure Mode** | Hallucination, incorrect facts | Wasteful over-engineering, building the wrong product |

---

## 2. Semantic Entropy in User Requests

When a user submits an instruction $X$, the space of valid candidate solutions $\mathcal{Y} = \{Y_1, Y_2, \dots, Y_k\}$ can exhibit varying entropy:

$$H(\mathcal{Y} \mid X) = -\sum_{i=1}^k P(Y_i \mid X) \log P(Y_i \mid X)$$

- **Single-Peaked Distribution ($H \approx 0$)**: One dominant interpretation ($P(Y_1 \mid X) \approx 1$). Examples:
  - "Rename `getUser` to `fetchUser` in `api.ts`."
  - "Add a type annotation to this function."
  *Action*: Execute immediately without gating.
- **Multi-Modal / High-Entropy Distribution ($H \gg 0$)**: Multiple distinct clusters of valid deliverables ($P(Y_1) \approx P(Y_2) \approx P(Y_3)$). Examples:
  - "Design an authentication layer." (JWT stateless vs. session-cookie vs. OAuth2/OIDC proxy).
  - "Optimize my training loop." (Distributed DDP vs. Mixed Precision/FP8 vs. DataLoader I/O prefetching).
  *Action*: Trigger the Aleatoric Uncertainty Resolver.

---

## 3. Common Divergence Archetypes

### Archetype A: Abstraction & Scope
- **Branch 1**: Minimal proof-of-concept / scratch script.
- **Branch 2**: Production-grade modular system with error handling and configuration.
- **Branch 3**: Enterprise distributed service with telemetry and observability.

### Archetype B: Modality & Deliverable Type
- **Branch 1**: Mathematical formulation / theoretical proof sketch.
- **Branch 2**: Runnable implementation code.
- **Branch 3**: Architecture design document / RFC / trade-off comparison.

### Archetype C: Optimization Objective Function
- **Branch 1**: Latency / Memory minimization (e.g. low-overhead C/Rust extension, SIMD, in-memory buffers).
- **Branch 2**: Throughput / Horizontal scalability (e.g. distributed batching, Kafka queue).
- **Branch 3**: Code simplicity & developer velocity (e.g. clean Python stdlib, readability over raw speed).

### Archetype D: Ecosystem & Dependency Posture
- **Branch 1**: Zero-dependency / pure standard library.
- **Branch 2**: Standard open-source industry stack (e.g. PyTorch, FastAPI, Redis).
- **Branch 3**: Cloud-managed service abstraction (e.g. AWS Lambda, DynamoDB, GCP Vertex).

---

## 4. Gating Threshold Heuristic

Activate the resolver gate if ANY of the following hold true:
1. **Regime Count**: There are $\ge 2$ distinct, incompatible implementation paths where work on Path A would be discarded if the user intended Path B.
2. **Blast Radius**: Estimated implementation effort $\ge 100$ lines of code or $\ge 3$ distinct files.
3. **Implicit Dependencies**: The choice implies introducing external infrastructure (databases, message brokers, external services).
