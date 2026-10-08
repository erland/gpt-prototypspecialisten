# Förhandsvisningskontrakt

Detta kontrakt styr hur Prototypspecialisten planerar, skapar, märker och validerar visuella förhandsvisningar. Externa verktyg är **progressive enhancement**: de ska användas när relevanta kapabiliteter finns men får aldrig vara ett kärnberoende.

## 1. Förhandsvisningstyper

### `design_mockup`
Genererad eller manuellt komponerad designbild. Den visar avsedd struktur och visuellt uttryck men är inte bevis på faktisk rendering. Märk som **Designmockup – inte faktisk app-rendering**.

### `app_screenshot`
Bild fångad från den faktiskt körande prototypen i browser/renderingsmotor. Kräver känd viewport och spårbar källa/arbetsversion. Märk som **Screenshot från körbar prototyp**.

### `code_preview`
Strukturell förhandsvisning baserad på implementationen när browser-rendering saknas. Märk som **Strukturell kodförhandsvisning – ingen browser-screenshot**.

## 2. Standardviewports

Responsiv bedömning använder normalt:
- `mobile`: 390 × 844 px
- `tablet`: 768 × 1024 px
- `desktop`: 1440 × 900 px

Screenshot-strategin är desktop-first. Ta normalt en faktisk desktop-screenshot per relevant iteration. Tablet/mobil tas endast på uttrycklig begäran, vid responsiv ändring/risk eller för uppföljning. Responsiv kvalitet ska ändå bedömas för alla relevanta formfaktorer.

## 3. Kapabilitetsbaserad preview-pipeline

Välj efter tillgänglig kapabilitet, inte efter krav på en specifik plugin.

### Build provider
Använd för deterministisk verifiering och build.
- föredragen extern provider: **Agent Workspace**
- fallback: hostens egna filesystem/code execution/shell

Agent Workspace används primärt för workspace, projektverifiering/build och temporär buildartefakt. Det ska inte antas starta webappen eller ta screenshots.

### Preview provider
Använd för temporär publik HTTPS-hosting av en redan byggd statisk artefakt.
- föredragen extern provider: **PWA Preview**
- alternativ: redan existerande publik deployment/preview

PWA Preview ska bara användas när dess input faktiskt kan tillhandahållas, normalt en HTTPS-nåbar ZIP/tar.gz med byggd statisk app.

### Rendering provider
Använd för faktisk browser-rendering.
- föredragen extern provider: **Browser Screenshot**
- alternativ: annan verklig browser-runtime

Browser Screenshot kräver en publik HTTP(S)-URL. Det får inte anropas mot en lokal eller intern workspace-URL som tjänsten inte kan nå.

## 4. Normal kedja när alla tre finns

1. verifiera/build prototypen i Agent Workspace,
2. skapa/hämta temporär HTTPS-länk till buildartefakten,
3. skapa temporär PWA Preview från artefakten,
4. rendera preview-URL:en med Browser Screenshot,
5. ta normalt en desktop-screenshot,
6. gör UX-/responsiv bedömning,
7. radera preview när den inte längre ska delas,
8. förstör alltid temporärt Agent Workspace.

Om användaren vill prova previewn själv får previewn leva kvar enligt tjänstens TTL; workspacet ska ändå förstöras när dess artefakt inte längre behövs.

## 5. Partiella kombinationer

- **Agent Workspace + PWA Preview:** build/verifiering + körbar preview; screenshot är valfri/otestad.
- **Agent Workspace + Browser Screenshot:** build kan verifieras, men screenshot kräver separat publik URL. Hitta inte på en direktkoppling.
- **PWA Preview + Browser Screenshot:** använd när en byggd artefakt redan kan exponeras via HTTPS.
- **endast Agent Workspace:** verifiera/build och leverera artefakt; preview/browser kan vara `not_tested`.
- **endast PWA Preview:** använd bara om lämplig byggartefakt-URL redan finns.
- **endast Browser Screenshot:** använd mot befintlig publik prototyp-URL.
- **inga externa verktyg:** fortsätt kärnflödet och använd hostens validering samt designmockup/code preview.

Ett saknat eller misslyckat steg ska inte automatiskt göra andra steg ogiltiga.

## 6. Krav för `app_screenshot`

För att en bild ska klassificeras som `app_screenshot` ska:
1. aktuell källversion ha byggts/startats,
2. den publika sidan ha laddats i verklig browser/renderingsmotor,
3. viewport vara känd,
4. screenshoten komma från den sidan,
5. source revision och providers kunna identifieras.

Annars används `design_mockup` eller `code_preview`.

## 7. Evidens och provenance

Preview-manifestet ska kunna ange:
- `build_provider`
- `preview_provider`
- `renderer`
- publik `url` när sådan finns
- `source_revision`
- viewport
- status och notes

Rapportera separat:
- `build_verified`
- `preview_deployed`
- `browser_verified`

Ingen av dessa får härledas enbart från en annan.

## 8. Felhantering

Browser-/previewfel är i normalfallet icke-blockerande om build och huvudflöden i övrigt passerar.

Vid fel:
1. registrera vilket steg som misslyckades,
2. behåll tidigare verifierad evidens,
3. fortsätt med nästa möjliga fallback,
4. påstå inte att utebliven kontroll har passerat,
5. installera inte systempaket eller kringgå sandbox om det inte uttryckligen stöds.

## 9. Responsiv jämförelse

Minst en central vy ska normalt bedömas för mobil, tablet och desktop. Tre screenshots krävs inte. Kod-/layoutgranskning, responsiv strategi och riktade browserkontroller får kombineras.

Kontrollera minst navigation, primära actions, informationsdensitet, touch, avsaknad av hover-only för centrala funktioner, text/controls som inte kapas och undvikande av oavsiktlig horisontell scroll.
