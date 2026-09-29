# Utvecklingsplan – Prototypspecialisten

## Projektprofil

- **Profil:** `zip_first_advanced`
- **Modellrobusthet:** `stateful`
- **Canonical princip:** ett gemensamt beteendekontrakt, runtime-adapters senare

## Steg 1 – Canonical projektgrund

**Mål:** skapa GPT-projektets canonical struktur och styrande kontrakt.

**Klart när:**
- `gpt-project.yaml` finns,
- canonical instruktion finns,
- capability- och artifact-kontrakt är definierade,
- workspace/state-modell finns,
- runtime-kandidater är dokumenterade,
- projektstatus finns,
- modellrobusthetsgates passerar,
- projekt-ZIP kan byggas.

## Steg 2 – UX- och prototypworkflow

**Mål:** operationalisera flödet från behov till prototypspecifikation.

**Klart när:** behovsanalys, scope, informationsarkitektur, användarflöden, exempeldata och responsiv strategi har tydliga outputs och gates.

## Steg 3 – Förhandsvisningskontrakt

**Mål:** definiera tidiga mockups och valfri verklig browser-rendering.

**Klart när:** mobil/tablet/desktop, mockupmärkning, screenshot-kontrakt, preview-manifest och fallback utan Chromium/Playwright är explicita och täcks av evalfall.

## Steg 4 – Kodgenereringskontrakt

**Mål:** definiera hur körbara React/Vite-prototyper genereras.

**Klart när:** standardstack, mockdata, simulerad API-/persistensstrategi, statisk deployment och README-krav finns.

## Steg 5 – Validering och kvalitetsgates

**Mål:** definiera deterministiska och modellbaserade kontroller.

**Klart när:** build, centrala filer, hosting, huvudflöden, tre formfaktorer, exempeldata och UX-granskning kan bedömas systematiskt.

## Steg 6 – ChatGPT Chat-distribution

**Mål:** skapa validerad Chat ZIP-runtime från canonical källor.

## Steg 7 – Custom GPT-distribution

**Mål:** skapa Custom GPT-kompatibel distribution utan att flytta kritiskt beteende till Knowledge.

## Steg 8 – OpenCode-distribution

**Mål:** skapa kodcentrerad runtime för faktisk implementation, build och validering.

## Steg 9 – Evals och modellrobusthet

**Mål:** utöka evals för idé, skärmdump, URL, responsiv översättning, formulär/fel, browser-fallback och återupptagning.

## Steg 10 – Runtime parity, hygiene och RC

**Mål:** verifiera aktiverade runtimes, hygiene, distributionsvalidering och release readiness.

## Release candidate

Steg 10 slutför planen. När parity-, distributions-, hygiene- och RC-gates passerar byggs `0.1.0-rc.1` för ChatGPT Chat, Custom GPT och OpenCode från samma canonicala projekt-snapshot.

## Steg 11 – Korrigering: GitHub CI, Release och readiness

**Bakgrund:** Efter RC.1 upptäcktes att GitHub Actions-standardkraven från GPT Byggaren inte hade applicerats. RC.1 betraktas därför inte som slutligt godkänd release candidate.

**Mål:** göra projektet fullt GitHub-redo enligt GPT Byggarens canonical policy.

**Klart när:**
- `.github/workflows/ci.yml` kör push, pull request och manuell dispatch,
- `.github/workflows/release.yml` triggas av publicerad GitHub Release och härleder version från release-taggen,
- CI och release bygger samtliga aktiverade targets från `build_system.targets`,
- regressionstester finns och körs med pytest,
- checksummor och delivery manifest skapas och verifieras,
- samma release-readinessmodell används lokalt/CI/release,
- slutlig lint, test, modellrobusthet, eval coverage, hygiene, build, distributionsvalidering och runtime parity passerar,
- en ny RC `0.1.0-rc.2` byggs från den korrigerade snapshoten.

## Release candidate efter korrigering

`0.1.0-rc.2` ersätter `0.1.0-rc.1` som aktuell release candidate.
