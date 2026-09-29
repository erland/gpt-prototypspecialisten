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

## Fallback

Playwright/Chromium är aldrig ett krav för kärnleveransen. Browserfel registreras, men en godkänd frontend-build och övriga kvalitetsgates får fortsätta till leverans. Mockup eller code preview används som tydligt märkt ersättning.
