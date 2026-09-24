# WoW Forever Macros

Macro cheatsheet for World of Warcraft: Forever (Classic+ on the Classic client, vanilla spell names, level cap 60).
Live site: GitHub Pages from `main` / root → https://nobody174.github.io/wow-forever-macros/

Small multi-page site: `index.html` is the countdown/landing page ("Venom & Trollmann's
Road to Forever"), `macros.html` is the macro cheatsheet, `builds.html` is a
coming-soon placeholder. All three share a top bar (site title, Macros / Builds /
Talent Calc links, current page highlighted).

## Files
- `data.py` — single source of truth for every macro. Edit macros HERE only.
- `template.html` — HTML/CSS/JS shell (shared top bar + macro cheatsheet UI);
  `__DATA__` is replaced with the macro JSON at build time, `__PAGE_MACROS__` /
  `__PAGE_BUILDS__` are replaced with `aria-current="page"` markers.
- `build.py` — generates `macros.html` and `wow-forever-macros.md` from `data.py` +
  `template.html`.
- `macros.html`, `wow-forever-macros.md` — generated output. Never hand-edit; run
  `python build.py`.
- `index.html` — hand-written landing page. Hero background (`assets/hero.webp`),
  title, countdown to the WoW Forever launch, and the visitor's local launch time via
  `Intl.DateTimeFormat`. Countdown target: `2026-11-04T23:00:00Z`. Hand-edit directly.
- `builds.html` — hand-written "coming soon" placeholder page. Hand-edit directly.
- `assets/hero.webp` — landing page hero background (dwarf/gnome group in front of
  Frostforge Pass gate, nameplates "Venom" and "Trollmann" over the two dwarves).
  Generated via local ComfyUI (SDXL base + inpainting), finalized with Pillow
  (crop/resize to 2560×1080, nameplate overlay in Cinzel, exported as WebP < 500KB).
- `assets/drafts/` — gitignored scratch folder for hero-image generation drafts/
  intermediates. Not part of the deployed site.

## Workflow
1. Macro changes: edit `data.py` (or `template.html` for cheatsheet layout/top bar
   changes), then run `python build.py`.
2. Landing/builds page changes: hand-edit `index.html` / `builds.html` directly.
3. Check every macro is <= 255 characters.
4. Test locally with `python -m http.server` before pushing.
5. Commit with a clear message and push to `main` (Pages redeploys in ~1 minute).

## Macro style rules (strict)
- Short, one-liners whenever possible. No bloated conditions.
- DPS: `/cast [@targettarget, harm, exists][harm] SPELL`
- Heal/utility (friendly only): `/cast [@mouseover, help, exists][help] SPELL`
- Friend-or-foe spells (e.g. Dispel Magic): `/cast [@mouseover, exists][exists] SPELL`
- Buffs: `/cast [@mouseover, help, exists][help][@player] SPELL`
- Spam-safe channels: `/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] SPELL`
- Focus: `/cast [@focus, harm, exists][harm] SPELL`
- Wand (must stay exactly two lines, never use !Shoot):
  ```
  /cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
  /cast [harm, nochanneling:Shoot] Shoot
  ```
- Melee: `/startattack [@targettarget, harm, exists][harm]`
- Hunter Auto Shot is the one exception that uses `!Auto Shot`.
- No ranks in spell names (highest rank casts automatically).
- All code and comments in English.

## Structure in data.py
Each class has a "Shared" section (all specs) plus spec sections. Macro types:
TT-aware DPS, Mouseover healing / utility, Cleanse / dispel, Wand / auto-attack,
Buffs, Panic / defensive, Targeting helpers, Class QoL, Focus.
Use helpers: dps(), heal(), util(), buff(), chan(), foc(), plain(), me(), stance().
