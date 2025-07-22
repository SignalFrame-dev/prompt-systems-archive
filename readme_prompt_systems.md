# SignalFrame | Prompt Systems Archive

This archive contains versioned, tested, and structured prompt systems authored by SignalFrame.

Each system includes:

- Versioned prompt evolution
- Model-specific evaluation notes
- Failure handling and constraint rationale
- Scoring tables (where applicable)
- Output samples and hallucination controls

## Current Systems

### 🏥 EMR Triage Summary

**Use Case Overview:**\
The EMR Triage Summary system converts nurse-written triage notes into a structured, physician-readable summary for downstream use in Electronic Medical Records. It extracts core clinical elements such as patient name, symptom onset, vitals, and medical risk factors while enforcing strict scope control. Designed for clinical clarity and high reproducibility, this system supports EMR pre-processing, intake workflows, and telehealth routing.

**What Makes This Work:**\
The prompt uses aggressive hallucination suppression and scope anchoring to prevent false positives, especially regarding patient condition or diagnosis. Rather than allowing interpretation or paraphrasing, the system enforces extraction of only what is explicitly stated in the triage note. Its layered instruction design also guides the model through domain-specific structure without overstepping clinical boundaries.

**Prompt (Redacted for Controlled Disclosure):**

```markdown
Your role: Convert the following triage note into a structured summary for physician review. Return only the items listed below. Do not interpret, diagnose, or include any content not present in the note.

Items to extract in this exact order:
- Patient name
- Birthday if present
- Chief complaint as written
- Symptom onset as stated
- Nurse observations (physical findings, behavior, context)
- Key vitals if present (e.g., HR, BP, O₂ sat, temperature)
- Risk factors if stated (e.g., diabetes, hypertension, edema)

Output format:
Return as a labeled bullet list using this order. If an item is not present, omit the label entirely.

Formatting rules:
- No introduction, greeting, or sign-off
- No assumptions or restatements
- No citations
- Do not summarize

(Advanced edge-case logic, error prevention design, and model-specific constraints redacted.)
Full version available upon request for clinical integration or QA collaboration.
```

**Model Test Status:**\
Passed full QA and adversarial stress testing across 7 models including GPT-4o, Claude Opus, Gemini 1.5 Pro, GPT-3.5 (3o), Mistral, Meta AI, and Perplexity. Demonstrated stable outputs under 50+ hours of cross-model testing.

---

### 📄 Legal Clause Extractor v1

**Use Case Overview:**\
Legal Clause Extractor v1 is a structured extraction system designed to retrieve obligations, restrictions, and renewal terms from legal or contract-like text. Built for use in legal tech and operations automation, this system converts unstructured legal input into labeled, scoped outputs. It is currently in QA version 2.7 and undergoing cross-model stress testing.

**What Makes This Work:**\
This system uses a rule hierarchy and constraint-layering strategy to eliminate hallucinations, scope creep, and ambiguous outputs. Instructions are sequenced to minimize inference pressure, guide compliance, and preserve context without overreach. The result is a robust, model-agnostic structure capable of surviving complex contract phrasing and formatting irregularities.

**Prompt (Redacted for Controlled Disclosure):**

```markdown
Your role: extract clause-level items from contract-like input text. Return only what is explicitly stated in the text.

Scope:
- Do not summarize or infer
- Do not include boilerplate or generic content
- Do not rewrite or rephrase
- Ignore formatting or visual layout cues unless specified

Items to extract:
- Legal obligations
- Restrictions or prohibitions
- Renewal terms or clauses

Output format:
Return each item as a labeled bullet list. If no item is present in the text, omit that section entirely.

Example format:
- Obligation: [text from contract]
- Obligation: [text from contract]
- Restriction: [text from contract]
- Renewal: [text from contract]

Important constraints:
- Do not hallucinate
- Do not fabricate missing sections
- Do not restate the instruction
- Return only the labeled list

(Advanced rule handling and ambiguity resolution instructions redacted.)
Full version available upon request for enterprise review or collaboration.
```

**Model Test Status:**\
Version 2.2 passed initial QA across GPT-4o and Claude Opus. Version 2.7 is now in cross-model stress testing with GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, and GPT-3.5.

---

*SignalFrame designs prompt systems that contain ambiguity, enforce clarity, and scale across models.*

