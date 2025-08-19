# SignalFrame | Prompt Systems Archive

This archive contains versioned, tested, and structured prompt systems authored by SignalFrame.

Each system includes:

* Versioned prompt evolution
* Model-specific evaluation notes
* Failure handling and constraint rationale
* Output samples and hallucination controls

---

## Current Systems

### 🏥 EMR Triage Summary

**Use Case Overview:**  
The EMR Triage Summary system converts nurse-written triage notes into a structured, physician-readable summary for downstream use in Electronic Medical Records. It extracts core clinical elements such as patient name, symptom onset, vitals, and medical risk factors while enforcing strict scope control. Designed for clinical clarity and reproducibility, this system supports EMR pre-processing, intake workflows, and telehealth routing.

**Baseline Version:** v1.4_Locked  

**Model Test Status:**  
Passed full QA and adversarial stress testing across GPT-4o, Claude 3.5, Gemini 1.5 Pro, Perplexity, Mistral, and Meta AI. Demonstrated stable outputs under 50+ hours of cross-model testing.

---

### 📄 Legal Contract Clause Extractor

**Use Case Overview:**  
The Legal Contract Clause Extractor retrieves obligations, restrictions, and renewal terms from contract text. Built for legal tech and operations automation, this system converts unstructured legal input into labeled, scoped outputs. It is hardened for reproducibility and designed to withstand model variability and ambiguous contract phrasing.

**Baseline Version:** v2.9_Locked  

**Model Test Status:**  
Passed compliance testing across GPT-4o, Claude 3.5, Perplexity, and Gemini 2.5 Flash. All models returned identical, fully compliant outputs.

---

## Versioning Policy

- **Locked versions** (e.g., `v1.4_Locked`, `v2.9_Locked`) represent hardened, tested baselines safe for public use.  
- **Earlier versions** (e.g., v2.7) are archived for transparency but not intended for production use.  
- Each system includes:  
  - Prompt file(s) with versioned naming  
  - Test logs in `/tests` subfolder  
  - Case study and human-context documentation  

---

*SignalFrame designs prompt systems that eliminate ambiguity, enforce clarity, and scale across models.*
