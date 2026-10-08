# Validerings- och kvalitetsgates

Detta kontrakt styr när en genererad prototyp får beskrivas som validerad, demonstrerbar och leveransklar.

## 1. Grundprincip

En prototyp är inte klar enbart för att filer har genererats. Före leverans ska projektstruktur, dependency/build, statisk hosting, huvudflöden, exempeldata, responsivitet, accessibility, UX-kvalitet och preview-spårbarhet bedömas. Dokumentera i `validation-report.yaml`.

## 2. Resultatnivåer

Varje gate använder `pass`, `pass_with_warning`, `fail`, `not_applicable` eller under pågående arbete `not_tested`. Obligatoriska gates får inte lämnas `not_tested` i en slutlig leverans.

## 3. Separata evidensnivåer

Håll följande oberoende:
- `build_verified`: dependency/build har faktiskt verifierats.
- `preview_deployed`: en körbar publik preview har faktiskt skapats eller verifierats.
- `browser_verified`: aktuell prototyp har faktiskt laddats/renderats i browser.

En nivå får aldrig antas vara sann bara för att en annan är sann.

## 4. Blockerande gates

### Centrala filer
Standardstacken ska minst ha `package.json`, Vite-/TypeScript-konfiguration, app-entrypoint, README, fixture/mockdata och deployment-konfiguration när statisk hosting ingår.

### Dependency och build
När kommandokörning finns ska minst `npm ci` och `npm run build` eller motsvarande köras. Om lockfil saknas får `npm install` användas med warning. Buildfel är blockerande.

Agent Workspace är föredragen extern build provider när tillgänglig, men hostens egen kodexekvering är fullgod fallback.

### Huvudflöden
Varje primärt demonstrationsscenario ska kunna genomföras från start till förväntat slut utan döda länkar eller ouppnåeliga tillstånd.

### Exempeldata
Data ska stödja minst ett komplett scenario, relevanta statusar/avvikelser, vara internkonsekvent och kunna återställas när användaren kan ändra den.

### Statisk hosting
För GitHub Pages ska Vite `base`, routing, statiskt output, deploymentinstruktion/workflow och frånvaro av serverhemligheter bedömas.

## 5. Responsiva gates

Om målplattformen inte avgränsats bedöms:
- mobil 390 × 844,
- tablet 768 × 1024,
- desktop 1440 × 900.

Kontrollera navigation, primära actions, clipping, horisontell scroll, touch/formulär och lämplig mobilrepresentation.

När en publik preview finns och Browser Screenshot är tillgänglig tas normalt bara desktop-screenshot. Tablet/mobil tas vid begäran, responsiv förändring/risk eller uppföljning. Övriga formfaktorer får bedömas genom kod-/layoutgranskning och riktade kontroller.

## 6. Optional tool pipeline

Använd tillgängliga providers utan att göra dem obligatoriska:

- **Agent Workspace:** verifiering/build och temporär buildartefakt.
- **PWA Preview:** publik HTTPS-preview av byggd statisk artefakt.
- **Browser Screenshot:** faktisk rendering av publik URL.

Normal full kedja är Agent Workspace → PWA Preview → Browser Screenshot. Om ett steg saknas eller fallerar ska tidigare verifierad evidens behållas och nästa möjliga fallback användas. Browser Screenshot får inte användas utan nåbar publik URL och PWA Preview får inte användas utan nåbar byggartefakt.

## 7. Accessibility-gate

Granska där relevant semantiska element, labels, tangentbordsåtkomlighet, fokusindikering, heading-struktur, att färg inte är enda informationsbärare, begripliga namn och dialogfokus. Uppenbara hinder i huvudflöden är blockerande.

## 8. UX-granskning

Bedöm minst informationshierarki, navigation, primär handling, kognitiv belastning, feedback, felhantering, konsekvens, responsiv prioritering och demonstrationsbarhet. Klassificera findings som `blocker`, `important` eller `improvement`.

## 9. Preview-gate

När previews levereras ska `preview-manifest.yaml` och faktisk leverans vara konsekventa:
- `design_mockup` får inte beskrivas som faktisk app-rendering,
- `app_screenshot` ska ha känd viewport, source revision och provider-provenance,
- preview/browserfel får vara warning och ska inte ensamt sätta totalresultat till fail,
- temporära resurser ska städas när de inte längre behövs.

## 10. Deterministisk kontra expertbaserad validering

Prioritera deterministiska kontroller för filnärvaro, konfiguration, dependencies, TypeScript/build, statiskt output, manifest och fixtures. Använd expertbedömning för informationshierarki, visuellt fokus, kognitiv belastning, responsiv omprioritering och begriplighet.

## 11. Totalresultat

`pass` kräver att blockerande gates passerar eller legitimt är `not_applicable`, inga UX-blockers återstår, build har verifierats när kodexekvering finns, huvudflöden/exempeldata är verifierade och relevanta formfaktorer bedömts. `pass_with_warning` får användas när endast icke-blockerande preview-/browserproblem eller liknande återstår.

## 12. Begränsad runtime

Om runtime saknar shell/build eller browser:
1. gör alla möjliga statiska/strukturella kontroller,
2. markera det som inte kunde testas,
3. beskriv det aldrig som verifierat,
4. ge exakta kommandon för en kapabel runtime,
5. blockera inte på preview/browser ensam,
6. markera faktisk build som `not_tested` tills evidens finns.

Normal leverans innehåller `validation-report.yaml`, `UX-REVIEW.md` och `preview-manifest.yaml` när previews finns.
