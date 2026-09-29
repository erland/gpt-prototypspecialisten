# Workflow- och state-policy

Projektets workflow är explicit för att samma GPT ska fungera robust över olika modellnivåer.

- `idea_analysis` → förstå behov, användare och referenser.
- `architecture` → definiera scope, IA, flöden, data och responsiv strategi.
- `planning` → planera avgränsat genomförande och leveranser.
- `implementation` → skapa eller ändra prototyp och projektartefakter.
- `validation` → kontrollera build, scenarier, responsivitet och relevanta kvalitetsgates.
- `packaging` → skapa leveranspaket och statisk deploy-konfiguration.
- `release` → bedöm release readiness och leverera.
- `maintenance` → iterera efter feedback eller återuppta tidigare projekt.
- `blocked` → använd när en verklig blockerare hindrar fortsatt arbete.
- `paused` → använd när arbetet avsiktligt avbryts utan blockerare.

Övergångar följer `gpt-project.yaml`. Status ska uppdateras först efter relevant validering.
