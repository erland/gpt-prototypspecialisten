# Validerings- och kvalitetsgates

Detta kontrakt styr när en genererad prototyp får beskrivas som validerad, demonstrerbar och leveransklar. Valideringen kombinerar deterministiska kontroller där det går med strukturerad UX-bedömning där mänsklig eller modellbaserad bedömning krävs.

## 1. Grundprincip

En prototyp är inte klar enbart för att filer har genererats. Före leverans ska följande bedömas systematiskt:

1. projektstruktur och centrala filer,
2. dependency-installation och build,
3. statisk hosting/deployment,
4. huvudflöden,
5. exempeldata och demonstrationsscenario,
6. mobil, tablet och desktop,
7. tillgänglighet och interaktionsfeedback,
8. UX-kvalitet,
9. preview-spårbarhet där previews ingår,
10. kända begränsningar och eventuella icke-blockerande avvikelser.

Validering ska dokumenteras i `validation-report.yaml` eller motsvarande strukturerad artefakt.

## 2. Resultatnivåer

Varje gate ska få ett av följande resultat:

- `pass` – kravet är uppfyllt,
- `pass_with_warning` – kärnkravet är uppfyllt men en tydlig, icke-blockerande avvikelse finns,
- `fail` – kravet är inte uppfyllt och blockerar färdigställande,
- `not_applicable` – kravet är uttryckligen irrelevant för aktuell prototyp.

`not_tested` får användas under arbete men inte i en slutlig leveransrapport för obligatoriska gates.

## 3. Blockerande gates

Följande är blockerande i normalfallet:

### 3.1 Centrala filer

Minst följande ska finnas för standardstacken eller ha dokumenterad motsvarighet:

- `package.json`,
- Vite-konfiguration,
- TypeScript-konfiguration,
- applikationsentrypoint,
- README,
- fixture/mockdata,
- deployment-konfiguration när statisk hosting ingår.

### 3.2 Dependency och build

När runtime tillåter kommandokörning ska minst följande köras eller motsvarande verifieras:

```bash
npm ci
npm run build
```

Om lockfil saknas får `npm install` användas, men leveransen ska då markera att dependency-resolution inte är fullt låst.

Buildfel är blockerande. Browser-renderingsfel är däremot inte automatiskt blockerande om build och övriga gates passerar.

### 3.3 Huvudflöden

Varje primärt demonstrationsscenario ska kunna genomföras från start till förväntat slut utan döda länkar, saknade actions eller tillstånd som inte kan nås.

För varje huvudflöde ska rapporten ange:

- startläge,
- steg/handlingar,
- förväntat slutläge,
- använda fixtures,
- resultat.

### 3.4 Exempeldata

Exempeldata ska:

- stödja minst ett komplett demonstrationsscenario,
- innehålla relevanta statusar och avvikelser,
- vara internkonsekvent,
- kunna återställas till känt startläge när användaren kan ändra data,
- inte kräva manuell preparering inför demo.

### 3.5 Statisk hosting

När GitHub Pages är referensmål ska minst följande bedömas:

- Vite `base` fungerar från repo-subpath,
- routing ger inte kända 404-problem vid normal navigation,
- buildoutput är statiskt,
- workflow eller deploymentinstruktion finns,
- inga serverhemligheter krävs för kärnflödena.

## 4. Responsiva gates

Om användaren inte avgränsat målplattformen ska varje huvudvy bedömas för:

- mobil: 390 × 844,
- tablet: 768 × 1024,
- desktop: 1440 × 900.

För varje viewport ska minst detta kontrolleras:

- central navigation är användbar,
- primära actions är synliga/nåbara,
- kritiskt innehåll klipps inte bort,
- oavsiktlig horisontell scroll saknas,
- formulär och touch-targets är praktiskt användbara,
- informationsrika desktopmönster har lämplig mobilrepresentation.

Om verklig browser-rendering är tillgänglig ska dessa kontroller helst baseras på den aktuella appen. Om Chromium/Playwright saknas får kod-/layoutgranskning och tydligt märkt designmockup användas som fallback. Fallback ska markeras i rapporten men blockerar inte i sig leveransen.

## 5. Accessibility-gate

På prototypnivå ska följande minst granskas där relevant:

- semantiska element,
- formulärlabels,
- tangentbordsåtkomlighet,
- fokusindikering,
- begriplig heading-struktur,
- färg är inte enda informationsbärare,
- knappar/länkar har begripliga namn,
- dialoger skapar inte uppenbar fokusfälla.

Uppenbara hinder i huvudflöden är blockerande. Mindre förbättringar kan dokumenteras som warnings.

## 6. UX-granskning

UX-granskningen är modell-/expertbaserad och ska vara strukturerad, inte en generell kommentar om att gränssnittet "ser bra ut".

Bedöm minst:

- informationshierarki,
- navigation och orienterbarhet,
- tydlighet i primär handling,
- kognitiv belastning,
- feedback efter handlingar,
- fel- och valideringshantering,
- konsekvens mellan vyer,
- responsiv prioritering,
- demonstrationsbarhet med medföljande data.

Varje identifierat problem ska klassas som:

- `blocker`,
- `important`,
- `improvement`.

`blocker` måste åtgärdas innan färdigställande. `important` ska normalt åtgärdas om det ryms inom prototypens scope; annars dokumenteras det tydligt. `improvement` får lämnas till senare iteration.

## 7. Preview-gate

När previews levereras ska `preview-manifest.yaml` och faktisk leverans vara konsekventa.

- `design_mockup` får inte beskrivas som faktisk app-rendering.
- `app_screenshot` ska ha känd viewport och spårbar arbetsversion.
- Browserfel får rapporteras som warning/fallback och ska inte i sig sätta totalresultat till fail.

## 8. Deterministisk kontra modellbaserad validering

Prioritera deterministiska kontroller för:

- filnärvaro,
- konfigurationsvärden,
- dependency-installation,
- TypeScript/build,
- statiskt output,
- manifeststruktur,
- dokumenterade fixtures och resetfunktioner.

Använd modell-/expertbedömning för:

- informationshierarki,
- visuellt fokus,
- kognitiv belastning,
- responsiv omprioritering,
- begriplighet och demonstrationskvalitet.

Rapporten ska skilja på `deterministic` och `expert_review` så att evidensnivån är tydlig.

## 9. Totalresultat

En leverans får markeras `pass` när:

- alla blockerande gates är `pass` eller legitimt `not_applicable`,
- inga UX-`blocker` återstår,
- build är godkänd när kodexekvering är tillgänglig,
- huvudflöden och exempeldata är verifierade,
- tre formfaktorer är bedömda när de ingår i målplattformen,
- kända warnings dokumenteras.

`pass_with_warning` får användas om endast icke-blockerande problem återstår, till exempel att verklig browser-screenshot inte kunde tas trots fungerande build.

## 10. Fallback när runtime är begränsad

Om aktuell runtime inte kan köra shell/build eller browser:

1. gör alla möjliga statiska och strukturella kontroller,
2. markera vilka kontroller som inte kunde köras,
3. försök inte beskriva dem som verifierade,
4. ge exakta kommandon som kan köras i en runtime med kodexekvering,
5. blockera inte på browser-rendering ensam,
6. markera däremot faktisk build som `not_tested` tills den verifierats; en slutlig "build validated"-claim får inte göras utan evidens.

## 11. Valideringsartefakter

Normal leverans ska innehålla:

- `validation-report.yaml` – maskinläsbar gate-status och evidens,
- `UX-REVIEW.md` – kort human-readable UX-bedömning,
- `preview-manifest.yaml` när previews finns.

Valideringsrapporten ska följa mallen i `templates/validation/validation-report.yaml`.
