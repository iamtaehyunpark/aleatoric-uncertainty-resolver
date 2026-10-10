# Aleatoric Uncertainty Resolver Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Multi-Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20Claude.ai%20%7C%20Antigravity%20%7C%20CLI-blue.svg)](#multi-platform-deployment)

Disambiguate inherently uncertain, under-specified, or high-entropy user requests by decomposing divergent interpretations, simulating expected outcomes for each path, and providing a structured decision gate before costly execution occurs.

---

## Directory Structure

```text
aleatoric-uncertainty-resolver/
├── SKILL.md                 # Complete agent instructions, 4-phase workflow, and guardrails
├── README.md                # Multi-platform deployment guide, architecture, and CLI usage
├── references/
│   ├── entropy_taxonomy.md  # Theoretical framing: aleatoric vs epistemic, mathematical entropy
│   └── decision_templates.md# Ready-to-use decision matrix templates for common archetypes
└── scripts/
    └── gate_formatter.py    # Standalone CLI validation and formatting utility
```

---

## Problem: The Cost of Guessing Under High Entropy

When an LLM agent encounters an ambiguous, under-specified prompt (e.g. *"Build an indexing pipeline"* or *"Implement semantic caching"*), default behaviors tend to:
1. **Arbitrarily guess** one implementation path without stating assumptions.
2. **Generate large blocks of code** or architecture files that might target the wrong regime (e.g. In-memory trie vs. distributed Redis vector store).
3. **Trigger deep rework cycles** and token exhaustion when the user inevitably clarifies: *"No, I meant an embedded local module, not a distributed service."*

The **Aleatoric Uncertainty Resolver** acts as a lightweight **circuit breaker**: it detects high semantic entropy ($\ge 2$ mutually incompatible regimes), halts downstream code generation, simulates candidate branches under strict brevity limits, and presents a deterministic decision gate (`[Option A]`, `[Option B]`, etc.) to the user.

---

## 4-Phase Operational Workflow

```
[High-Entropy User Prompt]
           │
           ▼
[Phase 1: Entropy Check]
  Formalize intent & check for ≥ 2 diverging target regimes
           │
           ▼
[Phase 2: Divergent Path Enumeration]
  Isolate 2 to 4 principal interpretations with underlying philosophies
           │
           ▼
[Phase 3: Generative Outcome Simulation]
  Strict brevity: ≤ 3 sentences per branch, 1-line deliverable, 1-3 line micro-snippet
           │
           ▼
[Phase 4: Structured Selection Gate]
  Deterministic keys ([Option A], [Option B]) + Decision Matrix + Direct interactive prompt
```

---

## Multi-Platform Deployment Guide

### 1. Claude Code

Install globally across all repositories or locally within your current project:

```bash
# Global installation
mkdir -p ~/.claude/skills
cp -r aleatoric-uncertainty-resolver ~/.claude/skills/

# Project-scoped installation
mkdir -p .claude/skills
cp -r aleatoric-uncertainty-resolver .claude/skills/
```

### 2. Antigravity & Antigravity CLI

Install into your Antigravity skills directory:

```bash
# Antigravity CLI global skill location
mkdir -p ~/.gemini/antigravity-cli/skills
cp -r aleatoric-uncertainty-resolver ~/.gemini/antigravity-cli/skills/

# Project-scoped installation
mkdir -p .agents/skills
cp -r aleatoric-uncertainty-resolver .agents/skills/
```

### 3. claude.ai Web Interface

Package the directory into a zip archive and upload it in **Settings > Features > Skills**:

```bash
zip -r aleatoric-uncertainty-resolver.zip aleatoric-uncertainty-resolver/
```

### 4. Claude API / Anthropic Skills API

Include `aleatoric-uncertainty-resolver/` in your container or custom prompt bundles.

---

## CLI Gate Formatter Utility

Use `scripts/gate_formatter.py` to validate gate data and print standardized matrices:

```bash
# Run built-in demo
python3 scripts/gate_formatter.py --demo

# Validate and format custom JSON definition
python3 scripts/gate_formatter.py --file path/to/options.json
```

### Example JSON Input Schema (`options.json`):
```json
{
  "input_analysis": "Ambiguity in vector search implementation regarding local vs cloud deployment.",
  "options": [
    {
      "title": "Local FAISS / HNSW Index",
      "philosophy": "In-process vector similarity search using FAISS with local embeddings.",
      "deliverable": "Self-contained Python script using faiss-cpu.",
      "shape_summary": "Python module (FAISS)",
      "pro": "Zero server infrastructure, sub-millisecond local latency",
      "con": "Bound by local process RAM, single-instance only",
      "snippet": "index = faiss.IndexFlatL2(d)\nindex.add(xb)"
    },
    {
      "title": "Managed Vector Database Client",
      "philosophy": "Cloud-native distributed vector search backed by Pinecone or Weaviate.",
      "deliverable": "Async client integration with connection pool and batch upserts.",
      "shape_summary": "Client SDK + API Wrapper",
      "pro": "Hands-off horizontal scalability and metadata filtering",
      "con": "Requires external API keys and network roundtrips"
    }
  ]
}
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
