# Prototypspecialisten

Canonical GPT-projekt för en UX-fokuserad prototypbyggare som skapar körbara, responsiva webbprototyper med realistisk exempeldata.

## Aktuell status

Steg 1–12 i utvecklingsplanen är implementerade. Projektet har canonical instruktion, explicit stateful workflow, UX-/preview-/kodgenererings-/valideringskontrakt samt ChatGPT Chat-, Custom GPT-, OpenCode- och OpenAI Plugin-distributioner. Projektet är förberett som release candidate `0.1.0-rc.3`.

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
  --version 0.1.0-rc.3 \
  --targets project,chat,custom_gpt,opencode,plugin
```

Genererade runtimepaket finns i `dist/`. Chat-distributionen kan bifogas i en ChatGPT-konversation. Custom GPT-distributionen innehåller Builder-underlag med instruktion, starters, capability-rekommendationer och runtime-kontrakt.

## UX- och prototypworkflow

Workflowet definierar explicita outputs och gates för behov, scope, informationsarkitektur, huvudflöden, obligatorisk exempeldata och responsiv strategi. Se `assistant/policies/ux-prototype-workflow.md`.

## Förhandsvisningskontrakt

Previewverktygen används som **progressive enhancement**. Agent Workspace ansvarar primärt för build/verifiering och temporär artefakt, PWA Preview för temporär publik HTTPS-hosting och Browser Screenshot för faktisk browser-rendering. När alla tre finns är normal kedja **Agent Workspace → PWA Preview → Browser Screenshot**. Partiella kombinationer används när deras verkliga in-/utdata går att koppla ihop, och projektet ska fungera utan någon av dem.

Screenshot-strategin är desktop-first: normalt tas 1440×900, medan tablet/mobil fångas vid behov. Responsiv design bedöms fortfarande för 390×844, 768×1024 och 1440×900. Build, preview och browser-verifiering hålls som separata evidensnivåer. Se `assistant/policies/preview-contract.md`.

## Kodgenereringskontrakt

React + TypeScript + Vite är standardstack med deterministiska fixtures, tunt mock-service-lager, browserpersistens, responsiv implementation och GitHub Pages-kompatibel statisk deployment. Se `assistant/policies/code-generation-contract.md`.

## Valideringskontrakt

Build, hosting, huvudflöden, exempeldata, tre formfaktorer, accessibility och UX-review bedöms systematiskt. Optional preview-/browserfel får inte radera tidigare verifierad build. Se `assistant/policies/validation-quality-gates.md`.

## ChatGPT Chat-runtime

Steg 6 aktiverar och validerar en Chat ZIP från canonical källor. Se `docs/chat-runtime.md`.

## Custom GPT-runtime

Steg 7 aktiverar och validerar Builder-paketet utan att flytta kritiskt beteende till Knowledge. Installerade prototypplugins används som optional capability providers. Se `docs/custom-gpt-runtime.md`.

## OpenCode-distribution

OpenCode-paketet är workspace-first för faktisk implementation, build och validering och använder samma canonical beteende som Chat och Custom GPT.

## OpenAI Plugin

OpenAI Plugin är en skills-first peer distribution med `equivalent_runtime_dependent` parity. Full canonical prototypimplementation kräver att hosten erbjuder writable filesystem, persistent workspace och code execution. Agent Workspace, PWA Preview och Browser Screenshot är valfria förstärkningar och får inte bli kärnberoenden.

## Evals och modellrobusthet

Evalpaketet täcker idé, skärmdump, URL, responsiv översättning, formulär/fel, browser-fallback, pluginfrånvaro, partiella capability-kombinationer, failure isolation, cleanup, återupptagning och runtime parity. Coverage-gaten körs med `scripts/validate_eval_coverage.py`.

## Runtime parity och RC

Slutlig parity-gate jämför canonicala kontrakt mellan Chat, Custom GPT, OpenCode och OpenAI Plugin. RC-readiness kräver att alla plansteg är klara, att inga varningar eller blockerare finns kvar och att slutlig hygiene passerar.

## GitHub Actions och release

CI finns i `.github/workflows/ci.yml` och körs vid push, pull request och manuell dispatch. GitHub Release-byggning finns i `.github/workflows/release.yml`; release-taggen används som version och distributionspaket plus checksummor bifogas.
