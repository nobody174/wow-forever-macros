# WoW Forever Macro Cheatsheet (nobody174 style)

Copy/paste macros for Priest, Shaman, Paladin, Warlock, Hunter and Warrior. Each class has a **Shared** section (every spec uses it) plus spec-only extras.

## Patterns

**TT-aware DPS**
```
#showtooltip SPELL
/cast [@targettarget, harm, exists][harm] SPELL
```

**Mouseover heal / utility**
```
#showtooltip SPELL
/cast [@mouseover, help, exists][help] SPELL
```

**Friend-or-foe (Dispel Magic)**
```
#showtooltip SPELL
/cast [@mouseover, exists][exists] SPELL
```

**Buffs (adds self fallback)**
```
#showtooltip SPELL
/cast [@mouseover, help, exists][help][@player] SPELL
```

**Spam-safe channel**
```
#showtooltip SPELL
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] SPELL
```

**Wand**
```
#showtooltip Shoot
/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
/cast [harm, nochanneling:Shoot] Shoot
```

## Notes

- Spells without a rank cast your highest rank automatically.
- Buff macros add `[@player]` as a last fallback so they self-buff with no target. Delete it if you want the strict two-clause style.
- Item macros (`/use ...`) need the item name edited to the rank you carry.
- WoW Forever changes some classes/systems; if a spell name is renamed or missing in beta, swap the name and keep the pattern.
- Macro limit is 255 characters; every macro here fits.

## Universal (all classes)

### Targeting helpers

**Smart target enemy** — Only grabs a new enemy if you have no live hostile target.

```
/targetenemy [noharm][dead]
```

**Grab TT (take the mob off your friend)**

```
/target [@targettarget, harm, exists]
```

**Assist mouseover / friendly target**

```
/assist [@mouseover, help, exists][help]
```

**Clear dead target**

```
/cleartarget [dead]
```

**Skull mark mouseover / target** — 8 = skull, 7 = cross, 5 = moon, 6 = square.

```
/tm [@mouseover, exists][] 8
```

### Focus

**Set focus (mouseover first)**

```
/focus [@mouseover, exists][]
```

**Clear focus**

```
/clearfocus
```

**Target focus**

```
/target focus
```

**Assist focus (set tank as focus)**

```
/assist focus
```

### Panic / defensive

**Healing potion** — Swap the item name to the potion rank you carry.

```
/use Major Healing Potion
```

**Mana potion** — Swap the item name to the potion rank you carry.

```
/use Major Mana Potion
```

### Misc / UI

**Zoom out more** — Raises the max camera zoom-out distance beyond the default cap.

```
/console cameraDistanceMaxZoomFactor 4
```

**Hide guild names** — Removes guild tags from nameplates and unit frames.

```
/console UnitNamePlayerGuild 0
```

**Hide PvP titles** — Removes PvP rank titles from nameplates and unit frames.

```
/console UnitNamePlayerPVPTitle 0
```

**Mark mouseover/target with skull** — Marks your mouseover target with a skull, or your current target if no mouseover.

```
/tm [@mouseover,exists] 8; 8
```

**Mark mouseover/target with cross** — Same as skull mark, using the cross icon instead.

```
/tm [@mouseover,exists] 7; 7
```

## Priest

### Priest — Shared (all specs)

#### TT-aware DPS

**Shadow Word: Pain**

```
#showtooltip Shadow Word: Pain
/cast [@targettarget, harm, exists][harm] Shadow Word: Pain
```

**Mind Blast**

```
#showtooltip Mind Blast
/cast [@targettarget, harm, exists][harm] Mind Blast
```

**Smite**

```
#showtooltip Smite
/cast [@targettarget, harm, exists][harm] Smite
```

**Holy Fire**

```
#showtooltip Holy Fire
/cast [@targettarget, harm, exists][harm] Holy Fire
```

**Mana Burn**

```
#showtooltip Mana Burn
/cast [@targettarget, harm, exists][harm] Mana Burn
```

#### Mouseover healing / utility

**Flash Heal**

```
#showtooltip Flash Heal
/cast [@mouseover, help, exists][help] Flash Heal
```

**Heal**

```
#showtooltip Heal
/cast [@mouseover, help, exists][help] Heal
```

**Greater Heal**

```
#showtooltip Greater Heal
/cast [@mouseover, help, exists][help] Greater Heal
```

**Lesser Heal**

```
#showtooltip Lesser Heal
/cast [@mouseover, help, exists][help] Lesser Heal
```

**Renew**

```
#showtooltip Renew
/cast [@mouseover, help, exists][help] Renew
```

**Power Word: Shield**

```
#showtooltip Power Word: Shield
/cast [@mouseover, help, exists][help] Power Word: Shield
```

**Prayer of Healing** — Party-wide, no target needed.

```
#showtooltip Prayer of Healing
/cast Prayer of Healing
```

**Resurrection**

```
#showtooltip Resurrection
/cast [@mouseover, help, exists][help] Resurrection
```

#### Cleanse / dispel

**Dispel Magic (friend or foe)**

```
#showtooltip Dispel Magic
/cast [@mouseover, exists][exists] Dispel Magic
```

**Cure Disease**

```
#showtooltip Cure Disease
/cast [@mouseover, help, exists][help] Cure Disease
```

**Abolish Disease**

```
#showtooltip Abolish Disease
/cast [@mouseover, help, exists][help] Abolish Disease
```

#### Wand / auto-attack

**Wand (spam-safe)**

```
#showtooltip Shoot
/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
/cast [harm, nochanneling:Shoot] Shoot
```

#### Buffs

**Power Word: Fortitude**

```
#showtooltip Power Word: Fortitude
/cast [@mouseover, help, exists][help][@player] Power Word: Fortitude
```

**Prayer of Fortitude**

```
#showtooltip Prayer of Fortitude
/cast [@mouseover, help, exists][help][@player] Prayer of Fortitude
```

**Shadow Protection**

```
#showtooltip Shadow Protection
/cast [@mouseover, help, exists][help][@player] Shadow Protection
```

**Levitate**

```
#showtooltip Levitate
/cast [@mouseover, help, exists][help][@player] Levitate
```

**Inner Fire**

```
#showtooltip Inner Fire
/cast Inner Fire
```

**Fear Ward** — Racial/availability may differ in Forever.

```
#showtooltip Fear Ward
/cast [@mouseover, help, exists][help][@player] Fear Ward
```

#### Panic / defensive

**Shield self**

```
#showtooltip Power Word: Shield
/cast [@player] Power Word: Shield
```

**Psychic Scream**

```
#showtooltip Psychic Scream
/cast Psychic Scream
```

**Fade**

```
#showtooltip Fade
/cast Fade
```

**Desperate Prayer** — Racial priest spell.

```
#showtooltip Desperate Prayer
/cast Desperate Prayer
```

#### Focus

**Shackle Undead on focus**

```
#showtooltip Shackle Undead
/cast [@focus, harm, exists][harm] Shackle Undead
```

**Mind Control on focus**

```
#showtooltip Mind Control
/cast [@focus, harm, exists][harm] Mind Control
```

### Priest — Shadow

#### TT-aware DPS

**Mind Flay (spam-safe)** — Won't clip an active channel.

```
#showtooltip Mind Flay
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Mind Flay
```

**Vampiric Embrace**

```
#showtooltip Vampiric Embrace
/cast [@targettarget, harm, exists][harm] Vampiric Embrace
```

**Silence**

```
#showtooltip Silence
/cast [@targettarget, harm, exists][harm] Silence
```

**Devouring Plague** — Racial priest spell.

```
#showtooltip Devouring Plague
/cast [@targettarget, harm, exists][harm] Devouring Plague
```

#### Buffs

**Shadowform (no cancel)** — Won't drop you out of form if pressed again.

```
#showtooltip Shadowform
/cast [noform] Shadowform
```

#### Focus

**Silence focus**

```
#showtooltip Silence
/cast [@focus, harm, exists][harm] Silence
```

### Priest — Holy

#### Mouseover healing / utility

**Inner Focus + Greater Heal**

```
#showtooltip Greater Heal
/cast Inner Focus
/cast [@mouseover, help, exists][help] Greater Heal
```

**Holy Nova**

```
#showtooltip Holy Nova
/cast Holy Nova
```

**Lightwell**

```
#showtooltip Lightwell
/cast Lightwell
```

### Priest — Discipline

#### Mouseover healing / utility

**Power Infusion**

```
#showtooltip Power Infusion
/cast [@mouseover, help, exists][help] Power Infusion
```

**Inner Focus + Greater Heal**

```
#showtooltip Greater Heal
/cast Inner Focus
/cast [@mouseover, help, exists][help] Greater Heal
```

#### Buffs

**Divine Spirit**

```
#showtooltip Divine Spirit
/cast [@mouseover, help, exists][help][@player] Divine Spirit
```

## Shaman

### Shaman — Shared (all specs)

#### TT-aware DPS

**Lightning Bolt**

```
#showtooltip Lightning Bolt
/cast [@targettarget, harm, exists][harm] Lightning Bolt
```

**Chain Lightning**

```
#showtooltip Chain Lightning
/cast [@targettarget, harm, exists][harm] Chain Lightning
```

**Earth Shock**

```
#showtooltip Earth Shock
/cast [@targettarget, harm, exists][harm] Earth Shock
```

**Flame Shock**

```
#showtooltip Flame Shock
/cast [@targettarget, harm, exists][harm] Flame Shock
```

**Frost Shock**

```
#showtooltip Frost Shock
/cast [@targettarget, harm, exists][harm] Frost Shock
```

**Purge (offensive dispel)**

```
#showtooltip Purge
/cast [@targettarget, harm, exists][harm] Purge
```

#### Mouseover healing / utility

**Healing Wave**

```
#showtooltip Healing Wave
/cast [@mouseover, help, exists][help] Healing Wave
```

**Lesser Healing Wave**

```
#showtooltip Lesser Healing Wave
/cast [@mouseover, help, exists][help] Lesser Healing Wave
```

**Chain Heal**

```
#showtooltip Chain Heal
/cast [@mouseover, help, exists][help] Chain Heal
```

**Ancestral Spirit**

```
#showtooltip Ancestral Spirit
/cast [@mouseover, help, exists][help] Ancestral Spirit
```

#### Cleanse / dispel

**Cure Poison**

```
#showtooltip Cure Poison
/cast [@mouseover, help, exists][help] Cure Poison
```

**Cure Disease**

```
#showtooltip Cure Disease
/cast [@mouseover, help, exists][help] Cure Disease
```

#### Wand / auto-attack

**Auto-attack (spam-safe)**

```
/startattack [@targettarget, harm, exists][harm]
```

#### Buffs

**Lightning Shield**

```
#showtooltip Lightning Shield
/cast Lightning Shield
```

**Rockbiter Weapon**

```
#showtooltip Rockbiter Weapon
/cast Rockbiter Weapon
```

**Flametongue Weapon**

```
#showtooltip Flametongue Weapon
/cast Flametongue Weapon
```

**Frostbrand Weapon**

```
#showtooltip Frostbrand Weapon
/cast Frostbrand Weapon
```

**Water Walking**

```
#showtooltip Water Walking
/cast [@mouseover, help, exists][help][@player] Water Walking
```

**Water Breathing**

```
#showtooltip Water Breathing
/cast [@mouseover, help, exists][help][@player] Water Breathing
```

#### Panic / defensive

**Self Lesser Healing Wave**

```
#showtooltip Lesser Healing Wave
/cast [@player] Lesser Healing Wave
```

**Stoneclaw Totem**

```
#showtooltip Stoneclaw Totem
/cast Stoneclaw Totem
```

**Grounding Totem**

```
#showtooltip Grounding Totem
/cast Grounding Totem
```

**Ghost Wolf (no cancel)**

```
#showtooltip Ghost Wolf
/cast [noform] Ghost Wolf
```

#### Class QoL

**Totems: melee group (press 4x)**

```
#showtooltip Strength of Earth Totem
/castsequence reset=combat Strength of Earth Totem, Windfury Totem, Searing Totem, Mana Spring Totem
```

**Totems: caster group (press 4x)** — Swap Grace of Air for Tranquil Air if you prefer.

```
#showtooltip Stoneskin Totem
/castsequence reset=combat Stoneskin Totem, Grace of Air Totem, Searing Totem, Mana Spring Totem
```

**Tremor Totem**

```
#showtooltip Tremor Totem
/cast Tremor Totem
```

**Poison Cleansing Totem**

```
#showtooltip Poison Cleansing Totem
/cast Poison Cleansing Totem
```

**Disease Cleansing Totem**

```
#showtooltip Disease Cleansing Totem
/cast Disease Cleansing Totem
```

**Earthbind Totem**

```
#showtooltip Earthbind Totem
/cast Earthbind Totem
```

**Magma Totem**

```
#showtooltip Magma Totem
/cast Magma Totem
```

**Fire Nova Totem**

```
#showtooltip Fire Nova Totem
/cast Fire Nova Totem
```

**Healing Stream Totem**

```
#showtooltip Healing Stream Totem
/cast Healing Stream Totem
```

#### Focus

**Earth Shock interrupt on focus**

```
#showtooltip Earth Shock
/cast [@focus, harm, exists][harm] Earth Shock
```

**Purge focus**

```
#showtooltip Purge
/cast [@focus, harm, exists][harm] Purge
```

### Shaman — Elemental

#### TT-aware DPS

**Elemental Mastery + Chain Lightning**

```
#showtooltip Chain Lightning
/cast Elemental Mastery
/cast [@targettarget, harm, exists][harm] Chain Lightning
```

**Elemental Mastery + Lightning Bolt**

```
#showtooltip Lightning Bolt
/cast Elemental Mastery
/cast [@targettarget, harm, exists][harm] Lightning Bolt
```

### Shaman — Enhancement

#### TT-aware DPS

**Stormstrike** — Also starts auto-attack.

```
#showtooltip Stormstrike
/cast [@targettarget, harm, exists][harm] Stormstrike
```

#### Buffs

**Windfury Weapon**

```
#showtooltip Windfury Weapon
/cast Windfury Weapon
```

## Paladin

### Paladin — Shared (all specs)

#### TT-aware DPS

**Judgement**

```
#showtooltip Judgement
/cast [@targettarget, harm, exists][harm] Judgement
```

**Hammer of Wrath**

```
#showtooltip Hammer of Wrath
/cast [@targettarget, harm, exists][harm] Hammer of Wrath
```

**Exorcism**

```
#showtooltip Exorcism
/cast [@targettarget, harm, exists][harm] Exorcism
```

**Hammer of Justice**

```
#showtooltip Hammer of Justice
/cast [@targettarget, harm, exists][harm] Hammer of Justice
```

**Consecration**

```
#showtooltip Consecration
/cast Consecration
```

**Holy Wrath**

```
#showtooltip Holy Wrath
/cast Holy Wrath
```

#### Mouseover healing / utility

**Holy Light**

```
#showtooltip Holy Light
/cast [@mouseover, help, exists][help] Holy Light
```

**Flash of Light**

```
#showtooltip Flash of Light
/cast [@mouseover, help, exists][help] Flash of Light
```

**Lay on Hands**

```
#showtooltip Lay on Hands
/cast [@mouseover, help, exists][help] Lay on Hands
```

**Blessing of Protection**

```
#showtooltip Blessing of Protection
/cast [@mouseover, help, exists][help] Blessing of Protection
```

**Blessing of Freedom**

```
#showtooltip Blessing of Freedom
/cast [@mouseover, help, exists][help] Blessing of Freedom
```

**Redemption**

```
#showtooltip Redemption
/cast [@mouseover, help, exists][help] Redemption
```

#### Cleanse / dispel

**Cleanse**

```
#showtooltip Cleanse
/cast [@mouseover, help, exists][help] Cleanse
```

**Purify**

```
#showtooltip Purify
/cast [@mouseover, help, exists][help] Purify
```

#### Wand / auto-attack

**Auto-attack (spam-safe)**

```
/startattack [@targettarget, harm, exists][harm]
```

#### Buffs

**Blessing of Might**

```
#showtooltip Blessing of Might
/cast [@mouseover, help, exists][help][@player] Blessing of Might
```

**Blessing of Wisdom**

```
#showtooltip Blessing of Wisdom
/cast [@mouseover, help, exists][help][@player] Blessing of Wisdom
```

**Blessing of Salvation**

```
#showtooltip Blessing of Salvation
/cast [@mouseover, help, exists][help][@player] Blessing of Salvation
```

**Blessing of Light**

```
#showtooltip Blessing of Light
/cast [@mouseover, help, exists][help][@player] Blessing of Light
```

**Greater Blessing of Might**

```
#showtooltip Greater Blessing of Might
/cast [@mouseover, help, exists][help][@player] Greater Blessing of Might
```

**Greater Blessing of Wisdom**

```
#showtooltip Greater Blessing of Wisdom
/cast [@mouseover, help, exists][help][@player] Greater Blessing of Wisdom
```

**Devotion Aura**

```
#showtooltip Devotion Aura
/cast Devotion Aura
```

**Retribution Aura**

```
#showtooltip Retribution Aura
/cast Retribution Aura
```

**Concentration Aura**

```
#showtooltip Concentration Aura
/cast Concentration Aura
```

#### Panic / defensive

**Divine Shield**

```
#showtooltip Divine Shield
/cast Divine Shield
```

**Divine Protection**

```
#showtooltip Divine Protection
/cast Divine Protection
```

**Lay on Hands self**

```
#showtooltip Lay on Hands
/cast [@player] Lay on Hands
```

**Blessing of Protection self**

```
#showtooltip Blessing of Protection
/cast [@player] Blessing of Protection
```

#### Class QoL

**Seal of Righteousness**

```
#showtooltip Seal of Righteousness
/cast Seal of Righteousness
```

**Seal of the Crusader**

```
#showtooltip Seal of the Crusader
/cast Seal of the Crusader
```

**Seal of Wisdom**

```
#showtooltip Seal of Wisdom
/cast Seal of Wisdom
```

**Seal of Light**

```
#showtooltip Seal of Light
/cast Seal of Light
```

**Seal of Justice**

```
#showtooltip Seal of Justice
/cast Seal of Justice
```

**Judge + reseal Righteousness loop** — Press: seal, judge, seal, judge...

```
#showtooltip Seal of Righteousness
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Righteousness, Judgement
```

**Crusader opener, then Righteousness**

```
#showtooltip Seal of the Crusader
/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Righteousness
```

**Divine Intervention**

```
#showtooltip Divine Intervention
/cast [@mouseover, help, exists][help] Divine Intervention
```

#### Focus

**Hammer of Justice focus**

```
#showtooltip Hammer of Justice
/cast [@focus, harm, exists][harm] Hammer of Justice
```

**Turn Undead focus**

```
#showtooltip Turn Undead
/cast [@focus, harm, exists][harm] Turn Undead
```

### Paladin — Retribution

#### TT-aware DPS

**Repentance**

```
#showtooltip Repentance
/cast [@targettarget, harm, exists][harm] Repentance
```

#### Buffs

**Sanctity Aura**

```
#showtooltip Sanctity Aura
/cast Sanctity Aura
```

**Seal of Command**

```
#showtooltip Seal of Command
/cast Seal of Command
```

#### Class QoL

**Crusader opener, then Command**

```
#showtooltip Seal of the Crusader
/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Command
```

**Judge + reseal Command loop**

```
#showtooltip Seal of Command
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Command, Judgement
```

#### Focus

**Repentance focus**

```
#showtooltip Repentance
/cast [@focus, harm, exists][harm] Repentance
```

### Paladin — Protection

#### TT-aware DPS

**Holy Shield**

```
#showtooltip Holy Shield
/cast Holy Shield
```

#### Buffs

**Righteous Fury**

```
#showtooltip Righteous Fury
/cast Righteous Fury
```

**Blessing of Kings**

```
#showtooltip Blessing of Kings
/cast [@mouseover, help, exists][help][@player] Blessing of Kings
```

**Blessing of Sanctuary**

```
#showtooltip Blessing of Sanctuary
/cast [@mouseover, help, exists][help][@player] Blessing of Sanctuary
```

#### Class QoL

**Judge + reseal Wisdom loop** — Mana-sustain tanking.

```
#showtooltip Seal of Wisdom
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Wisdom, Judgement
```

## Warlock

### Warlock — Shared (all specs)

#### TT-aware DPS

**Shadow Bolt**

```
#showtooltip Shadow Bolt
/cast [@targettarget, harm, exists][harm] Shadow Bolt
```

**Corruption**

```
#showtooltip Corruption
/cast [@targettarget, harm, exists][harm] Corruption
```

**Curse of Agony**

```
#showtooltip Curse of Agony
/cast [@targettarget, harm, exists][harm] Curse of Agony
```

**Immolate**

```
#showtooltip Immolate
/cast [@targettarget, harm, exists][harm] Immolate
```

**Searing Pain**

```
#showtooltip Searing Pain
/cast [@targettarget, harm, exists][harm] Searing Pain
```

**Soul Fire**

```
#showtooltip Soul Fire
/cast [@targettarget, harm, exists][harm] Soul Fire
```

**Death Coil**

```
#showtooltip Death Coil
/cast [@targettarget, harm, exists][harm] Death Coil
```

**Drain Life (spam-safe)**

```
#showtooltip Drain Life
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Life
```

**Drain Soul (spam-safe)**

```
#showtooltip Drain Soul
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Soul
```

**Drain Mana (spam-safe)**

```
#showtooltip Drain Mana
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Mana
```

**Curse of the Elements**

```
#showtooltip Curse of the Elements
/cast [@targettarget, harm, exists][harm] Curse of the Elements
```

**Curse of Shadow**

```
#showtooltip Curse of Shadow
/cast [@targettarget, harm, exists][harm] Curse of Shadow
```

**Curse of Recklessness**

```
#showtooltip Curse of Recklessness
/cast [@targettarget, harm, exists][harm] Curse of Recklessness
```

**Curse of Weakness**

```
#showtooltip Curse of Weakness
/cast [@targettarget, harm, exists][harm] Curse of Weakness
```

**Curse of Tongues**

```
#showtooltip Curse of Tongues
/cast [@targettarget, harm, exists][harm] Curse of Tongues
```

**Hellfire**

```
#showtooltip Hellfire
/cast Hellfire
```

**Rain of Fire**

```
#showtooltip Rain of Fire
/cast Rain of Fire
```

#### Mouseover healing / utility

**Health Funnel (pet)**

```
#showtooltip Health Funnel
/cast Health Funnel
```

**Unending Breath**

```
#showtooltip Unending Breath
/cast [@mouseover, help, exists][help][@player] Unending Breath
```

**Detect Invisibility**

```
#showtooltip Detect Invisibility
/cast [@mouseover, help, exists][help][@player] Detect Invisibility
```

**Soulstone mouseover** — Swap item name to your soulstone rank.

```
/use [@mouseover, help, exists][help] Major Soulstone
```

#### Cleanse / dispel

**Devour Magic (Felhunter)**

```
#showtooltip Devour Magic
/cast [@mouseover, help, exists][help] Devour Magic
```

#### Wand / auto-attack

**Wand (spam-safe)**

```
#showtooltip Shoot
/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
/cast [harm, nochanneling:Shoot] Shoot
```

#### Buffs

**Demon Armor**

```
#showtooltip Demon Armor
/cast Demon Armor
```

**Shadow Ward**

```
#showtooltip Shadow Ward
/cast Shadow Ward
```

#### Panic / defensive

**Healthstone** — Swap item name to your healthstone rank.

```
/use Major Healthstone
```

**Howl of Terror**

```
#showtooltip Howl of Terror
/cast Howl of Terror
```

**Fear**

```
#showtooltip Fear
/cast [@targettarget, harm, exists][harm] Fear
```

**Sacrifice (Voidwalker)**

```
#showtooltip Sacrifice
/cast Sacrifice
```

**Life Tap**

```
#showtooltip Life Tap
/cast Life Tap
```

#### Class QoL

**Pet attack TT / target**

```
/petattack [@targettarget, harm, exists][harm]
```

**Pet follow**

```
/petfollow
```

**Pet passive**

```
/petpassive
```

**Pet defensive**

```
/petdefensive
```

**Spell Lock (Felhunter)**

```
#showtooltip Spell Lock
/cast [@targettarget, harm, exists][harm] Spell Lock
```

**Torment (Voidwalker taunt)**

```
#showtooltip Torment
/cast [@targettarget, harm, exists][harm] Torment
```

**Summon Felhunter**

```
#showtooltip Summon Felhunter
/cast Summon Felhunter
```

**Summon Voidwalker**

```
#showtooltip Summon Voidwalker
/cast Summon Voidwalker
```

**Summon Succubus**

```
#showtooltip Summon Succubus
/cast Summon Succubus
```

**Summon Imp**

```
#showtooltip Summon Imp
/cast Summon Imp
```

#### Focus

**Fear focus**

```
#showtooltip Fear
/cast [@focus, harm, exists][harm] Fear
```

**Banish focus**

```
#showtooltip Banish
/cast [@focus, harm, exists][harm] Banish
```

**Seduction focus**

```
#showtooltip Seduction
/cast [@focus, harm, exists][harm] Seduction
```

**Spell Lock focus**

```
#showtooltip Spell Lock
/cast [@focus, harm, exists][harm] Spell Lock
```

**Enslave Demon focus**

```
#showtooltip Enslave Demon
/cast [@focus, harm, exists][harm] Enslave Demon
```

### Warlock — Affliction

#### TT-aware DPS

**Siphon Life**

```
#showtooltip Siphon Life
/cast [@targettarget, harm, exists][harm] Siphon Life
```

**Curse of Exhaustion**

```
#showtooltip Curse of Exhaustion
/cast [@targettarget, harm, exists][harm] Curse of Exhaustion
```

**Amplify Curse + Agony**

```
#showtooltip Curse of Agony
/cast Amplify Curse
/cast [@targettarget, harm, exists][harm] Curse of Agony
```

**DoT sequence (press to roll dots)**

```
#showtooltip Corruption
/castsequence [@targettarget, harm, exists][harm] reset=target Corruption, Curse of Agony, Siphon Life, Immolate
```

#### Panic / defensive

**Dark Pact**

```
#showtooltip Dark Pact
/cast Dark Pact
```

### Warlock — Demonology

#### Class QoL

**Fel Domination + Felhunter**

```
#showtooltip Summon Felhunter
/cast Fel Domination
/cast Summon Felhunter
```

**Fel Domination + Voidwalker**

```
#showtooltip Summon Voidwalker
/cast Fel Domination
/cast Summon Voidwalker
```

**Soul Link**

```
#showtooltip Soul Link
/cast Soul Link
```

**Demonic Sacrifice**

```
#showtooltip Demonic Sacrifice
/cast Demonic Sacrifice
```

### Warlock — Destruction

#### TT-aware DPS

**Conflagrate**

```
#showtooltip Conflagrate
/cast [@targettarget, harm, exists][harm] Conflagrate
```

**Shadowburn**

```
#showtooltip Shadowburn
/cast [@targettarget, harm, exists][harm] Shadowburn
```

**Immolate > Conflagrate**

```
#showtooltip Immolate
/castsequence [@targettarget, harm, exists][harm] reset=target/10 Immolate, Conflagrate
```

## Hunter

### Hunter — Shared (all specs)

#### TT-aware DPS

**Hunter's Mark**

```
#showtooltip Hunter's Mark
/cast [@targettarget, harm, exists][harm] Hunter's Mark
```

**Serpent Sting**

```
#showtooltip Serpent Sting
/cast [@targettarget, harm, exists][harm] Serpent Sting
```

**Arcane Shot**

```
#showtooltip Arcane Shot
/cast [@targettarget, harm, exists][harm] Arcane Shot
```

**Multi-Shot**

```
#showtooltip Multi-Shot
/cast [@targettarget, harm, exists][harm] Multi-Shot
```

**Concussive Shot**

```
#showtooltip Concussive Shot
/cast [@targettarget, harm, exists][harm] Concussive Shot
```

**Viper Sting**

```
#showtooltip Viper Sting
/cast [@targettarget, harm, exists][harm] Viper Sting
```

**Scorpid Sting**

```
#showtooltip Scorpid Sting
/cast [@targettarget, harm, exists][harm] Scorpid Sting
```

**Raptor Strike**

```
#showtooltip Raptor Strike
/cast [@targettarget, harm, exists][harm] Raptor Strike
```

**Mongoose Bite**

```
#showtooltip Mongoose Bite
/cast [@targettarget, harm, exists][harm] Mongoose Bite
```

**Wing Clip**

```
#showtooltip Wing Clip
/cast [@targettarget, harm, exists][harm] Wing Clip
```

**Distracting Shot**

```
#showtooltip Distracting Shot
/cast [@targettarget, harm, exists][harm] Distracting Shot
```

**Tranquilizing Shot (enrage dispel)** — Hunter's only dispel: removes Frenzy from enemies.

```
#showtooltip Tranquilizing Shot
/cast [@targettarget, harm, exists][harm] Tranquilizing Shot
```

#### Cleanse / dispel

*Hunters have no friendly cleanse. Use Tranquilizing Shot (TT-aware DPS) instead.*

#### Wand / auto-attack

**Auto Shot (spam-safe)** — Hunter exception: ! stops Auto Shot toggling off. Unlike wand Shoot, it works here.

```
#showtooltip Auto Shot
/cast [@targettarget, harm, exists][harm] !Auto Shot
```

**Melee auto-attack**

```
/startattack [@targettarget, harm, exists][harm]
```

#### Buffs

**Aspect: Hawk in combat, Cheetah out**

```
#showtooltip Aspect of the Hawk
/cast [combat] Aspect of the Hawk; Aspect of the Cheetah
```

**Aspect of the Hawk**

```
#showtooltip Aspect of the Hawk
/cast Aspect of the Hawk
```

**Aspect of the Monkey**

```
#showtooltip Aspect of the Monkey
/cast Aspect of the Monkey
```

**Aspect of the Pack**

```
#showtooltip Aspect of the Pack
/cast Aspect of the Pack
```

**Aspect of the Wild**

```
#showtooltip Aspect of the Wild
/cast Aspect of the Wild
```

#### Panic / defensive

**Feign Death**

```
#showtooltip Feign Death
/cast Feign Death
```

**Disengage**

```
#showtooltip Disengage
/cast [@targettarget, harm, exists][harm] Disengage
```

**Freezing Trap**

```
#showtooltip Freezing Trap
/cast Freezing Trap
```

**Frost Trap**

```
#showtooltip Frost Trap
/cast Frost Trap
```

**Rapid Fire**

```
#showtooltip Rapid Fire
/cast Rapid Fire
```

#### Class QoL

**Pet attack TT / target**

```
/petattack [@targettarget, harm, exists][harm]
```

**Pet follow**

```
/petfollow
```

**Pet passive**

```
/petpassive
```

**Call / Revive / Mend (one button)**

```
#showtooltip Mend Pet
/cast [nopet] Call Pet; [@pet, dead] Revive Pet; Mend Pet
```

**Feed Pet** — Swap food item for your pet's diet.

```
#showtooltip Feed Pet
/cast Feed Pet
/use Tough Jerky
```

**Flare**

```
#showtooltip Flare
/cast Flare
```

**Explosive Trap**

```
#showtooltip Explosive Trap
/cast Explosive Trap
```

**Immolation Trap**

```
#showtooltip Immolation Trap
/cast Immolation Trap
```

#### Focus

**Hunter's Mark focus**

```
#showtooltip Hunter's Mark
/cast [@focus, harm, exists][harm] Hunter's Mark
```

**Concussive Shot focus**

```
#showtooltip Concussive Shot
/cast [@focus, harm, exists][harm] Concussive Shot
```

### Hunter — Beast Mastery

#### TT-aware DPS

**Bestial Wrath + Rapid Fire burst**

```
#showtooltip Bestial Wrath
/cast Bestial Wrath
/cast Rapid Fire
```

**Intimidation** — Pet's next hit stuns its target.

```
#showtooltip Intimidation
/cast Intimidation
```

### Hunter — Marksmanship

#### TT-aware DPS

**Aimed Shot**

```
#showtooltip Aimed Shot
/cast [@targettarget, harm, exists][harm] Aimed Shot
```

**Scatter Shot**

```
#showtooltip Scatter Shot
/cast [@targettarget, harm, exists][harm] Scatter Shot
```

#### Buffs

**Trueshot Aura**

```
#showtooltip Trueshot Aura
/cast Trueshot Aura
```

#### Focus

**Scatter Shot focus**

```
#showtooltip Scatter Shot
/cast [@focus, harm, exists][harm] Scatter Shot
```

### Hunter — Survival

#### TT-aware DPS

**Counterattack**

```
#showtooltip Counterattack
/cast [@targettarget, harm, exists][harm] Counterattack
```

**Wyvern Sting**

```
#showtooltip Wyvern Sting
/cast [@targettarget, harm, exists][harm] Wyvern Sting
```

#### Panic / defensive

**Deterrence**

```
#showtooltip Deterrence
/cast Deterrence
```

#### Focus

**Wyvern Sting focus**

```
#showtooltip Wyvern Sting
/cast [@focus, harm, exists][harm] Wyvern Sting
```

## Warrior

### Warrior — Shared (all specs)

#### TT-aware DPS

**Heroic Strike**

```
#showtooltip Heroic Strike
/cast [@targettarget, harm, exists][harm] Heroic Strike
```

**Cleave**

```
#showtooltip Cleave
/cast [@targettarget, harm, exists][harm] Cleave
```

**Rend**

```
#showtooltip Rend
/cast [@targettarget, harm, exists][harm] Rend
```

**Hamstring**

```
#showtooltip Hamstring
/cast [@targettarget, harm, exists][harm] Hamstring
```

**Sunder Armor**

```
#showtooltip Sunder Armor
/cast [@targettarget, harm, exists][harm] Sunder Armor
```

**Execute**

```
#showtooltip Execute
/cast [@targettarget, harm, exists][harm] Execute
```

**Overpower (to Battle)**

```
#showtooltip Overpower
/cast [nostance:1] Battle Stance; [@targettarget, harm, exists][harm] Overpower
```

**Demoralizing Shout**

```
#showtooltip Demoralizing Shout
/cast Demoralizing Shout
```

**Thunder Clap (to Battle)**

```
#showtooltip Thunder Clap
/cast [nostance:1] Battle Stance; Thunder Clap
```

#### Cleanse / dispel

*Warriors have no dispel. Interrupt instead with Pummel or Shield Bash.*

#### Wand / auto-attack

**Auto-attack (spam-safe)**

```
/startattack [@targettarget, harm, exists][harm]
```

#### Buffs

**Battle Shout**

```
#showtooltip Battle Shout
/cast Battle Shout
```

**Bloodrage**

```
#showtooltip Bloodrage
/cast Bloodrage
```

**Berserker Rage (to Berserker)**

```
#showtooltip Berserker Rage
/cast [nostance:3] Berserker Stance; Berserker Rage
```

#### Panic / defensive

**Shield Wall (to Defensive)**

```
#showtooltip Shield Wall
/cast [nostance:2] Defensive Stance; Shield Wall
```

**Retaliation (to Battle)**

```
#showtooltip Retaliation
/cast [nostance:1] Battle Stance; Retaliation
```

**Intimidating Shout**

```
#showtooltip Intimidating Shout
/cast [@targettarget, harm, exists][harm] Intimidating Shout
```

**Disarm (to Defensive)**

```
#showtooltip Disarm
/cast [nostance:2] Defensive Stance; [@targettarget, harm, exists][harm] Disarm
```

#### Class QoL

**Battle Stance**

```
#showtooltip Battle Stance
/cast Battle Stance
```

**Defensive Stance**

```
#showtooltip Defensive Stance
/cast Defensive Stance
```

**Berserker Stance**

```
#showtooltip Berserker Stance
/cast Berserker Stance
```

**Charge / Intercept (one button)** — Out of combat: Charge. In combat: Intercept. Stance swaps cost rage above your Tactical Mastery cap.

```
#showtooltip Charge
/cast [nocombat, nostance:1] Battle Stance; [nocombat, @targettarget, harm, exists][nocombat, harm] Charge; [nostance:3] Berserker Stance; [@targettarget, harm, exists][harm] Intercept
```

**Taunt (to Defensive)** — Target the friend being hit: TT is the mob.

```
#showtooltip Taunt
/cast [nostance:2] Defensive Stance; [@targettarget, harm, exists][harm] Taunt
```

**Mocking Blow (to Battle)**

```
#showtooltip Mocking Blow
/cast [nostance:1] Battle Stance; [@targettarget, harm, exists][harm] Mocking Blow
```

**Challenging Shout**

```
#showtooltip Challenging Shout
/cast Challenging Shout
```

#### Focus

**Pummel focus**

```
#showtooltip Pummel
/cast [nostance:3] Berserker Stance; [@focus, harm, exists][harm] Pummel
```

**Shield Bash focus**

```
#showtooltip Shield Bash
/cast [@focus, harm, exists][harm] Shield Bash
```

**Taunt focus**

```
#showtooltip Taunt
/cast [@focus, harm, exists][harm] Taunt
```

### Warrior — Fury

#### TT-aware DPS

**Bloodthirst**

```
#showtooltip Bloodthirst
/cast [@targettarget, harm, exists][harm] Bloodthirst
```

**Whirlwind (to Berserker)**

```
#showtooltip Whirlwind
/cast [nostance:3] Berserker Stance; Whirlwind
```

**Pummel (to Berserker)**

```
#showtooltip Pummel
/cast [nostance:3] Berserker Stance; [@targettarget, harm, exists][harm] Pummel
```

**Slam**

```
#showtooltip Slam
/cast [@targettarget, harm, exists][harm] Slam
```

**Piercing Howl**

```
#showtooltip Piercing Howl
/cast Piercing Howl
```

#### Buffs

**Death Wish**

```
#showtooltip Death Wish
/cast Death Wish
```

**Recklessness (to Berserker)**

```
#showtooltip Recklessness
/cast [nostance:3] Berserker Stance; Recklessness
```

### Warrior — Protection

#### TT-aware DPS

**Shield Slam**

```
#showtooltip Shield Slam
/cast [@targettarget, harm, exists][harm] Shield Slam
```

**Revenge**

```
#showtooltip Revenge
/cast [@targettarget, harm, exists][harm] Revenge
```

**Shield Bash**

```
#showtooltip Shield Bash
/cast [@targettarget, harm, exists][harm] Shield Bash
```

**Concussion Blow**

```
#showtooltip Concussion Blow
/cast [@targettarget, harm, exists][harm] Concussion Blow
```

#### Panic / defensive

**Shield Block**

```
#showtooltip Shield Block
/cast Shield Block
```

**Last Stand**

```
#showtooltip Last Stand
/cast Last Stand
```
