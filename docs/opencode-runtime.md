# OpenCode-runtime

OpenCode är den kodcentrerade runtime-adaptern för Prototypspecialisten och är avsedd för faktisk implementation, build och validering i en repository/workspace.

## Projektion från canonical källor

- `AGENTS.md` genereras från `assistant/instructions.md` och kompletteras endast med OpenCode-specifika workspace-regler.
- `runtime-contract.json` innehåller snapshot av capability-, artifact-, workspace/state- och tool-kontrakten.
- `.opencode/skills/` genereras från canonical skill-definitioner. Om inga separata skills deklarerats skapas en konservativ projektskill från projektmetadata och canonical instruktion.
- `knowledge/` är stödjande och får inte behövas för kärnbeteendet.

## Workspace och kodarbete

OpenCode får använda sin inbyggda filredigering och shell för att skapa och validera prototyper. Den ska arbeta i användarens workspace, inte i assistentdistributionen. Prototypens egen `project-status.yaml` är auktoritativ vid återupptagning.

## Browser-rendering

Playwright/Chromium är aldrig ett hårt krav. Om verklig browser-rendering är tillgänglig kan den användas för screenshots i 390×844, 768×1024 och 1440×900. Om den saknas ska detta markeras i preview-/validation-evidensen och prototypen ska ändå kunna färdigställas när övriga blockerande gates passerar.

## Säkerhet och permissions

OpenCode-konfigurationen använder `ask` för generell shell och filredigering. Eventuella canonical custom tools får explicit permission enligt tool-kontraktet och får inte härledas implicit från godtyckliga scripts.
