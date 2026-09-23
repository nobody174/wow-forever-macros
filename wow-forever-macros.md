# WoW Forever Macro Cheatsheet (nobody174 style)

Copy/paste macros for Priest, Shaman, Paladin, Warlock, Hunter and Warrior. Each class has a **Shared** section (every spec uses it) plus spec-only extras.

## Patterns

**TT-aware DPS**
```
/cast [@targettarget, harm, exists][harm] SPELL
```

**Mouseover heal / utility**
```
/cast [@mouseover, help, exists][help] SPELL
```

**Friend-or-foe (Dispel Magic)**
```
/cast [@mouseover, exists][exists] SPELL
```

**Buffs (adds self fallback)**
```
/cast [@mouseover, help, exists][help][@player] SPELL
```

**Spam-safe channel**
```
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] SPELL
```

**Wand**
```
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

## Priest

### Priest — Shared (all specs)

#### TT-aware DPS

**Shadow Word: Pain**

```
/cast [@targettarget, harm, exists][harm] Shadow Word: Pain
```

**Mind Blast**

```
/cast [@targettarget, harm, exists][harm] Mind Blast
```

**Smite**

```
/cast [@targettarget, harm, exists][harm] Smite
```

**Holy Fire**

```
/cast [@targettarget, harm, exists][harm] Holy Fire
```

**Mana Burn**

```
/cast [@targettarget, harm, exists][harm] Mana Burn
```

#### Mouseover healing / utility

**Flash Heal**

```
/cast [@mouseover, help, exists][help] Flash Heal
```

**Heal**

```
/cast [@mouseover, help, exists][help] Heal
```

**Greater Heal**

```
/cast [@mouseover, help, exists][help] Greater Heal
```

**Lesser Heal**

```
/cast [@mouseover, help, exists][help] Lesser Heal
```

**Renew**

```
/cast [@mouseover, help, exists][help] Renew
```

**Power Word: Shield**

```
/cast [@mouseover, help, exists][help] Power Word: Shield
```

**Prayer of Healing** — Party-wide, no target needed.

```
/cast Prayer of Healing
```

**Resurrection**

```
/cast [@mouseover, help, exists][help] Resurrection
```

#### Cleanse / dispel

**Dispel Magic (friend or foe)**

```
/cast [@mouseover, exists][exists] Dispel Magic
```

**Cure Disease**

```
/cast [@mouseover, help, exists][help] Cure Disease
```

**Abolish Disease**

```
/cast [@mouseover, help, exists][help] Abolish Disease
```

#### Wand / auto-attack

**Wand (spam-safe)**

```
/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
/cast [harm, nochanneling:Shoot] Shoot
```

#### Buffs

**Power Word: Fortitude**

```
/cast [@mouseover, help, exists][help][@player] Power Word: Fortitude
```

**Prayer of Fortitude**

```
/cast [@mouseover, help, exists][help][@player] Prayer of Fortitude
```

**Shadow Protection**

```
/cast [@mouseover, help, exists][help][@player] Shadow Protection
```

**Levitate**

```
/cast [@mouseover, help, exists][help][@player] Levitate
```

**Inner Fire**

```
/cast Inner Fire
```

**Fear Ward** — Racial/availability may differ in Forever.

```
/cast [@mouseover, help, exists][help][@player] Fear Ward
```

#### Panic / defensive

**Shield self**

```
/cast [@player] Power Word: Shield
```

**Psychic Scream**

```
/cast Psychic Scream
```

**Fade**

```
/cast Fade
```

**Desperate Prayer** — Racial priest spell.

```
/cast Desperate Prayer
```

#### Focus

**Shackle Undead on focus**

```
/cast [@focus, harm, exists][harm] Shackle Undead
```

**Mind Control on focus**

```
/cast [@focus, harm, exists][harm] Mind Control
```

### Priest — Shadow

#### TT-aware DPS

**Mind Flay (spam-safe)** — Won't clip an active channel.

```
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Mind Flay
```

**Vampiric Embrace**

```
/cast [@targettarget, harm, exists][harm] Vampiric Embrace
```

**Silence**

```
/cast [@targettarget, harm, exists][harm] Silence
```

**Devouring Plague** — Racial priest spell.

```
/cast [@targettarget, harm, exists][harm] Devouring Plague
```

#### Buffs

**Shadowform (no cancel)** — Won't drop you out of form if pressed again.

```
/cast [noform] Shadowform
```

#### Focus

**Silence focus**

```
/cast [@focus, harm, exists][harm] Silence
```

### Priest — Holy

#### Mouseover healing / utility

**Inner Focus + Greater Heal**

```
/cast Inner Focus
/cast [@mouseover, help, exists][help] Greater Heal
```

**Holy Nova**

```
/cast Holy Nova
```

**Lightwell**

```
/cast Lightwell
```

### Priest — Discipline

#### Mouseover healing / utility

**Power Infusion**

```
/cast [@mouseover, help, exists][help] Power Infusion
```

**Inner Focus + Greater Heal**

```
/cast Inner Focus
/cast [@mouseover, help, exists][help] Greater Heal
```

#### Buffs

**Divine Spirit**

```
/cast [@mouseover, help, exists][help][@player] Divine Spirit
```

## Shaman

### Shaman — Shared (all specs)

#### TT-aware DPS

**Lightning Bolt**

```
/cast [@targettarget, harm, exists][harm] Lightning Bolt
```

**Chain Lightning**

```
/cast [@targettarget, harm, exists][harm] Chain Lightning
```

**Earth Shock**

```
/cast [@targettarget, harm, exists][harm] Earth Shock
```

**Flame Shock**

```
/cast [@targettarget, harm, exists][harm] Flame Shock
```

**Frost Shock**

```
/cast [@targettarget, harm, exists][harm] Frost Shock
```

**Purge (offensive dispel)**

```
/cast [@targettarget, harm, exists][harm] Purge
```

#### Mouseover healing / utility

**Healing Wave**

```
/cast [@mouseover, help, exists][help] Healing Wave
```

**Lesser Healing Wave**

```
/cast [@mouseover, help, exists][help] Lesser Healing Wave
```

**Chain Heal**

```
/cast [@mouseover, help, exists][help] Chain Heal
```

**Ancestral Spirit**

```
/cast [@mouseover, help, exists][help] Ancestral Spirit
```

#### Cleanse / dispel

**Cure Poison**

```
/cast [@mouseover, help, exists][help] Cure Poison
```

**Cure Disease**

```
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
/cast Lightning Shield
```

**Rockbiter Weapon**

```
/cast Rockbiter Weapon
```

**Flametongue Weapon**

```
/cast Flametongue Weapon
```

**Frostbrand Weapon**

```
/cast Frostbrand Weapon
```

**Water Walking**

```
/cast [@mouseover, help, exists][help][@player] Water Walking
```

**Water Breathing**

```
/cast [@mouseover, help, exists][help][@player] Water Breathing
```

#### Panic / defensive

**Self Lesser Healing Wave**

```
/cast [@player] Lesser Healing Wave
```

**Stoneclaw Totem**

```
/cast Stoneclaw Totem
```

**Grounding Totem**

```
/cast Grounding Totem
```

**Ghost Wolf (no cancel)**

```
/cast [noform] Ghost Wolf
```

#### Class QoL

**Totems: melee group (press 4x)**

```
/castsequence reset=combat Strength of Earth Totem, Windfury Totem, Searing Totem, Mana Spring Totem
```

**Totems: caster group (press 4x)** — Swap Grace of Air for Tranquil Air if you prefer.

```
/castsequence reset=combat Stoneskin Totem, Grace of Air Totem, Searing Totem, Mana Spring Totem
```

**Tremor Totem**

```
/cast Tremor Totem
```

**Poison Cleansing Totem**

```
/cast Poison Cleansing Totem
```

**Disease Cleansing Totem**

```
/cast Disease Cleansing Totem
```

**Earthbind Totem**

```
/cast Earthbind Totem
```

**Magma Totem**

```
/cast Magma Totem
```

**Fire Nova Totem**

```
/cast Fire Nova Totem
```

**Healing Stream Totem**

```
/cast Healing Stream Totem
```

#### Focus

**Earth Shock interrupt on focus**

```
/cast [@focus, harm, exists][harm] Earth Shock
```

**Purge focus**

```
/cast [@focus, harm, exists][harm] Purge
```

### Shaman — Elemental

#### TT-aware DPS

**Elemental Mastery + Chain Lightning**

```
/cast Elemental Mastery
/cast [@targettarget, harm, exists][harm] Chain Lightning
```

**Elemental Mastery + Lightning Bolt**

```
/cast Elemental Mastery
/cast [@targettarget, harm, exists][harm] Lightning Bolt
```

### Shaman — Enhancement

#### TT-aware DPS

**Stormstrike** — Also starts auto-attack.

```
/cast [@targettarget, harm, exists][harm] Stormstrike
```

#### Buffs

**Windfury Weapon**

```
/cast Windfury Weapon
```

## Paladin

### Paladin — Shared (all specs)

#### TT-aware DPS

**Judgement**

```
/cast [@targettarget, harm, exists][harm] Judgement
```

**Hammer of Wrath**

```
/cast [@targettarget, harm, exists][harm] Hammer of Wrath
```

**Exorcism**

```
/cast [@targettarget, harm, exists][harm] Exorcism
```

**Hammer of Justice**

```
/cast [@targettarget, harm, exists][harm] Hammer of Justice
```

**Consecration**

```
/cast Consecration
```

**Holy Wrath**

```
/cast Holy Wrath
```

#### Mouseover healing / utility

**Holy Light**

```
/cast [@mouseover, help, exists][help] Holy Light
```

**Flash of Light**

```
/cast [@mouseover, help, exists][help] Flash of Light
```

**Lay on Hands**

```
/cast [@mouseover, help, exists][help] Lay on Hands
```

**Blessing of Protection**

```
/cast [@mouseover, help, exists][help] Blessing of Protection
```

**Blessing of Freedom**

```
/cast [@mouseover, help, exists][help] Blessing of Freedom
```

**Redemption**

```
/cast [@mouseover, help, exists][help] Redemption
```

#### Cleanse / dispel

**Cleanse**

```
/cast [@mouseover, help, exists][help] Cleanse
```

**Purify**

```
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
/cast [@mouseover, help, exists][help][@player] Blessing of Might
```

**Blessing of Wisdom**

```
/cast [@mouseover, help, exists][help][@player] Blessing of Wisdom
```

**Blessing of Salvation**

```
/cast [@mouseover, help, exists][help][@player] Blessing of Salvation
```

**Blessing of Light**

```
/cast [@mouseover, help, exists][help][@player] Blessing of Light
```

**Greater Blessing of Might**

```
/cast [@mouseover, help, exists][help][@player] Greater Blessing of Might
```

**Greater Blessing of Wisdom**

```
/cast [@mouseover, help, exists][help][@player] Greater Blessing of Wisdom
```

**Devotion Aura**

```
/cast Devotion Aura
```

**Retribution Aura**

```
/cast Retribution Aura
```

**Concentration Aura**

```
/cast Concentration Aura
```

#### Panic / defensive

**Divine Shield**

```
/cast Divine Shield
```

**Divine Protection**

```
/cast Divine Protection
```

**Lay on Hands self**

```
/cast [@player] Lay on Hands
```

**Blessing of Protection self**

```
/cast [@player] Blessing of Protection
```

#### Class QoL

**Seal of Righteousness**

```
/cast Seal of Righteousness
```

**Seal of the Crusader**

```
/cast Seal of the Crusader
```

**Seal of Wisdom**

```
/cast Seal of Wisdom
```

**Seal of Light**

```
/cast Seal of Light
```

**Seal of Justice**

```
/cast Seal of Justice
```

**Judge + reseal Righteousness loop** — Press: seal, judge, seal, judge...

```
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Righteousness, Judgement
```

**Crusader opener, then Righteousness**

```
/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Righteousness
```

**Divine Intervention**

```
/cast [@mouseover, help, exists][help] Divine Intervention
```

#### Focus

**Hammer of Justice focus**

```
/cast [@focus, harm, exists][harm] Hammer of Justice
```

**Turn Undead focus**

```
/cast [@focus, harm, exists][harm] Turn Undead
```

### Paladin — Retribution

#### TT-aware DPS

**Repentance**

```
/cast [@targettarget, harm, exists][harm] Repentance
```

#### Buffs

**Sanctity Aura**

```
/cast Sanctity Aura
```

**Seal of Command**

```
/cast Seal of Command
```

#### Class QoL

**Crusader opener, then Command**

```
/castsequence [@targettarget, harm, exists][harm] reset=target Seal of the Crusader, Judgement, Seal of Command
```

**Judge + reseal Command loop**

```
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Command, Judgement
```

#### Focus

**Repentance focus**

```
/cast [@focus, harm, exists][harm] Repentance
```

### Paladin — Protection

#### TT-aware DPS

**Holy Shield**

```
/cast Holy Shield
```

#### Buffs

**Righteous Fury**

```
/cast Righteous Fury
```

**Blessing of Kings**

```
/cast [@mouseover, help, exists][help][@player] Blessing of Kings
```

**Blessing of Sanctuary**

```
/cast [@mouseover, help, exists][help][@player] Blessing of Sanctuary
```

#### Class QoL

**Judge + reseal Wisdom loop** — Mana-sustain tanking.

```
/castsequence [@targettarget, harm, exists][harm] reset=combat Seal of Wisdom, Judgement
```

## Warlock

### Warlock — Shared (all specs)

#### TT-aware DPS

**Shadow Bolt**

```
/cast [@targettarget, harm, exists][harm] Shadow Bolt
```

**Corruption**

```
/cast [@targettarget, harm, exists][harm] Corruption
```

**Curse of Agony**

```
/cast [@targettarget, harm, exists][harm] Curse of Agony
```

**Immolate**

```
/cast [@targettarget, harm, exists][harm] Immolate
```

**Searing Pain**

```
/cast [@targettarget, harm, exists][harm] Searing Pain
```

**Soul Fire**

```
/cast [@targettarget, harm, exists][harm] Soul Fire
```

**Death Coil**

```
/cast [@targettarget, harm, exists][harm] Death Coil
```

**Drain Life (spam-safe)**

```
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Life
```

**Drain Soul (spam-safe)**

```
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Soul
```

**Drain Mana (spam-safe)**

```
/cast [@targettarget, harm, exists, nochanneling][harm, nochanneling] Drain Mana
```

**Curse of the Elements**

```
/cast [@targettarget, harm, exists][harm] Curse of the Elements
```

**Curse of Shadow**

```
/cast [@targettarget, harm, exists][harm] Curse of Shadow
```

**Curse of Recklessness**

```
/cast [@targettarget, harm, exists][harm] Curse of Recklessness
```

**Curse of Weakness**

```
/cast [@targettarget, harm, exists][harm] Curse of Weakness
```

**Curse of Tongues**

```
/cast [@targettarget, harm, exists][harm] Curse of Tongues
```

**Hellfire**

```
/cast Hellfire
```

**Rain of Fire**

```
/cast Rain of Fire
```

#### Mouseover healing / utility

**Health Funnel (pet)**

```
/cast Health Funnel
```

**Unending Breath**

```
/cast [@mouseover, help, exists][help][@player] Unending Breath
```

**Detect Invisibility**

```
/cast [@mouseover, help, exists][help][@player] Detect Invisibility
```

**Soulstone mouseover** — Swap item name to your soulstone rank.

```
/use [@mouseover, help, exists][help] Major Soulstone
```

#### Cleanse / dispel

**Devour Magic (Felhunter)**

```
/cast [@mouseover, help, exists][help] Devour Magic
```

#### Wand / auto-attack

**Wand (spam-safe)**

```
/cast [@targettarget, harm, exists, nochanneling:Shoot] Shoot
/cast [harm, nochanneling:Shoot] Shoot
```

#### Buffs

**Demon Armor**

```
/cast Demon Armor
```

**Shadow Ward**

```
/cast Shadow Ward
```

#### Panic / defensive

**Healthstone** — Swap item name to your healthstone rank.

```
/use Major Healthstone
```

**Howl of Terror**

```
/cast Howl of Terror
```

**Fear**

```
/cast [@targettarget, harm, exists][harm] Fear
```

**Sacrifice (Voidwalker)**

```
/cast Sacrifice
```

**Life Tap**

```
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
/cast [@targettarget, harm, exists][harm] Spell Lock
```

**Torment (Voidwalker taunt)**

```
/cast [@targettarget, harm, exists][harm] Torment
```

**Summon Felhunter**

```
/cast Summon Felhunter
```

**Summon Voidwalker**

```
/cast Summon Voidwalker
```

**Summon Succubus**

```
/cast Summon Succubus
```

**Summon Imp**

```
/cast Summon Imp
```

#### Focus

**Fear focus**

```
/cast [@focus, harm, exists][harm] Fear
```

**Banish focus**

```
/cast [@focus, harm, exists][harm] Banish
```

**Seduction focus**

```
/cast [@focus, harm, exists][harm] Seduction
```

**Spell Lock focus**

```
/cast [@focus, harm, exists][harm] Spell Lock
```

**Enslave Demon focus**

```
/cast [@focus, harm, exists][harm] Enslave Demon
```

### Warlock — Affliction

#### TT-aware DPS

**Siphon Life**

```
/cast [@targettarget, harm, exists][harm] Siphon Life
```

**Curse of Exhaustion**

```
/cast [@targettarget, harm, exists][harm] Curse of Exhaustion
```

**Amplify Curse + Agony**

```
/cast Amplify Curse
/cast [@targettarget, harm, exists][harm] Curse of Agony
```

**DoT sequence (press to roll dots)**

```
/castsequence [@targettarget, harm, exists][harm] reset=target Corruption, Curse of Agony, Siphon Life, Immolate
```

#### Panic / defensive

**Dark Pact**

```
/cast Dark Pact
```

### Warlock — Demonology

#### Class QoL

**Fel Domination + Felhunter**

```
/cast Fel Domination
/cast Summon Felhunter
```

**Fel Domination + Voidwalker**

```
/cast Fel Domination
/cast Summon Voidwalker
```

**Soul Link**

```
/cast Soul Link
```

**Demonic Sacrifice**

```
/cast Demonic Sacrifice
```

### Warlock — Destruction

#### TT-aware DPS

**Conflagrate**

```
/cast [@targettarget, harm, exists][harm] Conflagrate
```

**Shadowburn**

```
/cast [@targettarget, harm, exists][harm] Shadowburn
```

**Immolate > Conflagrate**

```
/castsequence [@targettarget, harm, exists][harm] reset=target/10 Immolate, Conflagrate
```

## Hunter

### Hunter — Shared (all specs)

#### TT-aware DPS

**Hunter's Mark**

```
/cast [@targettarget, harm, exists][harm] Hunter's Mark
```

**Serpent Sting**

```
/cast [@targettarget, harm, exists][harm] Serpent Sting
```

**Arcane Shot**

```
/cast [@targettarget, harm, exists][harm] Arcane Shot
```

**Multi-Shot**

```
/cast [@targettarget, harm, exists][harm] Multi-Shot
```

**Concussive Shot**

```
/cast [@targettarget, harm, exists][harm] Concussive Shot
```

**Viper Sting**

```
/cast [@targettarget, harm, exists][harm] Viper Sting
```

**Scorpid Sting**

```
/cast [@targettarget, harm, exists][harm] Scorpid Sting
```

**Raptor Strike**

```
/cast [@targettarget, harm, exists][harm] Raptor Strike
```

**Mongoose Bite**

```
/cast [@targettarget, harm, exists][harm] Mongoose Bite
```

**Wing Clip**

```
/cast [@targettarget, harm, exists][harm] Wing Clip
```

**Distracting Shot**

```
/cast [@targettarget, harm, exists][harm] Distracting Shot
```

**Tranquilizing Shot (enrage dispel)** — Hunter's only dispel: removes Frenzy from enemies.

```
/cast [@targettarget, harm, exists][harm] Tranquilizing Shot
```

#### Cleanse / dispel

*Hunters have no friendly cleanse. Use Tranquilizing Shot (TT-aware DPS) instead.*

#### Wand / auto-attack

**Auto Shot (spam-safe)** — Hunter exception: ! stops Auto Shot toggling off. Unlike wand Shoot, it works here.

```
/cast [@targettarget, harm, exists][harm] !Auto Shot
```

**Melee auto-attack**

```
/startattack [@targettarget, harm, exists][harm]
```

#### Buffs

**Aspect: Hawk in combat, Cheetah out**

```
/cast [combat] Aspect of the Hawk; Aspect of the Cheetah
```

**Aspect of the Hawk**

```
/cast Aspect of the Hawk
```

**Aspect of the Monkey**

```
/cast Aspect of the Monkey
```

**Aspect of the Pack**

```
/cast Aspect of the Pack
```

**Aspect of the Wild**

```
/cast Aspect of the Wild
```

#### Panic / defensive

**Feign Death**

```
/cast Feign Death
```

**Disengage**

```
/cast [@targettarget, harm, exists][harm] Disengage
```

**Freezing Trap**

```
/cast Freezing Trap
```

**Frost Trap**

```
/cast Frost Trap
```

**Rapid Fire**

```
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
/cast [nopet] Call Pet; [@pet, dead] Revive Pet; Mend Pet
```

**Feed Pet** — Swap food item for your pet's diet.

```
/cast Feed Pet
/use Tough Jerky
```

**Flare**

```
/cast Flare
```

**Explosive Trap**

```
/cast Explosive Trap
```

**Immolation Trap**

```
/cast Immolation Trap
```

#### Focus

**Hunter's Mark focus**

```
/cast [@focus, harm, exists][harm] Hunter's Mark
```

**Concussive Shot focus**

```
/cast [@focus, harm, exists][harm] Concussive Shot
```

### Hunter — Beast Mastery

#### TT-aware DPS

**Bestial Wrath + Rapid Fire burst**

```
/cast Bestial Wrath
/cast Rapid Fire
```

**Intimidation** — Pet's next hit stuns its target.

```
/cast Intimidation
```

### Hunter — Marksmanship

#### TT-aware DPS

**Aimed Shot**

```
/cast [@targettarget, harm, exists][harm] Aimed Shot
```

**Scatter Shot**

```
/cast [@targettarget, harm, exists][harm] Scatter Shot
```

#### Buffs

**Trueshot Aura**

```
/cast Trueshot Aura
```

#### Focus

**Scatter Shot focus**

```
/cast [@focus, harm, exists][harm] Scatter Shot
```

### Hunter — Survival

#### TT-aware DPS

**Counterattack**

```
/cast [@targettarget, harm, exists][harm] Counterattack
```

**Wyvern Sting**

```
/cast [@targettarget, harm, exists][harm] Wyvern Sting
```

#### Panic / defensive

**Deterrence**

```
/cast Deterrence
```

#### Focus

**Wyvern Sting focus**

```
/cast [@focus, harm, exists][harm] Wyvern Sting
```

## Warrior

### Warrior — Shared (all specs)

#### TT-aware DPS

**Heroic Strike**

```
/cast [@targettarget, harm, exists][harm] Heroic Strike
```

**Cleave**

```
/cast [@targettarget, harm, exists][harm] Cleave
```

**Rend**

```
/cast [@targettarget, harm, exists][harm] Rend
```

**Hamstring**

```
/cast [@targettarget, harm, exists][harm] Hamstring
```

**Sunder Armor**

```
/cast [@targettarget, harm, exists][harm] Sunder Armor
```

**Execute**

```
/cast [@targettarget, harm, exists][harm] Execute
```

**Overpower (to Battle)**

```
/cast [nostance:1] Battle Stance; [@targettarget, harm, exists][harm] Overpower
```

**Demoralizing Shout**

```
/cast Demoralizing Shout
```

**Thunder Clap (to Battle)**

```
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
/cast Battle Shout
```

**Bloodrage**

```
/cast Bloodrage
```

**Berserker Rage (to Berserker)**

```
/cast [nostance:3] Berserker Stance; Berserker Rage
```

#### Panic / defensive

**Shield Wall (to Defensive)**

```
/cast [nostance:2] Defensive Stance; Shield Wall
```

**Retaliation (to Battle)**

```
/cast [nostance:1] Battle Stance; Retaliation
```

**Intimidating Shout**

```
/cast [@targettarget, harm, exists][harm] Intimidating Shout
```

**Disarm (to Defensive)**

```
/cast [nostance:2] Defensive Stance; [@targettarget, harm, exists][harm] Disarm
```

#### Class QoL

**Battle Stance**

```
/cast Battle Stance
```

**Defensive Stance**

```
/cast Defensive Stance
```

**Berserker Stance**

```
/cast Berserker Stance
```

**Charge / Intercept (one button)** — Out of combat: Charge. In combat: Intercept. Stance swaps cost rage above your Tactical Mastery cap.

```
/cast [nocombat, nostance:1] Battle Stance; [nocombat, @targettarget, harm, exists][nocombat, harm] Charge; [nostance:3] Berserker Stance; [@targettarget, harm, exists][harm] Intercept
```

**Taunt (to Defensive)** — Target the friend being hit: TT is the mob.

```
/cast [nostance:2] Defensive Stance; [@targettarget, harm, exists][harm] Taunt
```

**Mocking Blow (to Battle)**

```
/cast [nostance:1] Battle Stance; [@targettarget, harm, exists][harm] Mocking Blow
```

**Challenging Shout**

```
/cast Challenging Shout
```

#### Focus

**Pummel focus**

```
/cast [nostance:3] Berserker Stance; [@focus, harm, exists][harm] Pummel
```

**Shield Bash focus**

```
/cast [@focus, harm, exists][harm] Shield Bash
```

**Taunt focus**

```
/cast [@focus, harm, exists][harm] Taunt
```

### Warrior — Fury

#### TT-aware DPS

**Bloodthirst**

```
/cast [@targettarget, harm, exists][harm] Bloodthirst
```

**Whirlwind (to Berserker)**

```
/cast [nostance:3] Berserker Stance; Whirlwind
```

**Pummel (to Berserker)**

```
/cast [nostance:3] Berserker Stance; [@targettarget, harm, exists][harm] Pummel
```

**Slam**

```
/cast [@targettarget, harm, exists][harm] Slam
```

**Piercing Howl**

```
/cast Piercing Howl
```

#### Buffs

**Death Wish**

```
/cast Death Wish
```

**Recklessness (to Berserker)**

```
/cast [nostance:3] Berserker Stance; Recklessness
```

### Warrior — Protection

#### TT-aware DPS

**Shield Slam**

```
/cast [@targettarget, harm, exists][harm] Shield Slam
```

**Revenge**

```
/cast [@targettarget, harm, exists][harm] Revenge
```

**Shield Bash**

```
/cast [@targettarget, harm, exists][harm] Shield Bash
```

**Concussion Blow**

```
/cast [@targettarget, harm, exists][harm] Concussion Blow
```

#### Panic / defensive

**Shield Block**

```
/cast Shield Block
```

**Last Stand**

```
/cast Last Stand
```
