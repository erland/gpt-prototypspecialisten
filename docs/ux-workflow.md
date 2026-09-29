# UX-workflow – sammanfattning

Steg 2 operationaliserar arbetet före implementation. Den centrala arbetsartefakten är en prototypspecifikation med sex obligatoriska delar och gates:

1. behovsanalys,
2. scope,
3. informationsarkitektur,
4. huvudflöden,
5. exempeldata,
6. responsiv strategi.

Detaljerad policy: `assistant/policies/ux-prototype-workflow.md`.
Mall: `templates/prototype-spec/prototype-spec.yaml`.

## Designbeslut

- Exempeldata genereras alltid som del av processen.
- Data ska vara deterministisk nog för repeterbara demonstrationer.
- Minst ett komplett demonstrationsscenario ska fungera utan extern backend.
- Responsivitet definieras per huvudvy och omfattar mobil, tablet och desktop.
- Desktopmönster får byta presentationsform på mindre skärmar; responsivitet är inte liktydigt med proportionell skalning.
- Tekniska standardval får inte skapa onödiga följdfrågor.

## Gate till nästa fas

Förhandsvisning eller större kodimplementation får starta när samtliga sex workflow-gates är `pass` eller när en medveten användaravgränsning gör en gate irrelevant och det dokumenteras explicit.
