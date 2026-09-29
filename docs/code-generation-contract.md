# Kodgenereringskontrakt – översikt

Steg 4 låser standardarkitekturen för körbara prototyper.

## Standard

- React + TypeScript + Vite
- frontend-only
- deterministiska fixtures
- tunt simulerat service-lager
- `localStorage` när demoändringar behöver överleva omladdning
- statisk routing som fungerar på GitHub Pages
- responsiv UX för mobil, tablet och desktop
- `dist/` som statisk buildoutput
- README med demo-, reset-, build- och deploymentinstruktioner

Den normativa versionen finns i `assistant/policies/code-generation-contract.md`.

## Viktiga principer

1. Exempeldata är en del av implementationen, inte dekorativ testdata.
2. Slumpmässiga fel undviks; felvägar ska kunna demonstreras deterministiskt.
3. UI och mockdata separeras när interaktionen är mer än trivial.
4. Persistens ska kunna återställas till fixtures.
5. Responsivitet ska realisera prototypspecifikationen, inte bara krympa desktop-layouten.
6. Kärnflöden ska fungera utan verklig backend och utan applikationshemligheter.
7. GitHub Pages-base och routing ska vara explicit hanterade.
