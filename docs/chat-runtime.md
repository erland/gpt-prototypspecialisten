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

## Begränsningar

Chat-runtimeen kan skapa och redigera prototypfiler när hostmiljön har fil- och kodexekvering, men faktisk browser-rendering är inte garanterad. Om Chromium/Playwright saknas ska preview-kontraktets fallback användas. Detta får inte blockera en prototyp som i övrigt kan byggas och valideras.

## Validering

Distributionen ska minst innehålla entrypoint, version, manifest och canonical instruktion. Den får inte innehålla utvecklingskataloger som `evals/`, `tests/`, `research/`, Python-cache eller `.git`.
