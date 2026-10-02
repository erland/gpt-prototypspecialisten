# Förhandsvisning – sammanfattning

Canonical policy: `assistant/policies/preview-contract.md`.

## Standardbredder

- mobil: 390 px
- tablet: 768 px
- desktop: 1440 px

## Preview-typer

- `design_mockup` – genererad designbild, aldrig faktisk rendering.
- `app_screenshot` – fångad från den körbara prototypen med känd viewport och spårbar källa.
- `code_preview` – strukturell fallback när bild/browser saknas.

## Agent Workspace och screenshots

Agent Workspace är föredragen valfri runtime när den finns och är konfigurerad. Den används automatiskt för faktisk verifiering utan att användaren behöver begära det.

Screenshot-strategin är desktop-first: normalt tas bara 1440×900. Tablet/mobil tas vid uttrycklig begäran, responsiv förändring, hög responsiv risk eller uppföljning av ett känt problem. Responsiv kvalitet bedöms fortfarande för alla relevanta formfaktorer.

## Fallback

Agent Workspace, Playwright eller Chromium är aldrig krav för kärnleveransen. Browserfel registreras, men en godkänd frontend-build och övriga kvalitetsgates får fortsätta till leverans. Mockup eller code preview används som tydligt märkt ersättning.
