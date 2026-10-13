# Migrering till GPT Byggaren 1.6.21

- Ursprung: erland/gpt-prototypspecialisten, 0.1.0-rc.3
- Migreringskandidat: 0.1.0-migration.1
- Canonical instruktion och prototyprelaterade policies är bevarade.
- Custom GPT avvecklad som runtime; Claude Project och Claude Skills tillagda.
- Chat, Plugin och OpenCode byggs med samma originalmotor.
- Externa Agent Workspace, PWA Preview och Browser Screenshot förblir valfria.
- Den äldre runtime-paritetskontrollen har uppdaterats för de nya instruktionsmålen.
- Äldre GitHub-workflows bör granskas innan ändringarna publiceras; tidigare CI har historiska runtime-antaganden.
- Detta är en migreringskandidat, inte stabil release.

## Release quality update 0.1.0-rc.4

- Originalmotor v1.6.21 incheckningsbar i `tooling/gpt-byggaren-1.6.21`.
- CI/release använder originalmotorn för byggen och distributionstest.
- Paritetskontroll jämför nu riktiga genererade runtime-arkiv.
- Versionsbundet projekt-ZIP godkänns av releaseberedskapskontrollen.
- Regressionstesterna är 9/9; manuell runtime-smoke återstår innan stabil release.
