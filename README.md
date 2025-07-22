# SignalFrame | Prompt Systems Archive

## 📄 Legal Contract Clause Extractor (v2.7)
## 🏥 EMR Nurse Triage Summary Extractor (v1.0)

## Systems  
- [📄 Legal Contract Clause Extractor](#legal-contract-clause-extractor)  
- [🏥 EMR Nurse Triage Summary Extractor](#emr-nurse-triage-summary-extractor)

This archive contains enterprise-grade, versioned prompt systems authored by **SignalFrame** — designed for scale, precision, and hallucination control across AI model families.

Each system includes:
- Constraint design rationale
- Multi-round, multi-model QA test records
- Human red team adversarial challenge status (if applicable)
- Output samples and edge-case notes
- Public-safe prompt version for review and reference

---

## 📄 Legal Contract Clause Extractor

**Purpose:**  
Extracts *key contractual obligations, restrictions,* and *renewal terms* from legal and policy documents. Prioritizes semantic accuracy and strict scope compliance under legal review standards.

**Highlights:**
- Version 2.7 passed all hallucination, format, and ambiguity QA tests across GPT-4o, Claude 3.5, Gemini 1.5 Pro, GPT-3.5
- Survived human red team testing with only one soft hallucination in v2.2 (fully patched in final)
- Prompt design includes rule prioritization logic, formatting constraints, and execution bias protocols (redacted in public-safe version; available by request for enterprise review or research collaboration)
- Final version now under extended testing phase

---

- Case study publication pending
- Final public-safe prompt will be published after extended test phase

---

## 🏥 EMR Nurse Triage Summary Extractor

**Purpose:**  
Summarizes triage notes into structured medical summaries for EMR integration. Outputs include patient name, birthday, chief complaint, symptom onset, nurse observations, vitals, risk factors.

**Highlights:**
- Survived over 60 hours of adversarial stress testing
- Consistently compliant across GPT-4o, Claude 3.5, Gemini 1.5 Pro, GPT-3.5, Perplexity, Mistral, and Meta AI during 60+ hours of testing
- Hallucination-free across known edge cases
- Currently under final audit for deployment in HealthTech prototype systems

[🧠 Read the full EMR Case Study →](emr-nurse-triage-summary/CaseStudy.md)  
[📜 See the final public-safe prompt →](emr-nurse-triage-summary/EMRPrompt_Final.txt)

---

## 🧪 Coming Soon

- Prompt scoring harness (Python)
- Visual layout testing systems
- Failure-mode pattern library
- API simulation testing

---

**About SignalFrame**  
SignalFrame builds unbreakable prompt systems that contain ambiguity, enforce clarity, and scale across foundation models. Every system is structured for production-level QA.

*This archive is continuously updated as systems complete QA and are cleared for public review.*

### 📜 Usage and Permissions
All content © SignalFrame. Public-safe prompt versions may be used for reference or educational purposes with attribution. Redistribution, modification, or commercial use of full prompt systems requires written consent.

