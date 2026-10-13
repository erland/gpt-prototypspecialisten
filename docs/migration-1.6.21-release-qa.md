# Migrering – releasekvalitet

Versionsbunden GPT Byggaren-originalmotor finns i `tooling/gpt-byggaren-1.6.21/` och används av CI/release. `scripts/` innehåller även äldre projektspecifika kontroller. De fem paketen genereras från en canonical instruktion och testas med paritetsgranskning av de faktiska ZIP-arkiven, inte föråldrade `build/`-kataloger.

En stabil release kräver dessutom manuella smoke-tester i respektive runtime. Dessa är inte utförda av denna CI-kontroll. Installations-/runtimebeteende för tredjepartsplattformar kan inte intygas utifrån ZIP-struktur enbart.
