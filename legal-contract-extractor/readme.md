# Legal Contract Extractor

This system-level prompt extracts only the **key contractual obligations**, **restrictions**, and **renewal terms** from legal policy or contract text. It is engineered for strict scope control, ambiguity filtering, and multi-model stability.

## 🔍 What it Does
- Filters out boilerplate, summaries, party names, and non-binding language
- Extracts only the core actionable items explicitly stated in the text
- Complies with strict formatting rules for structured downstream use

## 🧠 Design Principles
- Brutal constraint enforcement
- Clear rule hierarchy for edge case handling
- Permission-based null output: returns “No items to extract” when needed
- Model-agnostic: tested across GPT-4o, Claude 3.5, Gemini 1.5 Pro, GPT-3.5

## 📄 Files Included
- `prompt-v1.0.md`: The extraction system prompt (currently v2.7)
- `case-study.md`: Step-by-step case study with rationale and sample inputs
- `human-context.md`: Author notes and design framing for future collaborators

## 🚧 Status
- ✅ Final version (2.7) uploaded
- 🧪 Extended QA testing in progress (model and human red team)

## 🏷 Version
**Current:** v2.7  
**Tested Models:** GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-3.5 (3o)

---

SignalFrame · [GitHub](https://github.com/SignalFrame-dev)
