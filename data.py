# Macro data source for nobody174's WoW Forever cheatsheet.
# All patterns follow the user's style rules exactly.

def dps(s):   return f"#showtooltip {s}\n/cast [@targettarget, harm, exists][harm] {s}"
def heal(s):  return f"#showtooltip {s}\n/cast [@mouseover, help, exists][help] {s}"
def util(s):  return f"#showtooltip {s}\n/cast [@mouseover, exists][exists] {s}"
def buff(s):  return f"#showtooltip {s}\n/cast [@mouseover, help, exists][help][@player] {s}"
def chan(s):  return f"#showtooltip {s}\n/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] {s}"
def foc(s):   return f"#showtooltip {s}\n/cast [@focus, harm, exists][harm] {s}"
def plain(s): return f"#showtooltip {s}\n/cast {s}"
def me(s):    return f"#showtooltip {s}\n/cast [@player] {s}"
def stance(n, stance_name, spell, tt=True):
    target = "[@targettarget, harm, exists][harm] " if tt else ""
    return f"#showtooltip {spell}\n/cast [nostance:{n}] {stance_name}; {target}{spell}"

WAND  = "#showtooltip Shoot\n/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot\n/cast [harm, nochanneling:Shoot] Shoot"
MELEE = "/startattack [@targettarget, harm, exists][harm]"
PETATK = "/petattack [@targettarget, harm, exists][harm]"

def M(name, code, note=""): return {"name": name, "code": code, "note": note}
def G(kind, macros): return {"type": kind, "macros": macros}

# Macro type labels (the 8 requested categories, plus Misc / UI)
DPS, HEAL, CLEAN, AUTO, BUFF, PANIC, TARGET, QOL, FOCUS, MISC = (
    "TT-aware DPS", "Mouseover healing / utility", "Cleanse / dispel",
    "Wand / auto-attack", "Buffs", "Panic / defensive", "Targeting helpers",
    "Class QoL", "Focus", "Misc / UI")

UNIVERSAL = [
    G(TARGET, [
        M("Smart target enemy", "/targetenemy [noharm][dead]", "Only grabs a new enemy if you have no live hostile target."),
        M("Grab TT (take the mob off your friend)", "/target [@targettarget, harm, exists]"),
        M("Assist mouseover / friendly target", "/assist [@mouseover, help, exists][help]"),
        M("Clear dead target", "/cleartarget [dead]"),
        M("Skull mark mouseover / target", "/tm [@mouseover, exists][] 8", "8 = skull, 7 = cross, 5 = moon, 6 = square."),
    ]),
    G(FOCUS, [
        M("Set focus (mouseover first)", "/focus [@mouseover, exists][]"),
        M("Clear focus", "/clearfocus"),
        M("Target focus", "/target focus"),
        M("Assist focus (set tank as focus)", "/assist focus"),
    ]),
    G(PANIC, [
        M("Healing potion", "/use Major Healing Potion", "Swap the item name to the potion rank you carry."),
        M("Mana potion", "/use Major Mana Potion", "Swap the item name to the potion rank you carry."),
    ]),
    G(MISC, [
        M("Zoom out more", "/console cameraDistanceMaxZoomFactor 4", "Raises the max camera zoom-out distance beyond the default cap."),
        M("Hide guild names", "/console UnitNamePlayerGuild 0", "Removes guild tags from nameplates and unit frames."),
        M("Hide PvP titles", "/console UnitNamePlayerPVPTitle 0", "Removes PvP rank titles from nameplates and unit frames."),
        M("Mark mouseover/target with skull", "/tm [@mouseover,exists] 8; 8", "Marks your mouseover target with a skull, or your current target if no mouseover."),
        M("Mark mouseover/target with cross", "/tm [@mouseover,exists] 7; 7", "Same as skull mark, using the cross icon instead."),
        M("Weapon swap: 1H+offhand ↔ 2H", "/equipslot 16 Durgen's Crescent Axe\n/equipslot 17 Veteran Shield\n/equipslot 16 Ironforge Greathammer", "Swap the item names for your own gear. Toggles between 1H+offhand and 2H each press — slot 16 = main hand, 17 = off hand/shield."),
    ]),
]

CLASSES = [
 {"name": "Priest", "color": "#FFFFFF", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Shadow Word: Pain", dps("Shadow Word: Pain")), M("Mind Blast", dps("Mind Blast")),
            M("Smite", dps("Smite")), M("Holy Fire", dps("Holy Fire")), M("Mana Burn", dps("Mana Burn"))]),
    G(AUTO, [M("Wand (spam-safe)", WAND)]),
    G(HEAL, [M("Flash Heal", heal("Flash Heal")), M("Heal", heal("Heal")), M("Greater Heal", heal("Greater Heal")),
             M("Lesser Heal", heal("Lesser Heal")), M("Renew", heal("Renew")),
             M("Power Word: Shield", heal("Power Word: Shield")), M("Prayer of Healing", plain("Prayer of Healing"), "Party-wide, no target needed."),
             M("Resurrection", heal("Resurrection"))]),
    G(CLEAN, [M("Dispel Magic (friend or foe)", util("Dispel Magic")), M("Cure Disease", heal("Cure Disease")),
              M("Abolish Disease", heal("Abolish Disease"))]),
    G(BUFF, [M("Power Word: Fortitude", buff("Power Word: Fortitude")), M("Prayer of Fortitude", buff("Prayer of Fortitude")),
             M("Shadow Protection", buff("Shadow Protection")), M("Levitate", buff("Levitate")),
             M("Inner Fire", plain("Inner Fire")), M("Fear Ward", buff("Fear Ward"), "Racial/availability may differ in Forever.")]),
    G(PANIC, [M("Shield self", me("Power Word: Shield")), M("Psychic Scream", plain("Psychic Scream")),
              M("Fade", plain("Fade")), M("Desperate Prayer", plain("Desperate Prayer"), "Racial priest spell.")]),
    G(FOCUS, [M("Shackle Undead on focus", foc("Shackle Undead")), M("Mind Control on focus", foc("Mind Control"))]),
  ]},
  {"spec": "Shadow", "groups": [
    G(DPS, [M("Mind Flay (spam-safe)", chan("Mind Flay"), "Won't clip an active channel."),
            M("Vampiric Embrace", dps("Vampiric Embrace")), M("Silence", dps("Silence")),
            M("Devouring Plague", dps("Devouring Plague"), "Racial priest spell.")]),
    G(BUFF, [M("Shadowform (no cancel)", "#showtooltip Shadowform\n/cast [noform] Shadowform", "Won't drop you out of form if pressed again.")]),
    G(FOCUS, [M("Silence focus", foc("Silence"))]),
  ]},
  {"spec": "Holy", "groups": [
    G(HEAL, [M("Inner Focus + Greater Heal", "#showtooltip Greater Heal\n/cast Inner Focus\n/cast [@mouseover, help, exists][help] Greater Heal"),
             M("Holy Nova", plain("Holy Nova")), M("Lightwell", plain("Lightwell"))]),
  ]},
  {"spec": "Discipline", "groups": [
    G(HEAL, [M("Power Infusion", heal("Power Infusion")),
             M("Inner Focus + Greater Heal", "#showtooltip Greater Heal\n/cast Inner Focus\n/cast [@mouseover, help, exists][help] Greater Heal")]),
    G(BUFF, [M("Divine Spirit", buff("Divine Spirit"))]),
  ]},
 ]},

 {"name": "Shaman", "color": "#0070DE", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Lightning Bolt", dps("Lightning Bolt")), M("Chain Lightning", dps("Chain Lightning")),
            M("Earth Shock", dps("Earth Shock")), M("Flame Shock", dps("Flame Shock")),
            M("Frost Shock", dps("Frost Shock")), M("Purge (offensive dispel)", dps("Purge"))]),
    G(AUTO, [M("Auto-attack (spam-safe)", MELEE)]),
    G(HEAL, [M("Healing Wave", heal("Healing Wave")), M("Lesser Healing Wave", heal("Lesser Healing Wave")),
             M("Chain Heal", heal("Chain Heal")), M("Ancestral Spirit", heal("Ancestral Spirit"))]),
    G(CLEAN, [M("Cure Poison", heal("Cure Poison")), M("Cure Disease", heal("Cure Disease"))]),
    G(BUFF, [M("Lightning Shield", plain("Lightning Shield")), M("Rockbiter Weapon", plain("Rockbiter Weapon")),
             M("Flametongue Weapon", plain("Flametongue Weapon")), M("Frostbrand Weapon", plain("Frostbrand Weapon")),
             M("Water Walking", buff("Water Walking")), M("Water Breathing", buff("Water Breathing"))]),
    G(PANIC, [M("Self Lesser Healing Wave", me("Lesser Healing Wave")), M("Stoneclaw Totem", plain("Stoneclaw Totem")),
              M("Grounding Totem", plain("Grounding Totem")), M("Ghost Wolf (no cancel)", "#showtooltip Ghost Wolf\n/cast [noform] Ghost Wolf")]),
    G(QOL, [M("Totems: melee group (press 4x)", "#showtooltip Strength of Earth Totem\n/castsequence reset=combat Strength of Earth Totem, Windfury Totem, Searing Totem, Mana Spring Totem"),
            M("Totems: caster group (press 4x)", "#showtooltip Stoneskin Totem\n/castsequence reset=combat Stoneskin Totem, Grace of Air Totem, Searing Totem, Mana Spring Totem", "Swap Grace of Air for Tranquil Air if you prefer."),
            M("Tremor Totem", plain("Tremor Totem")), M("Poison Cleansing Totem", plain("Poison Cleansing Totem")),
            M("Disease Cleansing Totem", plain("Disease Cleansing Totem")), M("Earthbind Totem", plain("Earthbind Totem")),
            M("Magma Totem", plain("Magma Totem")), M("Fire Nova Totem", plain("Fire Nova Totem")),
            M("Healing Stream Totem", plain("Healing Stream Totem"))]),
    G(FOCUS, [M("Earth Shock interrupt on focus", foc("Earth Shock")), M("Purge focus", foc("Purge"))]),
  ]},
  {"spec": "Elemental", "groups": [
    G(DPS, [M("Elemental Mastery + Chain Lightning", "#showtooltip Chain Lightning\n/cast Elemental Mastery\n/cast [@targettarget, harm, exists][harm] Chain Lightning"),
            M("Elemental Mastery + Lightning Bolt", "#showtooltip Lightning Bolt\n/cast Elemental Mastery\n/cast [@targettarget, harm, exists][harm] Lightning Bolt")]),
  ]},
  {"spec": "Enhancement", "groups": [
    G(DPS, [M("Stormstrike", dps("Stormstrike"), "Also starts auto-attack.")]),
    G(BUFF, [M("Windfury Weapon", plain("Windfury Weapon"))]),
  ]},
 ]},

 {"name": "Paladin", "color": "#F58CBA", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Judgement", dps("Judgement")), M("Hammer of Wrath", dps("Hammer of Wrath")),
            M("Exorcism", dps("Exorcism")), M("Hammer of Justice", dps("Hammer of Justice")),
            M("Consecration", plain("Consecration")), M("Holy Wrath", plain("Holy Wrath"))]),
    G(AUTO, [M("Auto-attack (spam-safe)", MELEE)]),
    G(HEAL, [M("Holy Light", heal("Holy Light")), M("Flash of Light", heal("Flash of Light")),
             M("Lay on Hands", heal("Lay on Hands")), M("Blessing of Protection", heal("Blessing of Protection")),
             M("Blessing of Freedom", heal("Blessing of Freedom")), M("Redemption", heal("Redemption"))]),
    G(CLEAN, [M("Cleanse", heal("Cleanse")), M("Purify", heal("Purify"))]),
    G(BUFF, [M("Blessing of Might", buff("Blessing of Might")), M("Blessing of Wisdom", buff("Blessing of Wisdom")),
             M("Blessing of Salvation", buff("Blessing of Salvation")), M("Blessing of Light", buff("Blessing of Light")),
             M("Greater Blessing of Might", buff("Greater Blessing of Might")),
             M("Greater Blessing of Wisdom", buff("Greater Blessing of Wisdom")),
             M("Devotion Aura", plain("Devotion Aura")), M("Retribution Aura", plain("Retribution Aura")),
             M("Concentration Aura", plain("Concentration Aura"))]),
    G(PANIC, [M("Divine Shield", plain("Divine Shield")), M("Divine Protection", plain("Divine Protection")),
              M("Lay on Hands self", me("Lay on Hands")), M("Blessing of Protection self", me("Blessing of Protection"))]),
    G(QOL, [M("Seal of Righteousness", plain("Seal of Righteousness")), M("Seal of the Crusader", plain("Seal of the Crusader")),
            M("Seal of Wisdom", plain("Seal of Wisdom")), M("Seal of Light", plain("Seal of Light")),
            M("Seal of Justice", plain("Seal of Justice")),
            M("Judge + reseal Righteousness loop", "#showtooltip Seal of Righteousness\n/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Righteousness, Judgement", "Press: seal, judge, seal, judge..."),
            M("Crusader opener, then Righteousness", "#showtooltip Seal of the Crusader\n/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Righteousness"),
            M("Divine Intervention", heal("Divine Intervention"))]),
    G(FOCUS, [M("Hammer of Justice focus", foc("Hammer of Justice")), M("Turn Undead focus", foc("Turn Undead"))]),
  ]},
  {"spec": "Retribution", "groups": [
    G(DPS, [M("Repentance", dps("Repentance"))]),
    G(BUFF, [M("Sanctity Aura", plain("Sanctity Aura")), M("Seal of Command", plain("Seal of Command"))]),
    G(QOL, [M("Crusader opener, then Command", "#showtooltip Seal of the Crusader\n/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Command"),
            M("Judge + reseal Command loop", "#showtooltip Seal of Command\n/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Command, Judgement")]),
    G(FOCUS, [M("Repentance focus", foc("Repentance"))]),
  ]},
  {"spec": "Protection", "groups": [
    G(DPS, [M("Holy Shield", plain("Holy Shield"))]),
    G(BUFF, [M("Righteous Fury", plain("Righteous Fury")), M("Blessing of Kings", buff("Blessing of Kings")),
             M("Blessing of Sanctuary", buff("Blessing of Sanctuary"))]),
    G(QOL, [M("Judge + reseal Wisdom loop", "#showtooltip Seal of Wisdom\n/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Wisdom, Judgement", "Mana-sustain tanking.")]),
  ]},
 ]},

 {"name": "Warlock", "color": "#8788EE", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Shadow Bolt", dps("Shadow Bolt")), M("Corruption", dps("Corruption")),
            M("Curse of Agony", dps("Curse of Agony")), M("Immolate", dps("Immolate")),
            M("Searing Pain", dps("Searing Pain")), M("Soul Fire", dps("Soul Fire")),
            M("Death Coil", dps("Death Coil")), M("Drain Life (spam-safe)", chan("Drain Life")),
            M("Drain Soul (spam-safe)", chan("Drain Soul")), M("Drain Mana (spam-safe)", chan("Drain Mana")),
            M("Curse of the Elements", dps("Curse of the Elements")), M("Curse of Shadow", dps("Curse of Shadow")),
            M("Curse of Recklessness", dps("Curse of Recklessness")), M("Curse of Weakness", dps("Curse of Weakness")),
            M("Curse of Tongues", dps("Curse of Tongues")), M("Hellfire", plain("Hellfire")),
            M("Rain of Fire", plain("Rain of Fire"))]),
    G(AUTO, [M("Wand (spam-safe)", WAND)]),
    G(HEAL, [M("Health Funnel (pet)", plain("Health Funnel")), M("Unending Breath", buff("Unending Breath")),
             M("Detect Invisibility", buff("Detect Invisibility")),
             M("Soulstone mouseover", "/use [@mouseover, help, exists][help] Major Soulstone", "Swap item name to your soulstone rank.")]),
    G(CLEAN, [M("Devour Magic (Felhunter)", heal("Devour Magic"))]),
    G(BUFF, [M("Demon Armor", plain("Demon Armor")), M("Shadow Ward", plain("Shadow Ward"))]),
    G(PANIC, [M("Healthstone", "/use Major Healthstone", "Swap item name to your healthstone rank."),
              M("Howl of Terror", plain("Howl of Terror")), M("Fear", dps("Fear")),
              M("Sacrifice (Voidwalker)", plain("Sacrifice")), M("Life Tap", plain("Life Tap"))]),
    G(QOL, [M("Pet attack TT / target", PETATK), M("Pet follow", "/petfollow"),
            M("Pet passive", "/petpassive"), M("Pet defensive", "/petdefensive"),
            M("Spell Lock (Felhunter)", dps("Spell Lock")), M("Torment (Voidwalker taunt)", dps("Torment")),
            M("Summon Felhunter", plain("Summon Felhunter")), M("Summon Voidwalker", plain("Summon Voidwalker")),
            M("Summon Succubus", plain("Summon Succubus")), M("Summon Imp", plain("Summon Imp"))]),
    G(FOCUS, [M("Fear focus", foc("Fear")), M("Banish focus", foc("Banish")), M("Seduction focus", foc("Seduction")),
              M("Spell Lock focus", foc("Spell Lock")), M("Enslave Demon focus", foc("Enslave Demon"))]),
  ]},
  {"spec": "Affliction", "groups": [
    G(DPS, [M("Siphon Life", dps("Siphon Life")), M("Curse of Exhaustion", dps("Curse of Exhaustion")),
            M("Amplify Curse + Agony", "#showtooltip Curse of Agony\n/cast Amplify Curse\n/cast [@targettarget, harm, exists][harm] Curse of Agony"),
            M("DoT sequence (press to roll dots)", "#showtooltip Corruption\n/castsequence [@targettarget, harm, exists][harm] reset=target Corruption, Curse of Agony, Siphon Life, Immolate")]),
    G(PANIC, [M("Dark Pact", plain("Dark Pact"))]),
  ]},
  {"spec": "Demonology", "groups": [
    G(QOL, [M("Fel Domination + Felhunter", "#showtooltip Summon Felhunter\n/cast Fel Domination\n/cast Summon Felhunter"),
            M("Fel Domination + Voidwalker", "#showtooltip Summon Voidwalker\n/cast Fel Domination\n/cast Summon Voidwalker"),
            M("Soul Link", plain("Soul Link")), M("Demonic Sacrifice", plain("Demonic Sacrifice"))]),
  ]},
  {"spec": "Destruction", "groups": [
    G(DPS, [M("Conflagrate", dps("Conflagrate")), M("Shadowburn", dps("Shadowburn")),
            M("Immolate > Conflagrate", "#showtooltip Immolate\n/castsequence [@targettarget, harm, exists][harm] reset=target/10 Immolate, Conflagrate")]),
  ]},
 ]},

 {"name": "Hunter", "color": "#ABD473", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Hunter's Mark", dps("Hunter's Mark")), M("Serpent Sting", dps("Serpent Sting")),
            M("Arcane Shot", dps("Arcane Shot")), M("Multi-Shot", dps("Multi-Shot")),
            M("Concussive Shot", dps("Concussive Shot")), M("Viper Sting", dps("Viper Sting")),
            M("Scorpid Sting", dps("Scorpid Sting")), M("Raptor Strike", dps("Raptor Strike")),
            M("Mongoose Bite", dps("Mongoose Bite")), M("Wing Clip", dps("Wing Clip")),
            M("Distracting Shot", dps("Distracting Shot")),
            M("Tranquilizing Shot (enrage dispel)", dps("Tranquilizing Shot"), "Hunter's only dispel: removes Frenzy from enemies.")]),
    G(AUTO, [M("Auto Shot (spam-safe)", "#showtooltip Auto Shot\n/cast [@targettarget, harm, exists][harm] !Auto Shot",
               "Hunter exception: ! stops Auto Shot toggling off. Unlike wand Shoot, it works here."),
             M("Melee auto-attack", MELEE)]),
    G(BUFF, [M("Aspect: Hawk in combat, Cheetah out", "#showtooltip Aspect of the Hawk\n/cast [combat] Aspect of the Hawk; Aspect of the Cheetah"),
             M("Aspect of the Hawk", plain("Aspect of the Hawk")), M("Aspect of the Monkey", plain("Aspect of the Monkey")),
             M("Aspect of the Pack", plain("Aspect of the Pack")), M("Aspect of the Wild", plain("Aspect of the Wild"))]),
    G(PANIC, [M("Feign Death", plain("Feign Death")), M("Disengage", dps("Disengage")),
              M("Freezing Trap", plain("Freezing Trap")), M("Frost Trap", plain("Frost Trap")),
              M("Rapid Fire", plain("Rapid Fire"))]),
    G(QOL, [M("Pet attack TT / target", PETATK), M("Pet follow", "/petfollow"), M("Pet passive", "/petpassive"),
            M("Call / Revive / Mend (one button)", "#showtooltip Mend Pet\n/cast [nopet] Call Pet; [@pet, dead] Revive Pet; Mend Pet"),
            M("Feed Pet", "#showtooltip Feed Pet\n/cast Feed Pet\n/use Tough Jerky", "Swap food item for your pet's diet."),
            M("Flare", plain("Flare")), M("Explosive Trap", plain("Explosive Trap")),
            M("Immolation Trap", plain("Immolation Trap"))]),
    G(CLEAN, [M("No friendly dispel", "", "Hunters have no friendly cleanse. Use Tranquilizing Shot (TT-aware DPS) instead.")]),
    G(FOCUS, [M("Hunter's Mark focus", foc("Hunter's Mark")), M("Concussive Shot focus", foc("Concussive Shot"))]),
  ]},
  {"spec": "Beast Mastery", "groups": [
    G(DPS, [M("Bestial Wrath + Rapid Fire burst", "#showtooltip Bestial Wrath\n/cast Bestial Wrath\n/cast Rapid Fire"),
            M("Intimidation", plain("Intimidation"), "Pet's next hit stuns its target.")]),
  ]},
  {"spec": "Marksmanship", "groups": [
    G(DPS, [M("Aimed Shot", dps("Aimed Shot")), M("Scatter Shot", dps("Scatter Shot"))]),
    G(BUFF, [M("Trueshot Aura", plain("Trueshot Aura"))]),
    G(FOCUS, [M("Scatter Shot focus", foc("Scatter Shot"))]),
  ]},
  {"spec": "Survival", "groups": [
    G(DPS, [M("Counterattack", dps("Counterattack")), M("Wyvern Sting", dps("Wyvern Sting"))]),
    G(PANIC, [M("Deterrence", plain("Deterrence"))]),
    G(FOCUS, [M("Wyvern Sting focus", foc("Wyvern Sting"))]),
  ]},
 ]},

 {"name": "Warrior", "color": "#C79C6E", "sections": [
  {"spec": "Shared", "groups": [
    G(DPS, [M("Heroic Strike", dps("Heroic Strike")), M("Cleave", dps("Cleave")),
            M("Rend", dps("Rend")), M("Hamstring", dps("Hamstring")), M("Sunder Armor", dps("Sunder Armor")),
            M("Execute", dps("Execute")), M("Overpower (to Battle)", stance(1, "Battle Stance", "Overpower")),
            M("Demoralizing Shout", plain("Demoralizing Shout")),
            M("Thunder Clap (to Battle)", stance(1, "Battle Stance", "Thunder Clap", tt=False))]),
    G(AUTO, [M("Auto-attack (spam-safe)", MELEE)]),
    G(BUFF, [M("Battle Shout", plain("Battle Shout")), M("Bloodrage", plain("Bloodrage")),
             M("Berserker Rage (to Berserker)", stance(3, "Berserker Stance", "Berserker Rage", tt=False))]),
    G(PANIC, [M("Shield Wall (to Defensive)", stance(2, "Defensive Stance", "Shield Wall", tt=False)),
              M("Retaliation (to Battle)", stance(1, "Battle Stance", "Retaliation", tt=False)),
              M("Intimidating Shout", dps("Intimidating Shout")),
              M("Disarm (to Defensive)", stance(2, "Defensive Stance", "Disarm"))]),
    G(QOL, [M("Battle Stance", plain("Battle Stance")), M("Defensive Stance", plain("Defensive Stance")),
            M("Berserker Stance", plain("Berserker Stance")),
            M("Charge / Intercept (one button)", "#showtooltip Charge\n/cast [nocombat, nostance:1] Battle Stance; [nocombat, @targettarget, harm, exists][nocombat, harm] Charge; [nostance:3] Berserker Stance; [@targettarget, harm, exists][harm] Intercept",
              "Out of combat: Charge. In combat: Intercept. Stance swaps cost rage above your Tactical Mastery cap."),
            M("Taunt (to Defensive)", stance(2, "Defensive Stance", "Taunt"), "Target the friend being hit: TT is the mob."),
            M("Mocking Blow (to Battle)", stance(1, "Battle Stance", "Mocking Blow")),
            M("Challenging Shout", plain("Challenging Shout"))]),
    G(CLEAN, [M("No dispel", "", "Warriors have no dispel. Interrupt instead with Pummel or Shield Bash.")]),
    G(FOCUS, [M("Pummel focus", "#showtooltip Pummel\n/cast [nostance:3] Berserker Stance; [@focus, harm, exists][harm] Pummel"),
              M("Shield Bash focus", foc("Shield Bash")), M("Taunt focus", foc("Taunt"))]),
  ]},
  {"spec": "Fury", "groups": [
    G(DPS, [M("Bloodthirst", dps("Bloodthirst")),
            M("Whirlwind (to Berserker)", stance(3, "Berserker Stance", "Whirlwind", tt=False)),
            M("Pummel (to Berserker)", stance(3, "Berserker Stance", "Pummel")),
            M("Slam", dps("Slam")), M("Piercing Howl", plain("Piercing Howl"))]),
    G(BUFF, [M("Death Wish", plain("Death Wish")),
             M("Recklessness (to Berserker)", stance(3, "Berserker Stance", "Recklessness", tt=False))]),
  ]},
  {"spec": "Protection", "groups": [
    G(DPS, [M("Shield Slam", dps("Shield Slam")), M("Revenge", dps("Revenge")),
            M("Shield Bash", dps("Shield Bash")), M("Concussion Blow", dps("Concussion Blow"))]),
    G(PANIC, [M("Shield Block", plain("Shield Block")), M("Last Stand", plain("Last Stand"))]),
  ]},
 ]},
]
