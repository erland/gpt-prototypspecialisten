## Förhandsvisning och optional tool pipeline

Följ `assistant/policies/preview-contract.md`. Klassificera previews som `design_mockup`, `app_screenshot` eller `code_preview`. En `app_screenshot` kräver faktisk browser-rendering av aktuell app med känd viewport och spårbar arbetsversion.

Välj verktyg efter kapabilitet:

- **workspace_build:** Agent Workspace när tillgängligt för projektverifiering/build och temporär buildartefakt.
- **temporary_preview:** PWA Preview när en byggd statisk ZIP/tar.gz kan nås via HTTPS och publik preview behövs.
- **browser_screenshot:** Browser Screenshot när en publik HTTP(S)-URL finns och faktisk rendering tillför värde.
- **local_fallback:** utan dessa fortsätter kärnflödet med hostens filer/kodexekvering, statisk granskning och designmockup/code preview.

När alla tre finns är normal kedja **Agent Workspace → PWA Preview → Browser Screenshot**. Ta normalt en desktop-screenshot. Tablet/mobil tas på begäran, vid responsiv ändring/risk eller uppföljning.

Koppla aldrig ihop steg utan verklig överlämningsväg. Browser Screenshot behöver publik URL; PWA Preview behöver nåbar byggartefakt. Om länken saknas markeras steget `not_tested` i stället för att påstås verifierat.

Rensa temporära resurser efter användning: preview när den inte ska delas vidare, därefter workspace. Om användaren ska prova previewn själv får den leva kvar enligt previewtjänstens TTL.

Om preview/browser fallerar: behåll tidigare verifierad evidens, registrera felet som icke-blockerande, fortsätt med möjlig fallback och påstå aldrig att det misslyckade steget passerat.

