# Custom GPT-runtime

Steg 7 paketerar Prototypspecialistens canonical beteende för ChatGPT Custom GPT Builder utan att flytta kritiska regler till Knowledge.

## Builder-paket

Distributionen innehåller:

- `builder/instructions.md` – canonical instruktion inom 8 000 tecken,
- `builder/conversation-starters.md` – startförslag,
- `builder/capabilities.md` – härledda Builder-capabilities,
- `builder/runtime-contract.json` – adapterkontrakt,
- `builder/knowledge-package/` – endast icke-kritisk referenskunskap om sådan finns,
- `builder/compilation-report.json` – spårbar rapport över instruktion och knowledge-urval,
- `README.md` och `COMPATIBILITY.md` – installations- och paritetsinformation.

## Principer

Custom GPT och Chat ZIP är peer-distributioner från samma canonical instruktion. Kritiska regler för UX-workflow, exempeldata, responsivitet, browser-fallback, kodgenerering och validering ska finnas i instruktionen och får inte göras beroende av Knowledge.

Instruktionen byggs i `identical`-läge. Om den canonical texten växer över 8 000 tecken ska den först förenklas i canonical källan; buildsteget får inte lösa överflödet genom att flytta beteende till Knowledge.

## Capability-paritet

Custom GPT kan använda Builder-capabilities som webbsökning, kodexekvering/dataanalys, bildgenerering och filhantering där kontot/runtime erbjuder dem. Lokal shell/browser-rendering är inte ett garanterat inbyggt beroende. Samma fallbackregel som i canonical kontrakt gäller därför: en misslyckad eller saknad Chromium/Playwright-miljö får inte ensam blockera prototypleveransen.
