import json
from data import *

ORDER = [DPS, HEAL, CLEAN, AUTO, BUFF, PANIC, TARGET, QOL, FOCUS, MISC]
def sort_groups(gs): return sorted(gs, key=lambda g: ORDER.index(g["type"]))

INTRO_RULES = [
 ("TT-aware DPS", dps("SPELL")),
 ("Mouseover heal / utility", heal("SPELL")),
 ("Friend-or-foe (Dispel Magic)", util("SPELL")),
 ("Buffs (adds self fallback)", buff("SPELL")),
 ("Spam-safe channel", chan("SPELL")),
 ("Wand", WAND),
]

# ---------- Markdown ----------
md = []
md.append("# WoW Forever Macro Cheatsheet (nobody174 style)\n")
md.append("Copy/paste macros for Priest, Shaman, Paladin, Warlock, Hunter and Warrior. "
          "Each class has a **Shared** section (every spec uses it) plus spec-only extras.\n")
md.append("## Patterns\n")
for n, c in INTRO_RULES:
    md.append(f"**{n}**\n```\n{c}\n```\n")
md.append("## Notes\n")
md.append("- Spells without a rank cast your highest rank automatically.\n"
          "- Buff macros add `[@player]` as a last fallback so they self-buff with no target. Delete it if you want the strict two-clause style.\n"
          "- Item macros (`/use ...`) need the item name edited to the rank you carry.\n"
          "- WoW Forever changes some classes/systems; if a spell name is renamed or missing in beta, swap the name and keep the pattern.\n"
          "- Macro limit is 255 characters; every macro here fits.\n")

md.append("## Universal (all classes)\n")
for g in UNIVERSAL:
    md.append(f"### {g['type']}\n")
    for m in g["macros"]:
        md.append(f"**{m['name']}**" + (f" — {m['note']}" if m['note'] else "") + "\n")
        md.append(f"```\n{m['code']}\n```\n")

for cls in CLASSES:
    md.append(f"## {cls['name']}\n")
    for sec in cls["sections"]:
        title = "Shared (all specs)" if sec["spec"] == "Shared" else sec["spec"]
        md.append(f"### {cls['name']} — {title}\n")
        for g in sort_groups(sec["groups"]):
            md.append(f"#### {g['type']}\n")
            for m in g["macros"]:
                if not m["code"]:
                    md.append(f"*{m['note']}*\n"); continue
                md.append(f"**{m['name']}**" + (f" — {m['note']}" if m['note'] else "") + "\n")
                md.append(f"```\n{m['code']}\n```\n")

open("wow-forever-macros.md", "w", encoding="utf-8").write("\n".join(md))

# ---------- HTML ----------
payload = {"universal": {"name": "Universal", "color": "#FFD100",
                         "sections": [{"spec": "All classes", "groups": UNIVERSAL}]},
           "classes": CLASSES, "order": ORDER,
           "patterns": [{"name": n, "code": c} for n, c in INTRO_RULES]}
tpl = open("template.html", encoding="utf-8").read()
tpl = (tpl.replace("__DATA__", json.dumps(payload))
          .replace("__PAGE_MACROS__", 'aria-current="page"')
          .replace("__PAGE_BUILDS__", ""))
open("macros.html", "w", encoding="utf-8").write(tpl)
print("built")
