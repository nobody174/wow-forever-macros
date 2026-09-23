# WoW Forever Macros

Macro cheatsheet for World of Warcraft: Forever (Classic+ on the Classic client, vanilla spell names, level cap 60).
Live site: GitHub Pages from `main` / root → https://nobody174.github.io/wow-forever-macros/

## Files
- `data.py` — single source of truth for every macro. Edit macros HERE only.
- `template.html` — HTML/CSS/JS shell; `__DATA__` is replaced with JSON at build time.
- `build.py` — generates `index.html` and `wow-forever-macros.md` from `data.py` + `template.html`.
- `index.html`, `wow-forever-macros.md` — generated output. Never hand-edit; run `python build.py`.

## Workflow
1. Edit `data.py` (or `template.html` for layout/design changes).
2. Run `python build.py`.
3. Check every macro is <= 255 characters.
4. Commit with a clear message and push to `main` (Pages redeploys in ~1 minute).

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
