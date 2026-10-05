# Runtime-bedömning

| Runtime | Suitability | Planerad standardaktivering | Kommentar |
|---|---|---:|---|
| ChatGPT Chat | hög | ja, i steg 6 | Stark iterativ dialog, bildanalys och mockupstöd; riktig browser-rendering är miljöberoende. |
| ChatGPT Custom GPT | hög | ja, i steg 7 | Bra användarpaketering; kärnregler måste ligga i canonical instruktion. |
| Claude Projects | medel | nej i första versionen | Behöver separat verifiering av bild-/fil-/renderingsflöde. |
| OpenCode | hög | ja, i steg 8 | Stark för faktisk kodändring, build och test; visuell chat-preview är en parity-skillnad. |
| OpenAI Plugin | hög / runtime-beroende | ja | Skills-first peer runtime. Full canonical implementation och build kräver host med writable filesystem, persistent workspace och code execution; Agent Workspace/browser-rendering är optional förstärkning. |

Runtime-adapters aktiveras först när motsvarande adaptersteg implementerats och validerats. OpenAI Plugin använder host-capabilities för faktisk projektimplementation och deklarerar inga syntetiska runtime-tools.
