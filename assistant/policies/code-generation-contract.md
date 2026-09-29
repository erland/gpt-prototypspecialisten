# Kodgenereringskontrakt

Detta kontrakt styr hur Prototypspecialisten genererar en körbar frontendprototyp efter att UX-/prototypspecifikationen har passerat sina gates. Målet är en liten, begriplig och trovärdig kodbas som kan köras lokalt och deployas statiskt utan backend.

## 1. Standardstack

Om användaren inte uttryckligen behöver något annat ska prototypen använda:

- React,
- TypeScript,
- Vite,
- vanlig CSS, CSS Modules eller annan lättviktig stylinglösning som fungerar helt statiskt,
- statiska assets,
- lokal mockdata och simulerade tjänster.

Undvik beroenden som kräver server, databas, hemligheter eller externa API-nycklar. Lägg bara till större UI-ramverk eller state-bibliotek när prototypens komplexitet faktiskt motiverar det.

### Gate

Standardstacken är godkänd när `npm install`/`npm ci` och `npm run build` kan ge en statisk frontendbundle utan backendkrav.

## 2. Projektstruktur

Generera normalt en struktur i denna riktning:

```text
prototype/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   ├── data/
│   │   └── fixtures.ts
│   ├── services/
│   │   └── mock-api.ts
│   ├── state/
│   │   └── storage.ts
│   ├── types/
│   ├── App.tsx
│   └── main.tsx
├── .github/workflows/deploy-pages.yml
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

Strukturen får förenklas för små prototyper. Skapa inte tomma kataloger eller abstraktioner utan verklig användning.

## 3. Exempeldata

Exempeldata ska härledas från `sample_data_plan` och vara deterministisk som standard.

Krav:

- data ska stödja minst ett komplett demonstrationsscenario,
- relevanta statusar och avvikande tillstånd ska finnas,
- data ska ha begripliga och domännära namn i stället för generiska `Item 1`, `Item 2`,
- datum, roller och relationer ska vara internt konsekventa,
- slumpdata får bara användas när variationen är en del av demonstrationen och får inte göra tester/demos instabila.

Fixtures ska normalt ligga i TypeScript eller JSON och kunna återställas till ett känt startläge.

## 4. Simulerad API-/tjänstelager

Komponenter ska normalt inte importera och mutera fixture-data direkt. Lägg ett tunt mock-service-lager mellan UI och data när prototypen har mer än trivial interaktion.

Mock-service får simulera:

- läsning,
- sökning,
- filtrering och sortering,
- skapande och uppdatering,
- statusändringar,
- borttagning,
- laddningsfördröjning,
- definierade fel- och varningstillstånd.

Föredra deterministiska felvägar, exempelvis särskilda fixtures eller explicit "simulera fel"-läge, framför slumpmässiga 10-procentsfel.

## 5. Persistens

Persistens ska väljas utifrån demonstrationsbehovet:

- `memory` för korta, helt återställbara demos,
- `localStorage` när användarens ändringar bör finnas kvar efter omladdning,
- `sessionStorage` när persistens bara ska gälla aktuell flik/session.

Standard för interaktiva CRUD-prototyper är `localStorage` med:

- namespacade nycklar,
- versionsfält för lagrad struktur när det behövs,
- säker JSON-parsning,
- fallback till fixtures vid saknad eller korrupt data,
- tydlig `reset demo data`-funktion när återställning är värdefull.

Lagra inte hemligheter eller känsliga riktiga data i browser storage.

## 6. Routing och GitHub Pages

Prototypen ska fungera som statisk webbapp. För routing ska implementationen väljas så att direktnavigation på GitHub Pages inte ger 404.

Tillåtna standardstrategier:

1. hash-baserad routing, eller
2. SPA-fallback som uttryckligen konfigureras och verifieras för valt hostingmål.

Om GitHub Pages är referensmål ska Vites `base` hanteras korrekt för projekt-repo. Undvik hårdkodade root-paths som bara fungerar på `localhost`.

## 7. Responsiv implementation

Implementationen ska realisera `responsive_strategy`, inte bara lägga till generella media queries.

Minimikrav:

- central navigation fungerar på 390, 768 och 1440 px om målplattformen inte avgränsats,
- primära actions är nåbara i alla relevanta viewports,
- tät desktopinformation får lämplig mobilrepresentation,
- inga centrala flöden kräver hover,
- formulär och touch-targets är praktiskt användbara,
- oavsiktlig horisontell scroll undviks.

När en tabell inte fungerar på mobil ska den exempelvis kunna bli kort, prioriterad kolumnlista eller drill-down i stället för en komprimerad oläslig tabell.

## 8. Tillstånd och feedback

Huvudflöden ska innehålla trovärdiga tillstånd där de är relevanta:

- initialt läge,
- loading,
- tomt läge,
- lyckad handling,
- valideringsfel,
- servicefel,
- bekräftelse före destruktiv handling,
- sparad/ändrad status.

Tillstånd ska vara demonstrerbara med medföljande data och inte bara finnas som död kod.

## 9. Tillgänglighet och grundläggande UX-kodkvalitet

Prototypnivå betyder inte att grundläggande användbarhet får hoppas över.

Krav där relevanta:

- semantiska HTML-element,
- labels kopplade till formulärfält,
- tangentbordsåtkomliga interaktioner,
- fokusindikering,
- begripliga knapp- och länktexter,
- färg får inte vara enda informationsbäraren,
- rimlig heading-struktur,
- modaler/dialoger får inte skapa uppenbara fokusfällor.

## 10. Statisk deployment

En färdig normalprototyp ska kunna deployas med en statisk buildkatalog, normalt `dist/`.

GitHub Pages-konfiguration ska normalt innehålla ett workflow som:

1. checkar ut repot,
2. installerar Node,
3. installerar dependencies deterministiskt,
4. kör build,
5. laddar upp Pages-artifact,
6. deployar till Pages.

Workflowet får inte kräva applikationshemligheter för en ren frontendprototyp.

## 11. README-krav

Varje levererad prototyp ska ha en README som minst beskriver:

- prototypens syfte och avgränsning,
- vad som simuleras,
- viktigaste demonstrationsscenario,
- hur man kör lokalt,
- hur man bygger,
- hur data återställs om persistens används,
- vilka referensviewports som stöds,
- hur GitHub Pages/deployment fungerar,
- kända prototypbegränsningar,
- skillnaden mellan prototypfunktion och verklig produktion/integration där detta annars kan misstolkas.

## 12. Ingen falsk backend

UI:t får simulera serverbeteende men leveransen ska tydligt säga att detta är simulering. Implementera inte pseudokod som ser ut att anropa en verklig tjänst om ingen sådan tjänst finns.

Externa nätverksanrop ska vara borttagna eller uttryckligen valfria för normal demo. Prototypens kärnflöden ska fungera offline efter dependency-installation/build när användningsfallet tillåter det.

## 13. Kodgenereringsgate

Kodgenereringskontraktet är uppfyllt när:

- standardstacken eller dokumenterad avvikelse är tydlig,
- fixture-data stödjer huvudscenariot,
- interaktiv data går genom ett begripligt service-/state-lager där det behövs,
- persistensstrategin är explicit,
- responsiv strategi är implementerbar för alla relevanta viewports,
- statisk routing/base-path är kompatibel med hostingmålet,
- GitHub Pages eller motsvarande statisk deployment är definierad,
- README-kraven är definierade,
- prototypen kräver ingen verklig backend för kärnflödena.
