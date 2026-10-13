# Modulära skills – Prototypspecialisten

Version: 0.1.0-rc.5 (kandidat)

Sex kanoniska skills är separata källmoduler. `assistant/core.md` innehåller identitet, kärnregler och operativ kärna. `assistant/assembly.json` återskapar exakt den äldre instruktionen, utan beteendeförändring. `assistant/instructions.md` finns kvar som historiskt jämförelseunderlag; den kanoniska kompileringen bygger på core och modulernas `source`.

För full godkännandestatus behövs GitHub Actions och manuella installationstester i Chat ZIP och Plugin.
