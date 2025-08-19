# Legal Contract Clause Extractor

This system-level prompt extracts only the **contractual obligations**, **restrictions**, and **renewal terms** from legal, policy, or contract-like input text. It is engineered for strict scope control, ambiguity filtering, and multi-model compliance.

## 🔍 What It Does
- Filters out boilerplate, summaries, party identifiers, and non-binding language  
- Extracts only actionable items explicitly stated in the input  
- Enforces structured format for downstream automation or review

## 🧠 Design Principles
- Constraint-layered design with refusal fallback logic  
- Explicit scope boundaries and no-inference guardrails  
- Permission-based null output: omits sections when content is absent  
- Model-agnostic structure tested across major systems

## 📄 Files Included
- `prompt-v2.7.md` — current public-safe system prompt  
- `case-study.md` — case structure and sample scenario  
- `human-context.md` — authorship rationale and IP framing

## 🚧 Status
- ✅ Version 2.7 committed  
- 🧪 Extended QA testing in progress (SignalFrame manual + model red team)

## 🏷 Version Info
**Current:** v2.7  
**Tested Models:** GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-3.5 (3o)

## Versioning Notes

- **Legal Contract Clause Extractor — v2.9_Locked** is the current baseline.  
  - This version has passed compliance testing across multiple models (GPT-4o, Claude 3.5, Perplexity, Gemini 2.5 Flash).  
  - It is considered the hardened prompt for ongoing public reference.

- Earlier versions (e.g., v2.7) remain archived for historical transparency.  
  - These represent pre-lock iterations and may not reflect the current tested standard.  
  - They are kept in the repository to preserve version history, not for active use.

---

*Note: This public version omits internal rule hierarchy, fallback handling, and full model-specific execution logic.*

---

SignalFrame · [GitHub](https://github.com/SignalFrame-dev)
