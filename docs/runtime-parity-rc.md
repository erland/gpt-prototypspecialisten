# Runtime parity och release candidate

## Syfte

Slutsteget verifierar att alla aktiva distributioner fortfarande representerar samma canonicala GPT-beteende och att projektet kan paketeras som en release candidate utan kvarvarande plansteg eller hygieneproblem.

## Runtime parity

Aktiva runtimes är ChatGPT Chat, Custom GPT och OpenCode. Parity-gaten verifierar att deras genererade runtime-kontrakt har samma canonicala projektion för:

- capabilities,
- artifacts,
- workspace/state,
- tools.

Runtime-specifika adapterfält får skilja sig. Kärnmarkörerna i canonical instruktion måste däremot finnas kvar i varje kompilerad runtime-instruktion.

Kör:

```bash
python scripts/validate_runtime_parity.py --project-root .
```

## RC-gate

En release candidate får bara skapas när:

- alla tio plansteg är klara,
- inga blockerare eller varningar återstår,
- senaste validering är `pass`,
- slutlig project hygiene är `pass`,
- `next_step` är tom,
- distributionsbygget har ett explicit `-rc.N`-versionsnummer,
- delivery-manifestet motsvarar samma RC-version.

Kör efter RC-bygget:

```bash
python scripts/validate_release_candidate.py --project-root . --version 0.1.0-rc.2
```

## Release candidate

Första release candidate för projektet är `0.1.0-rc.2`. Den är avsedd för praktisk provkörning av Chat-, Custom GPT- och OpenCode-distributionerna innan en eventuell `0.1.0`-release.
