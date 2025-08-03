# Hallucination Boundaries in Prompt Design

**Author:** SignalFrame  
**Type:** Design ethics note  
**Status:** Living document

---

## Premise

Large language models are not neutral. They are prediction engines trained on latent bias, implicit context, and surface-level structure. In high-stakes domains, hallucination is not noise—it’s *risk.*

---

## Boundaries That Protect

### ✅ Acceptable Techniques
- “Only include information present in the input”
- Explicit field labeling
- Output format constraints (e.g., bullet-first, label-colon)
- Scope separation (e.g., instruction vs. metadata)
- Omission-based logic (e.g., “Omit if not documented”)

### 🚫 Dangerous Techniques
- “Summarize in your own words” without scoping
- “Simplify this” in clinical/legal contexts
- Any instruction lacking an inference boundary
- Broad use of “relevant,” “important,” or “significant”
- Catch-all prompts using “extract key takeaways” in regulated settings

---

## 🧭 SignalFrame Principle

> *Contain hallucination by design. Not by correction.*

Prompt systems should enforce *clarity through constraint*, not after-the-fact review.

---

## References and Examples

For implementation examples, see:
- `systems/emr-triage-summary/emr-triage-summary-V2-prompt.md`
- `systems/legal-contract-extractor/legal-contract-extractor-v1-prompt.md`
