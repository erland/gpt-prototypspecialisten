# Migrering till GPT Byggaren 1.6.21

## Versionshistorik och omfattning

- Ursprunglig projektversion: `0.1.0-rc.3`.
- Första migrationsbygge: `0.1.0-migration.1` (historik, inte aktuell version).
- Första uppdaterade releasekandidat: `0.1.0-rc.4` (PR #5, mergad).
- **Aktuell releasekandidat: `0.1.0-rc.5` (modulära skills, PR #6).**
- Fem aktiva distributioner: Chat ZIP, ChatGPT Plugin, Claude Project, Claude Skills och OpenCode.
- Custom GPT är avstängd som distributionsmål.
- Agent Workspace, PWA Preview och Browser Screenshot är fortsatt frivilliga integrationer.

## Modulär arkitektur i rc.5

- `assistant/core.md` innehåller gemensam identitet, kärnregler och arbetsledning.
- `assistant/assembly.json` anger ordning och ägarskap för instruktionens avsnitt.
- `assistant/skills/{ux-analys,responsiv-ux,preview-publicering,prototypbygge,verifiering,projektstatus}/behavior.md` är de sex kanoniska skillkällorna.
- `gpt-project.yaml` aktiverar `instructions.mode: modular_skills` och pekar ut källorna.
- Den sammansatta instruktionen jämfördes lokalt med tidigare kanonisk instruktion och var tecken för tecken identisk i migrationsarbetet.

## Motor, kompatibilitet och filhygien

Den versionsbundna originalmotorn finns under `tooling/gpt-byggaren-1.6.21/`. GitHub Actions använder denna motor för lint, distributionbygge och distributionsvalidering. Befintliga `scripts/` behålls avsiktligt för projektspecifika kontroller och regressionstester; radera dem inte utan separat beroendeanalys.

Inaktiva äldre `runtime.custom_gpt`-inställningar kan finnas kvar som kompatibilitetsmetadata, men ska inte generera en sjätte distribution.

`.gitignore` utesluter bland annat `dist/`, `build/`, ZIP-arkiv och cachefiler. Originalmotorns källkod i `tooling/` är däremot avsiktligt versionshanterad.

## Verifiering och releasegrindar

- Lokalt under rc.5-migreringen: kanonisk lint med 0 fel/0 varningar, 9/9 regressionstester, distributionsvalidering och runtime-paritet PASS.
- GitHub Actions på PR #6 ska kontrolleras efter ändringar; lokala tester utgör inte bevis på godkänd CI för PR-committen.
- Före merge: kontrollera aktuell CI, filändringar och att inga genererade paket eller cachefiler tillkommit.
- Före stabil release: genomför praktiska smoke-/acceptanstester i samtliga fem runtime-miljöer, särskilt Chat ZIP och Plugin med och utan frivilliga integrationer.

Denna PR avser en releasekandidat, inte en stabil release.
