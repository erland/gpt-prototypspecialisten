# Validering och kvalitetsgates

Steg 5 definierar hur Prototypspecialisten avgör om en prototyp verkligen är demonstrerbar och leveransklar.

Valideringen kombinerar deterministiska kontroller med strukturerad UX-granskning. Build, centrala filer, hosting, huvudflöden och exempeldata är blockerande i normalfallet. Mobil, tablet och desktop ska bedömas när målplattformen inte avgränsats.

Build, publik preview och browser-rendering är tre separata evidensnivåer: `build_verified`, `preview_deployed` och `browser_verified`. Ingen får antas bara för att en annan passerat.

Agent Workspace är föredragen extern build-provider, PWA Preview kan ge temporär publik HTTPS-preview och Browser Screenshot kan verifiera faktisk rendering från publik URL. Alla tre är optional enhancements; kärnflödet ska fungera utan dem.

Normalt tas bara en desktop-screenshot; tablet/mobil tas vid behov. Browser-/previewfel är inte ensamt blockerande, men faktisk build får aldrig påstås vara verifierad utan evidens.

Se canonical policy i `assistant/policies/validation-quality-gates.md`.
