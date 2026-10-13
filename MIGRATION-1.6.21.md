# Migrering till GPT Byggaren 1.6.21

## Versioner och omfattning

- Ursprung: Prototypspecialisten `0.1.0-rc.3`.
- Första mellanliggande migrationsbygge: `0.1.0-migration.1` (historik, inte aktuell releasekandidat).
- **Aktuell releasekandidat: `0.1.0-rc.4`.**
- Fem aktiva distributioner: Chat ZIP, ChatGPT Plugin, Claude Project, Claude Skills och OpenCode.
- Custom GPT är avstängd som distributionsmål.
- Canonical instruktion och UX-/prototyppolicyer är bevarade.
- Agent Workspace, PWA Preview och Browser Screenshot förblir frivilliga integrationer.

## Motor, kompatibilitet och filer

Den versionsbundna originalmotorn finns i `tooling/gpt-byggaren-1.6.21/`. CI och release använder dess skript för kanonisk lint, distributionbygge och distributionsvalidering.

De befintliga skripten under `scripts/` behålls avsiktligt: de används av projektspecifika kontroller, paritetsvalidering och äldre regressionstester. Det finns således två koduppsättningar men **en explicit vald byggmotor i GitHub Actions**. Radera inte lokala skript utan en separat beroende- och regressionstestgenomgång.

Äldre `runtime.custom_gpt`-inställningar är inaktiva och finns kvar som kompatibilitetsmetadata. De får inte aktivera ett sjätte distributionsmål.

`.gitignore` utesluter bland annat `dist/`, `build/`, ZIP-arkiv och cachefiler. Dessa ska inte checkas in. Originalmotorns versionsbundna källkod under `tooling/` är däremot avsedd att versionshanteras.

## Kvalitet och nästa grind

- Lokal kontroll i migrationsarbetskopian: 9/9 regressionstester, kanonisk lint utan fel och varningar, distributionsvalidering och runtime-paritet godkända.
- Det är **inte likvärdigt med en verifierad GitHub Actions-körning** på PR-grenens commit.
- Före merge: kontrollera att GitHub Actions på PR-grenen passerar; granska filändringarna och kontrollera att inga byggartefakter lagts till.
- Före stabil release: gör manuella smoke-tester i respektive runtime, med och utan frivilliga integrationer där det är relevant.
- PR #5 är en releasekandidat och ska inte i sig betraktas som stabil release.
