# Project – Prototypspecialisten

Canonical GPT-projekt för en UX-fokuserad expert på körbara, responsiva webbprototyper med realistisk exempeldata.

Aktiverade och validerade runtimes: ChatGPT Chat, Custom GPT och OpenCode.

Auktoritativ status finns i `project-status.yaml`. Utvecklingsplan finns i `docs/development-plan.md`.

## OpenCode

OpenCode är den kodcentrerade peer-runtimen för faktisk prototypimplementation, build och validering. Distributionen genereras från canonical instruktion till `AGENTS.md`, använder `opencode.json` för explicita permissions och inkluderar `runtime-contract.json` samt projektlokala skills.

## Evals och modellrobusthet

Modellrobustheten verifieras med scenarier för idé, skärmdump, URL, responsiv översättning, formulär/fel, browser-fallback, återupptagning och runtime parity. Coverage valideras deterministiskt av `scripts/validate_eval_coverage.py`.
