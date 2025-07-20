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

### 🚫 Dangerous Techniques
- “Summarize in your own words” without scoping  
- “Simplify this” in clinical/legal contexts  
- Any instruction lacking an inference boundary  
- Broad use of “relevant,” “important,” or “significant”

---

## SignalFrame Principle

> *Contain hallucination by design. Not by correction.*

Prompt systems should enforce *clarity through constraint*, not after-the-fact review.

---

This document evolves with usage. For implementation examples, see:
- `emr-triage-summary/V2_prompt.md`
- `legal-contract-clause-extractor/V1_prompt.md`

