# Legal Contract Clause Extractor

## 🔍 What It Does
- Extracts three clause types from contract text:  
  - **Obligations**  
  - **Restrictions**  
  - **Renewal/Termination**  
- Reproduces each clause **verbatim**, preserving full sentence boundaries.  
- Outputs in a strict, labeled format for legal review.  

---

## 🧠 Design Principles
- Enforces **scope-only extraction** (no unrelated clauses).  
- Requires **word-for-word reproduction** — no paraphrasing or commentary.  
- Omits labels entirely if a clause type is absent.  

---

## 📄 Files Included
- `legal-contract-extractor-v2.9_Locked.md` — current baseline prompt  
- `case-study.md` — applied contract scenarios and notes  
- `human-context.md` — authorship rationale and design context  
- `tests/` — compliance logs  
- `archive/` — earlier versions and QA summaries  

---

## 🏷 Version Info
- **Current baseline:** v2.9_Locked (2025-07-28)  
- **Tested models:** GPT-4o, Claude 3.5, Gemini 2.5 Flash, Perplexity  
- **Result:** Passed structured compliance tests (verbatim + format + scope)  

---

## Versioning Notes
- **Locked versions** = tested baselines, safe for reference.  
- **Earlier versions** are archived for transparency but not intended for active use.  
- **v2.7 specifically failed**: models drifted on paraphrasing, truncation, and commentary. This version is preserved in `/archive` as a record of failed compliance.  
- **v2.9_Locked** incorporated fixes and passed compliance across all tested models.  

---

SignalFrame · [GitHub](https://github.com/SignalFrame-dev)
