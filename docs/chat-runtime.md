# ChatGPT Chat-runtime

ChatGPT Chat-distributionen är en genererad runtime från projektets canonical källor.

## Innehåll

- `START-HERE.md` är mänsklig entrypoint.
- `assistant/instructions.md` är canonical instruktion projicerad till runtime.
- `assistant/runtime-contract.json` är en kompilerad snapshot av capability-, artifact-, workspace/state- och tool-kontrakt.
- `assistant/policies/` innehåller de policies som canonical instruktionen hänvisar till.
- `schemas/` och `templates/` innehåller runtime-relevanta scheman och arbetsmallar.
- `knowledge/` innehåller endast icke-kritisk kunskap; kärnbeteende får inte vara beroende av Knowledge.

## Användning

Bifoga Chat ZIP-filen i en ChatGPT-konversation och ange att ZIP-filen ska användas som GPT-kontext för konversationen.

## Optional tool enhancement

Chat-runtimeen ska upptäcka tillgängliga kapabiliteter och använda dem utan att göra dem obligatoriska:

- Agent Workspace kan verifiera/builda prototypen och ge en temporär buildartefakt.
- PWA Preview kan hosta en nåbar statisk ZIP/tar.gz som temporär publik HTTPS-preview.
- Browser Screenshot kan rendera en publik URL och ta faktisk screenshot.

När alla tre finns är den föredragna kedjan Agent Workspace → PWA Preview → Browser Screenshot. Partiella kombinationer används endast när deras faktiska in-/utdata kan kopplas ihop. Saknade verktyg får inte blockera kärnflödet.

## Begränsningar

Chat-runtimeen kan skapa och redigera prototypfiler när hostmiljön har fil- och kodexekvering, men faktisk build, publik preview och browser-rendering är separata evidensnivåer. Om externa verktyg eller Chromium/Playwright saknas ska preview-kontraktets fallback användas.

## Validering

Distributionen ska minst innehålla entrypoint, version, manifest och canonical instruktion. Den får inte innehålla utvecklingskataloger som `evals/`, `tests/`, `research/`, Python-cache eller `.git`.
