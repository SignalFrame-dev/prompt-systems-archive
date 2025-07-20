# SignalFrame | Prompt Systems Archive

This archive contains versioned, tested, and structured prompt systems authored by SignalFrame.

Each system includes:
- Versioned prompt evolution
- Model-specific evaluation notes
- Failure handling and constraint rationale
- Scoring tables (where applicable)
- Output samples and hallucination controls

## Current Systems

### 🏥 EMR Nurse Triage Summary
- Prompt to extract structured clinical data from triage notes
- Tested across 7 models
- Survived 50+ hours of automated testing
- Case study included

### ⚖️ Legal Contract Clause Extractor
- Summarizes legal case data into bullet format for downstream review
- Scope-controlled, hallucination-safe
- Currently under multi-model evaluation

## Coming Soon

- Python scoring harness (hallucination + format detection)
- Visual layout test systems
- Failure-mode library

---
*SignalFrame designs prompt systems that contain ambiguity, enforce clarity, and scale across models.*
