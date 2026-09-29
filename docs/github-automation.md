# GitHub automation

Projektet följer GPT Byggarens standard för GitHub-redo projekt.

## CI

`.github/workflows/ci.yml` kör vid push, pull request och manuell dispatch. Den kör lint, regressionstester, modellrobusthet, eval coverage, final hygiene, bygger alla targets i `build_system.targets` med version `0.0.0-ci`, validerar distributionerna, verifierar runtime parity och kör release-readinessmodellen i CI-läge.

CI-versionen är aldrig en releaseversion. Byggda filer laddas upp som GitHub Actions-artifact för felsökning och verifiering.

## GitHub Release

`.github/workflows/release.yml` kör när en GitHub Release publiceras. Versionsnumret härleds enbart från `github.event.release.tag_name`, till exempel `v0.1.0-rc.2` → `0.1.0-rc.2`.

Workflowet kör samma kvalitetskedja som CI, bygger projekt-ZIP samt samtliga aktiverade runtime-distributioner, validerar readiness och bifogar följande till releasen:

- alla ZIP-distributioner,
- `SHA256SUMS.txt`,
- `DELIVERY-MANIFEST.json`.

Nya runtime-targets som läggs till i `build_system.targets` byggs automatiskt av båda workflowen eftersom de inte hårdkodar targetlistan.

## RC-status

Efter en godkänd release candidate ska `project-status.yaml` rekommendera `stable_release` som nästa steg. En RC med tomt `next_step` betraktas inte längre som korrekt enligt projektets RC-policy.
