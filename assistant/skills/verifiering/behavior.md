## Validering och kvalitetsgates

Följ `assistant/policies/validation-quality-gates.md` och dokumentera i `validation-report.yaml`.

Håll evidensnivåerna separata:
- `build_verified`
- `preview_deployed`
- `browser_verified`

Ingen nivå får härledas enbart från en annan. Saknad preview/browser är inte blockerande om övriga gates passerar. Om målplattformen inte avgränsats ska mobil 390×844, tablet 768×1024 och desktop 1440×900 bedömas. Påstå aldrig att build, preview, screenshot eller interaktion är verifierad utan faktisk evidens.

