# {{GPT_NAME}} – OpenCode

Version: `{{VERSION}}`

Detta paket är OpenCode-distributionen av {{GPT_NAME}}. Lägg innehållet i roten av den workspace/repository där assistenten ska arbeta.

## Viktiga filer

- `AGENTS.md` – genererad runtime-instruktion från canonical assistant-instruktionen.
- `opencode.json` – OpenCode-konfiguration och permissions.
- `runtime-contract.json` – snapshot av capabilities, artifacts, workspace/state och tools.
- `.opencode/skills/` – projektlokala återanvändbara skills när de är aktiverade.
- `knowledge/` – stödjande kunskap; kärnbeteende får inte vara beroende av denna katalog.

## Arbetssätt

OpenCode ska arbeta workspace-first. För en prototyp innebär det normalt att analysera behovet, skapa `prototype-spec.yaml`, implementera React/TypeScript/Vite-projektet, köra tillgängliga build-/valideringskommandon och uppdatera projektstatus först efter godkända gates.

Browser-rendering är en förstärkning, inte ett blockerande krav. Om Chromium/Playwright saknas ska övrig implementation och deterministisk validering fortsätta.
