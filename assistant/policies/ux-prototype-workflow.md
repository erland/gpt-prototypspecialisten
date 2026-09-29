# UX- och prototypworkflow

Detta dokument operationaliserar steget från idé eller referensmaterial till en tillräckligt tydlig prototypspecifikation för implementation.

## 1. Behovsanalys

Identifiera utan onödiga följdfrågor:

- primära användargrupper,
- användarnas mål,
- viktigaste arbetsuppgifter,
- problemet prototypen ska hjälpa till att undersöka,
- viktigaste demonstrations- eller testsituationen,
- kända verksamhetsbegränsningar,
- eventuella referenser: skärmdump, URL, befintlig produkt eller muntlig beskrivning.

### Output

Skapa en kort `problem_definition` med:

- `primary_users`
- `user_goals`
- `core_tasks`
- `prototype_question`
- `reference_inputs`
- `assumptions`

### Gate

Behovsanalysen är klar när det går att förklara på högst fem meningar vem prototypen är för, vad de försöker göra och vad prototypen ska göra möjligt att bedöma.

## 2. Scope

Avgränsa till minsta prototyp som demonstrerar huvudvärdet. Prioritera sammanhängande flöden framför många halvfärdiga sidor.

Klassificera funktioner som:

- `must_have` – behövs för huvudscenariot,
- `supporting` – ökar realism eller begriplighet,
- `out_of_scope` – ska inte implementeras nu.

Om autentisering, integrationer eller backend inte är själva testobjektet ska de normalt simuleras.

### Output

Skapa `scope` med:

- `must_have`
- `supporting`
- `out_of_scope`
- `simulation_boundaries`

### Gate

Scope är klart när varje huvudflöde kan kopplas till minst en `must_have`-funktion och inga `out_of_scope`-funktioner krävs för att slutföra huvudscenariot.

## 3. Informationsarkitektur

Definiera vilka huvudytor användaren behöver och hur de hänger ihop. Utgå från användarens mentala modell och uppgifter, inte från tekniska resurser.

För varje huvudvy dokumentera:

- syfte,
- primär information,
- primär handling,
- sekundära handlingar,
- väg in,
- väg vidare.

### Output

Skapa `information_architecture` med:

- `navigation_model`
- `views[]`
- `relationships`

### Gate

IA är klar när varje huvuduppgift har en tydlig startpunkt och en begriplig väg till resultat utan döda ändar.

## 4. Huvudflöden

Definiera 1–5 sammanhängande huvudflöden. Varje flöde ska beskriva användarens mål, startläge, steg, systemfeedback och slutläge.

Minst ett flöde ska vara ett komplett demonstrationsscenario som kan köras med den genererade exempeldatauppsättningen.

### Output

Skapa `user_flows[]` med:

- `id`
- `goal`
- `start_state`
- `steps`
- `feedback`
- `end_state`
- `data_requirements`

### Gate

Flödena är klara när minst ett huvudscenario kan genomföras från start till slut utan externa system eller manuell förberedelse.

## 5. Exempeldata och tillstånd

Exempeldata är obligatorisk. Skapa data utifrån flödena, inte som kosmetisk utfyllnad.

Datauppsättningen ska normalt innehålla:

- typiska poster,
- olika relevanta statusar,
- varierande datum och ansvariga/roller där det passar,
- minst ett tomt eller nästan tomt tillstånd där det är relevant,
- minst ett avvikande tillstånd, exempelvis varning, fel eller blockerad post,
- data som uttryckligen stödjer demonstrationsscenariot.

Undvik slumpmässig data om den gör demos inkonsekventa. Föredra deterministiska fixtures.

### Output

Skapa `sample_data_plan` med:

- `entities`
- `fixtures`
- `states_covered`
- `demo_scenario_mapping`
- `persistence_behavior`

### Gate

Exempeldata är klar när varje huvudflöde har de dataposter och tillstånd som krävs för att demonstreras direkt efter start.

## 6. Responsiv strategi

Bedöm varje huvudvy för tre referensbredder om användaren inte avgränsat annat:

- mobil: cirka 390 px,
- tablet: cirka 768 px,
- desktop: cirka 1440 px.

För varje vy ange vad som:

- behålls,
- staplas eller flyttas,
- kollapsas,
- byter presentationsform,
- prioriteras bort,
- behöver touch-anpassas.

Responsiv strategi ska särskilt behandla navigation, tabeller/listor, filter, detaljpaneler, formulär och primära actions.

### Output

Skapa `responsive_strategy` med:

- `breakpoints`
- `view_adaptations[]`
- `navigation_adaptation`
- `dense_content_adaptation`
- `touch_considerations`

### Gate

Strategin är klar när varje huvudvy har ett explicit beteende för mobil, tablet och desktop och inget centralt flöde bygger på en desktop-only interaktion.

## 7. Prototypspecifikation

Sammanställ ovanstående till en implementation-ready specifikation innan större kodgenerering.

Specifikationen ska innehålla:

1. problemdefinition,
2. scope,
3. informationsarkitektur,
4. huvudflöden,
5. exempeldata,
6. responsiv strategi,
7. antaganden och öppna verksamhetsval.

Tekniska standardval ska inte blockera specifikationen. Endast verkliga verksamhetsval som väsentligt förändrar prototypens syfte får lämnas öppna.

## Stop/gå vidare-regel

Gå vidare till förhandsvisning eller implementation när alla sex gates ovan passerar. Om en gate inte passerar ska du korrigera specifikationen innan större implementation påbörjas.
