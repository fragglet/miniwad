#!/usr/bin/env python

import deh9000
import shutil

# Monsters without MF_COUNTKILL:
MONSTERS = (
	deh9000.MT_BOSSBRAIN,
	deh9000.MT_SKULL,
)

WEAPONS = (
	deh9000.MT_SHOTGUN,
	deh9000.MT_SUPERSHOTGUN,
	deh9000.MT_CHAINGUN,
	deh9000.MT_MISC25, # bfg
	deh9000.MT_MISC26, # csaw
	deh9000.MT_MISC27, # RL
	deh9000.MT_MISC28, # plasma
)

frames = ["empty"] * len(deh9000.states)

def sprite_name(state):
	name = deh9000.sprnames[state.sprite]
	return name + "ABCDEFGHIJKLMNOPQRSTUVWXYZ[^]"[state.frame & 0xff] + "0"

def handle_weapon(mobj):
	for state_id in deh9000.states.walk(mobj.spawnstate):
		frames[state_id] = "weapon"

def handle_pickup(mobj):
	for state_id in deh9000.states.walk(mobj.spawnstate):
		frames[state_id] = "item"

def handle_monster(mobj):
	for field in ("meleestate", "missilestate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "monster_fire"
	for field in ("deathstate", "xdeathstate", "raisestate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "corpse"
	for field in ("spawnstate", "seestate", "painstate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "monster"

def handle_player(mobj):
	for field in ("meleestate", "missilestate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "player_fire"
	for field in ("deathstate", "xdeathstate", "raisestate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "corpse"
	for field in ("spawnstate", "seestate", "painstate"):
		for state_id in deh9000.states.walk(getattr(mobj, field)):
			frames[state_id] = "player"

def handle_projectile(mobj):
	for state_id in deh9000.states.walk(mobj.spawnstate):
		frames[state_id] = "projectile"

def handle_obstacle(mobj):
	for state_id in deh9000.states.walk(mobj.spawnstate):
		frames[state_id] = "obstacle"

for mobj_id, mobj in enumerate(deh9000.mobjinfo):
	if mobj_id in WEAPONS:
		handle_weapon(mobj)
	elif mobj.flags & deh9000.MF_SPECIAL:
		handle_pickup(mobj)
	elif mobj_id in MONSTERS or (mobj.flags & deh9000.MF_COUNTKILL):
		handle_monster(mobj)
	elif mobj.flags & deh9000.MF_MISSILE:
		handle_projectile(mobj)
	elif mobj.flags & deh9000.MF_SOLID:
		handle_obstacle(mobj)

handle_player(deh9000.mobjinfo[deh9000.MT_PLAYER])

for weapon_id, weapon in enumerate(deh9000.weaponinfo):
	for state_id in deh9000.states.walk(weapon.flashstate):
		frames[state_id] = "gunflash"
	for field in ("upstate", "downstate", "readystate", "atkstate"):
		for state_id in deh9000.states.walk(getattr(weapon, field)):
			frames[state_id] = "gun"

wadinfo_names = set()

for state_id, state in enumerate(deh9000.states):
	template = frames[state_id]
	name = sprite_name(state).lower()
	#print("state %d: %s -> %s" % (state_id, template, name))
	if template != "empty":
		shutil.copy(template + ".png", "../%s.png" % name)
	wadinfo_names.add(name)

for name in sorted(wadinfo_names):
	print(name)

