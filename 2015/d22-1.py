import copy, math

spells = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229,
}

def simulate(player: dict, boss: dict):
    options = [player_turn(copy.deepcopy(player), copy.deepcopy(boss), spell) for spell in spells if spells[spell] <= player['mp']]
    if len(options) == 0:
        return math.inf
    return min(options)

def player_turn(player, boss, spell):
    # if spell in player['eff']:
    #     return math.inf
    player['mp'] -= spells[spell]
    player['spent'] += spells[spell]
    if player['spent'] > 10_000:
        return math.inf
    if 'Recharge' in player['eff']:
        player['mp'] += 101
    dec_effects(player['eff'])
    if spell == 'Magic Missile':
        boss['hp'] -= 4
    elif spell == 'Drain':
        player['hp'] += 2
        boss['hp'] -= 2
    elif spell == 'Shield':
        player['eff']['Shield'] = 6
    elif spell == 'Poison':
        player['eff']['Poison'] = 6
    elif spell == 'Recharge':
        player['eff']['Recharge'] = 5
    if boss['hp'] <= 0:
        print("grrrr")
        return player['spent']
    return boss_turn(player, boss)

def boss_turn(player, boss):
    if 'Recharge' in player['eff']:
        player['mp'] += 101
    damage = boss['damage']
    if 'Shield' in player['eff']:
        damage -= 7
    if 'Poison' in player['eff']:
        boss['hp'] -= 3
    player['hp'] -= damage
    if player['hp'] <= 0:
        return math.inf
    dec_effects(player['eff'])
    return(simulate(player, boss))

def dec_effects(effects: dict):
    rem = []
    for effect in effects:
        effects[effect] -= 1
        if effects[effect] == 0:
            rem.append(effect)
    for r in rem:
        effects.pop(r)

player = {
    'hp': 50,
    'mp': 500,
    'eff': {},
    'spent': 0,
}
    
boss = {
    'hp': 71,
    'damage': 10,
}

print(simulate(player, boss))