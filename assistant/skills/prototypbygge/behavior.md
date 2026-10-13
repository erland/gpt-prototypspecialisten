## Standardteknik

Följ `assistant/policies/code-generation-contract.md`. Standard är React, TypeScript och Vite, frontend-only, statiska resurser och inga externa API-nycklar, databaser eller produktionsautentisering om användaren inte uttryckligen behöver det.

Exempeldata ska vara deterministisk och demonstrationsbar. Använd ett tunt simulerat service-/state-lager vid mer än trivial interaktion. Använd normalt `localStorage` när demoändringar ska överleva omladdning och erbjud återställning. GitHub Pages-routing och Vite `base` ska fungera från repo-subpath.

## Leveranskrav

Normal leverans: körbar källkod, realistisk exempeldata, responsivt gränssnitt, minst ett komplett demonstrationsscenario, README, statisk build/deployment-konfiguration, GitHub Pages-stöd när GitHub används, lista över simulerade funktioner, kort UX-bedömning samt faktisk screenshot där möjligt eller tydligt märkt mockup annars.

