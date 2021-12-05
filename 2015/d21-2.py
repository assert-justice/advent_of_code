def simulate(player, boss):
    player = player.copy()
    boss = boss.copy()
    turn = 0
    while True:
        turn += 1
        #print('turn:', turn)
        damage = player['damage'] - boss['armor']
        if damage < 1:
            damage = 1
        boss['hp'] -= damage
        if boss['hp'] <= 0:
            return True
        damage = boss['damage'] - player['armor']
        if damage < 1:
            damage = 1
        player['hp'] -= damage
        if player['hp'] <= 0:
            return False

boss = {
    'hp': 100,
    'damage': 8,
    'armor': 2,
}

player = {
    'hp': 100,
    'damage': 10,
    'armor': 0,
}

# player wins if they have 7 armor and >= 1 damage
# unarmored player dies on the 13th turn
# player wins if they have 10 damage and >= 0 armor

# while player['damage'] > 0:
#     sim = simulate(player, boss)
#     if sim:
#         print( (player['damage'], player['armor'],) )
#         player['damage'] -= 1
#     else:
#         player['armor'] += 1

# (10, 0)
# (9, 1)
# (8, 2)
# (7, 3)
# (6, 4)
# (5, 5)
# (4, 6)
# (1, 7)

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

weapons = [
    ( 8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
]

armors = [
    (  0, 0, 0),
    ( 13, 0, 1),
    ( 31, 0, 2),
    ( 53, 0, 3),
    ( 75, 0, 4),
    (102, 0, 5),
]

rings = [
    (  0, 0, 0),
    (  0, 0, 0),
    ( 25, 1, 0),
    ( 50, 2, 0),
    (100, 3, 0),
    ( 20, 0, 1),
    ( 40, 0, 2),
    ( 80, 0, 3),
]

targets = [
    (10, 0),
    (9, 1),
    (8, 2),
    (7, 3),
    (6, 4),
    (5, 5),
    (4, 6),
    (1, 7),
]

max_cost = 0
defen = 0
dam = 0
for weapon in weapons:
    for armor in armors:
        for i in range(len(rings)):
            for f in range(len(rings) - 1):
                if f == i:
                    f = len(rings) - 1
                damage = weapon[1] + rings[i][1] + rings[f][1]
                defense = armor[2] + rings[i][2] + rings[f][2]
                cost = weapon[0] + armor[0] + rings[i][0] + rings[f][0]
                for target in targets:
                    player['damage'] = damage
                    player['armor'] = defense
                    if not simulate(player, boss):
                        if  cost > max_cost:
                            max_cost = cost
                            defen = defense
                            dam = damage
                    # if damage < target[0] or defense < target[1]:
                    #     if  cost > max_cost:
                    #         max_cost = cost
                    #         defen = defense
                    #         dam = damage
print(max_cost, dam, defen)
# 326 is too high