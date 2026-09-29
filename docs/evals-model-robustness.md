# Evals och modellrobusthet

## Syfte

Evalpaketet verifierar att Prototypspecialistens kärnbeteende förblir stabilt över modeller och aktiverade runtimes. Fokus ligger på beteenden som annars lätt degraderas till generisk kodgenerering eller visuella påståenden utan evidens.

## Obligatorisk scenariotäckning

Följande områden måste finnas i evalpaketet:

- idé som enda input,
- skärmdump som inspirationskälla,
- URL som inspirationskälla med fallback utan webbtillgång,
- responsiv översättning mellan desktop och mobil,
- formulär och deterministiska fel-/valideringstillstånd,
- browser-fallback när Chromium/Playwright saknas,
- återupptagning från `project-status.yaml`,
- valideringsgate som hindrar falsk completion,
- runtime parity mellan Chat, Custom GPT och OpenCode.

## Deterministisk coverage-gate

Kör:

```bash
python scripts/validate_eval_coverage.py --project-root .
```

Kontrollen verifierar unika eval-id:n, obligatoriska kategorier, komplett model-compatibility-svit och att specialiserade sviter för workflow, preview, codegen, validation och distribution finns kvar.

## Modellrobusthetsprinciper

1. Samma canonical instruktion är auktoritativ för alla runtimes.
2. Separata modellinstruktioner är inte tillåtna.
3. Kärnregler får inte kräva fler än ett policyhopp från canonical instruktion.
4. Deterministisk validering föredras framför självvärdering.
5. Browser-rendering är valfri evidens och aldrig ett krav för kärnleveransen.
6. Mockup och faktisk app-screenshot måste alltid kunna särskiljas.
7. Exempeldata och tre formfaktorer är normalbeteende, inte opt-in.
