# {{GPT_NAME}} — OpenAI Plugin {{VERSION}}

Skills-first runtime för att analysera, bygga, iterera och validera responsiva webbprototyper.

## Skills

{{SKILLS}}

## Runtimekrav

- Filesystem read/write krävs för att skapa och ändra ett verkligt prototypprojekt.
- Persistent workspace/state krävs för iterativ utveckling och återupptagning.
- Code execution krävs för slutlig build-validering av den körbara frontendprototypen.
- Shell är rekommenderad för npm-install/build där hosten erbjuder den.
- Agent Workspace och liknande externa verktyg är valfria integrationsförstärkningar, inte kärnberoenden.
- Browser-rendering och screenshots är valfria förstärkningar; faktisk build får aldrig redovisas som validerad utan evidens.
- Skilj alltid mellan designmockup, faktisk app-screenshot och code preview.
