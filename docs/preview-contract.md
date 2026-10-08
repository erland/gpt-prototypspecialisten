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

## Optional capability pipeline

Prototypspecialisten använder tillgängliga verktyg som progressive enhancement:

- Agent Workspace: build/verifiering och temporär buildartefakt.
- PWA Preview: temporär publik HTTPS-hosting av byggd statisk artefakt.
- Browser Screenshot: faktisk browser-rendering av publik URL.

När alla tre finns är normal kedja Agent Workspace → PWA Preview → Browser Screenshot. Partiella kombinationer används endast när deras verkliga in-/utdata går att koppla ihop. Inget av verktygen är obligatoriskt.

Screenshot-strategin är desktop-first: normalt tas bara 1440×900. Tablet/mobil tas vid uttrycklig begäran, responsiv förändring, hög responsiv risk eller uppföljning. Responsiv kvalitet bedöms fortfarande för alla relevanta formfaktorer.

## Fallback

Saknade plugins, Playwright eller Chromium är aldrig krav för kärnleveransen. Build, preview och browser-verifiering rapporteras som separata evidensnivåer. Ett browser-/previewfel får inte radera en tidigare verifierad build.
