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

Custom GPT kan använda Builder-capabilities och installerade plugins där kontot/runtime erbjuder dem. Externa verktyg behandlas som optional capability providers: Agent Workspace för build/verifiering och artefakt, PWA Preview för temporär publik preview och Browser Screenshot för browser-rendering. Full kedja används när alla relevanta verktyg finns; annars används den delmängd som faktiskt kan kopplas ihop.

Lokal shell/browser-rendering och dessa plugins är inte garanterade beroenden. Samma fallbackregel gäller därför i alla runtimes: saknad preview eller browser får inte ensam blockera prototypleveransen och får aldrig beskrivas som verifierad utan evidens.
