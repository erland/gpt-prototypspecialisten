# Validering och kvalitetsgates

Steg 5 definierar hur Prototypspecialisten avgör om en prototyp verkligen är demonstrerbar och leveransklar.

Valideringen kombinerar deterministiska kontroller med strukturerad UX-granskning. Build, centrala filer, hosting, huvudflöden och exempeldata är blockerande i normalfallet. Mobil, tablet och desktop ska bedömas när målplattformen inte avgränsats.

Agent Workspace är föredragen valfri runtime för faktisk verifiering när den finns och är konfigurerad. Normalt tas bara en desktop-screenshot; tablet/mobil tas vid behov. Responsiv bedömning kvarstår för alla relevanta formfaktorer.

Browser-rendering är önskvärd men inte ett hårt krav. Om Agent Workspace/Playwright/Chromium saknas får layoutgranskning och tydligt märkt mockup användas som fallback. Däremot får faktisk build aldrig påstås vara verifierad utan evidens.

Se canonical policy i `assistant/policies/validation-quality-gates.md`.
