# Förhandsvisningskontrakt

Detta kontrakt styr hur Prototypspecialisten planerar, skapar, märker och validerar visuella förhandsvisningar. Målet är att ge användaren snabb visuell återkoppling utan att blanda ihop designmockups med faktisk rendering av den körbara prototypen.

## 1. Förhandsvisningstyper

Endast följande typer får användas:

### `design_mockup`

En genererad eller manuellt komponerad visuell designförhandsvisning. Den visar avsedd struktur, hierarki, navigation och visuellt uttryck, men är **inte bevis** på hur den körbara appen faktiskt renderar.

Måste märkas tydligt som exempelvis **Designmockup** eller **Genererad mockup**.

### `app_screenshot`

En bild fångad från den faktiskt körande prototypen i en browser/renderingsmotor. Den får endast beskrivas som faktisk screenshot när den kommer från den byggda appen.

Måste ha spårbar information om viewport och källa.

### `code_preview`

En enklare strukturell förhandsvisning baserad på den genererade implementationen när varken bildgenerering eller browser-rendering är tillgänglig. Den kan exempelvis vara en beskrivning av layout och komponenter. Den får aldrig beskrivas som screenshot.

## 2. Standardviewports

Om användaren inte anger annat ska förhandsvisningar och responsivitetskontroll utgå från:

- `mobile`: 390 × 844 px
- `tablet`: 768 × 1024 px
- `desktop`: 1440 × 900 px

Bredden är kontraktsbärande. Höjden får justeras om innehållet kräver helsidesfångst eller runtime har andra begränsningar.

Om en målplattform uttryckligen avgränsas får övriga viewports utelämnas, men detta ska dokumenteras i preview-manifestet.

## 3. Tidig mockup

Tidig mockup används före eller under implementation när visuell återkoppling sannolikt minskar risken att bygga fel lösning.

Mockupen ska härledas från samma prototypspecifikation som implementationen och visa minst:

- huvudsaklig informationshierarki,
- navigation,
- primär handling,
- centrala dataobjekt,
- responsiv omprioritering för relevanta viewports.

För en normal flerplattformslösning bör användaren kunna bedöma mobil, tablet och desktop. Det är tillåtet att visa dem som separata bilder eller i en samlad jämförelse, så länge varje viewport går att identifiera.

## 4. Faktisk browser-rendering

Browser-rendering är en förbättring, inte ett kärnberoende.

För att en bild ska klassificeras som `app_screenshot` ska följande vara sant:

1. prototypen har byggts eller startats från den aktuella källkoden,
2. sidan har laddats i en verklig browser eller kompatibel renderingsmotor,
3. viewport är känd,
4. screenshoten kommer från den sidan,
5. källrevision eller motsvarande arbetsversion går att identifiera i projektets preview-manifest.

Om dessa villkor inte kan styrkas ska bilden klassificeras som `design_mockup` eller `code_preview`.

## 5. Playwright/Chromium

Playwright, Chromium eller motsvarande får användas när runtime stödjer det, men får aldrig vara ett krav för att färdigställa prototypen.

Browser-rendering får som mest blockera statusen för **faktisk screenshot**, inte:

- UX-specifikation,
- kodgenerering,
- frontend-build,
- exempeldata,
- statisk deployment,
- projektleverans.

Förväntad felhantering:

1. registrera renderingsförsöket som misslyckat,
2. behåll deterministisk build-validering som primär teknisk gate,
3. använd tydligt märkt designmockup om bildgenerering finns,
4. annars använd code preview och beskriv vad som inte kunde visuellt verifieras,
5. fortsätt leveransen om övriga kvalitetsgates passerar.

Försök inte installera systempaket eller kringgå runtime-sandbox om detta inte uttryckligen stöds av miljön och behövs för användarens mål.

## 6. Märkning i chatten och leveransen

Varje visuell förhandsvisning ska kunna besvaras med frågan: **är detta vad appen faktiskt renderade, eller en designbild?**

Använd följande språk konsekvent:

- `design_mockup`: "Designmockup – inte faktisk app-rendering"
- `app_screenshot`: "Screenshot från körbar prototyp"
- `code_preview`: "Strukturell kodförhandsvisning – ingen browser-screenshot"

Blanda inte flera typer utan separata etiketter.

## 7. Preview-manifest

När prototypprojektet innehåller eller levererar förhandsvisningar ska ett maskinläsbart `preview-manifest.yaml` kunna skapas med följande information per preview:

- `id`
- `type`: `design_mockup`, `app_screenshot` eller `code_preview`
- `viewport`
- `source`
- `source_revision`
- `status`
- `notes`

För browser-rendering ska även browser/renderingsmotor anges när den är känd.

## 8. Responsiv jämförelse

Minst en central vy ska normalt kunna bedömas i alla tre referensbredder före slutleverans.

Bedömningen ska kontrollera att:

- navigationen är användbar,
- primära handlingar fortfarande är synliga eller lätt åtkomliga,
- tät information får lämplig mobilrepresentation,
- ingen central funktion kräver hover-only-beteende,
- text och kontroller inte kapas,
- oavsiktlig horisontell scroll undviks.

Om faktisk browser-rendering saknas ska dessa punkter valideras mot responsiv strategi och implementation, och den visuella osäkerheten ska framgå.

## 9. Gate för Steg 3

Förhandsvisningskontraktet är operationaliserat när:

- de tre preview-typerna är definierade,
- standardviewports är explicita,
- faktisk screenshot kräver verifierbar app-rendering,
- mockupmärkning är obligatorisk,
- Playwright/Chromium-fel har icke-blockerande fallback,
- preview-manifest har en mall,
- evalfall täcker felmärkning, viewportkrav och browser-fallback.
