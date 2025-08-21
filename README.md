# SignalFrame | Prompt Systems Archive

This archive contains versioned, tested, and structured prompt systems authored by SignalFrame.  
Each system is maintained with version history, test logs, and case study documentation.

---

## Current Systems

### 🏥 EMR Nurse Triage Summary
- **Purpose:** Extract structured clinical data from triage notes for physician review in EMR systems.  
- **Baseline:** v1.4_Locked  
- **Testing:** Passed compliance across GPT-4o, Claude 3.5, Gemini 1.5 Pro, Perplexity, Mistral, and Meta AI after 50+ hours of stress testing.  
- **Failure history:** v1.0 archived — partial paraphrasing and over-labeling observed, corrected in later versions.  
- **Folder:** [`systems/emr-triage-summary`](systems/emr-triage-summary)  

---

### 📄 Legal Contract Clause Extractor
- **Purpose:** Extract obligations, restrictions, and renewal/termination clauses from contract text.  
- **Baseline:** v2.9_Locked  
- **Testing:** Passed compliance across GPT-4o, Claude 3.5, Gemini 2.5 Flash, and Perplexity. All models produced identical, verbatim outputs.  
- **Failure history:** v2.7 archived — failed due to paraphrasing, truncation, and Gemini commentary drift. Hardened into v2.9_Locked.  
- **Folder:** [`systems/legal-contract-extractor`](systems/legal-contract-extractor)  

---

## Versioning Policy
- **Locked versions** (e.g., `v1.4_Locked`, `v2.9_Locked`) represent hardened, tested baselines safe for public use.  
- **Earlier versions** are archived for transparency but are not intended for production use.  
- Failure versions (e.g., EMR v1.0, Legal v2.7) are explicitly preserved to document known weaknesses and the fixes applied.  

---

## Testing
- Each locked version undergoes adversarial and multi-model compliance testing.  
- Results are stored in system-specific `tests/` folders.  
- Logs record pass/fail outcomes, format compliance, and hallucination control.  

---

*SignalFrame designs prompt systems that eliminate ambiguity, enforce clarity, and scale across models.*
