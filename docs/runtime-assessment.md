# Runtime-bedömning

| Runtime | Suitability | Planerad standardaktivering | Kommentar |
|---|---|---:|---|
| ChatGPT Chat | hög | ja, i steg 6 | Stark iterativ dialog, bildanalys och mockupstöd; riktig browser-rendering är miljöberoende. |
| ChatGPT Custom GPT | hög | ja, i steg 7 | Bra användarpaketering; kärnregler måste ligga i canonical instruktion. |
| Claude Projects | medel | nej i första versionen | Behöver separat verifiering av bild-/fil-/renderingsflöde. |
| OpenCode | hög | ja, i steg 8 | Stark för faktisk kodändring, build och test; visuell chat-preview är en parity-skillnad. |
| OpenAI Plugin | medel | nej i första versionen | Relevant senare för skills-first flöde, men inte full parity för lokal exekvering/rendering. |

Runtime-adapters är avsiktligt inte aktiverade i Steg 1. Varje planerat standardmål aktiveras när motsvarande adaptersteg implementeras och valideras.
