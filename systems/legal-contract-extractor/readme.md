# Legal Contract Clause Extractor

This system-level prompt extracts only the **contractual obligations**, **restrictions**, and **renewal terms** from legal, policy, or contract-like input text.  
It is engineered for strict scope control, ambiguity filtering, and multi-model compliance.

---

## 🔍 What It Does
- Extracts only actionable items explicitly stated in the input  
- Filters out summaries, party identifiers, and non-binding language  
- Enforces structured, reproducible format for downstream automation or review  

---

## 🧠 Design Principles
- Constraint-layered design with refusal fallback logic  
- Explicit scope boundaries and no-inference guardrails  
- Null-output allowed where sections are absent  
- Model-agnostic structure validated across multiple LLMs  

---

## 📄 Files Included
- `legal-contract-extractor-prompt-v2.9_Locked.md` — current hardened baseline prompt  
- `case-study.md` — applied case study and scenario notes  
- `human-context.md` — authorship rationale and IP framing  
- `tests/` — model compliance logs  
- `archive/` — previous versions (e.g., v2.7) kept for transparency  

---

## 🏷 Version Info
- **Current baseline:** v2.9_Locked (2025-07-28)  
- **Tested models:** GPT-4o, Claude 3.5, Perplexity, Gemini 2.5 Flash  
- **Result:** All models produced identical, fully compliant outputs on benchmark input  

---

## Versioning Notes
- **Locked versions** (e.g., `v2.9_Locked`) represent hardened, tested baselines safe for public use.  
- **Earlier versions** (e.g., v2.7) are archived for historical transparency but are not intended for production use.  

---

*Note: Public release omits internal fallback handling and full model-specific execution logic.*  

---

SignalFrame · [GitHub](https://github.com/SignalFrame-dev)
