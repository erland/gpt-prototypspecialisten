# Prototypspecialisten

Canonical GPT-projekt för en UX-fokuserad prototypbyggare som skapar körbara, responsiva webbprototyper med realistisk exempeldata.

## Aktuell status

Steg 1–10 i utvecklingsplanen är implementerade. Projektet har canonical instruktion, explicit stateful workflow, UX-/preview-/kodgenererings-/valideringskontrakt samt validerade ChatGPT Chat-, Custom GPT- och OpenCode-distributioner. Projektet är förberett som release candidate `0.1.0-rc.2`.

## Validering

```bash
python scripts/lint_gpt_project.py --project-root .
python scripts/validate_model_robustness.py --project-root .
python scripts/validate_eval_coverage.py --project-root .
python scripts/project_hygiene.py --project-root . --mode checkpoint
python scripts/validate_distributions.py --project-root .
python scripts/validate_runtime_parity.py --project-root .
```

## Bygga RC-paketen

```bash
python scripts/build_distributions.py \
  --project-root . \
  --version 0.1.0-rc.2 \
  --targets project,chat,custom_gpt,opencode
```

Genererade runtimepaket finns i `dist/`. Chat-distributionen kan bifogas i en ChatGPT-konversation. Custom GPT-distributionen innehåller Builder-underlag med instruktion, starters, capability-rekommendationer och runtime-kontrakt.

## UX- och prototypworkflow

Workflowet definierar explicita outputs och gates för behov, scope, informationsarkitektur, huvudflöden, obligatorisk exempeldata och responsiv strategi. Se `assistant/policies/ux-prototype-workflow.md`.

## Förhandsvisningskontrakt

Tydlig separation finns mellan designmockup, faktisk app-screenshot och code preview. Agent Workspace via MCP är föredragen valfri runtime när den finns och används automatiskt för faktisk verifiering. Screenshot-strategin är desktop-first: normalt tas bara 1440×900, medan tablet/mobil fångas vid behov. Responsiv design bedöms fortfarande för 390×844, 768×1024 och 1440×900. Browser-runtime är uttryckligen icke-blockerande. Se `assistant/policies/preview-contract.md`.

## Kodgenereringskontrakt

React + TypeScript + Vite är standardstack med deterministiska fixtures, tunt mock-service-lager, browserpersistens, responsiv implementation och GitHub Pages-kompatibel statisk deployment. Se `assistant/policies/code-generation-contract.md`.

## Valideringskontrakt

Build, hosting, huvudflöden, exempeldata, tre formfaktorer, accessibility och UX-review bedöms systematiskt. Se `assistant/policies/validation-quality-gates.md`.

## ChatGPT Chat-runtime

Steg 6 aktiverar och validerar en Chat ZIP från canonical källor. Se `docs/chat-runtime.md`.

## Custom GPT-runtime

Steg 7 aktiverar och validerar Builder-paketet utan att flytta kritiskt beteende till Knowledge. Se `docs/custom-gpt-runtime.md`.


## OpenCode

OpenCode-distributionen genereras från samma canonical instruktion och är workspace-first för faktisk implementation, build och validering.
## OpenCode-distribution

OpenCode-paketet är avsett att läggas i en repository/workspace där prototypen ska byggas. Det använder samma canonical beteende som Chat och Custom GPT men kan utnyttja runtimeens filredigering och shell för faktisk implementation och deterministisk validering.


## Evals och modellrobusthet

Evalpaketet täcker idé, skärmdump, URL, responsiv översättning, formulär/fel, browser-fallback, återupptagning och runtime parity. Coverage-gaten körs med `scripts/validate_eval_coverage.py`. Se `docs/evals-model-robustness.md`.


## Runtime parity och RC

Slutlig parity-gate jämför canonicala kontrakt mellan Chat, Custom GPT och OpenCode. RC-readiness kräver att alla plansteg är klara, att inga varningar eller blockerare finns kvar och att slutlig hygiene passerar. Se `docs/runtime-parity-rc.md`.

## GitHub Actions och release

Projektet är GitHub-redo enligt GPT Byggarens standard. CI finns i `.github/workflows/ci.yml` och körs vid push, pull request och manuell dispatch. Den bygger automatiskt alla targets i `build_system.targets` med den reserverade CI-versionen `0.0.0-ci`.

GitHub Release-byggning finns i `.github/workflows/release.yml`. När en release publiceras härleds versionsnumret från release-taggen och projekt-ZIP, Chat ZIP, Custom GPT ZIP och OpenCode ZIP byggs, valideras och bifogas tillsammans med `SHA256SUMS.txt` och `DELIVERY-MANIFEST.json`.

Se `docs/github-automation.md` för detaljer.
