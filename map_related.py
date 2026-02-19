import random


def world_settings(map_x=5, map_y=10):
    """Generate map"""
    generate_map = [[" "] * map_x for _ in range(map_y)]
    return generate_map


def move_table(action):
    """Tables used for alternative button"""
    moveset = {
        "w": [-1, 0],
        "a": [0, -1],
        "d": [0, 1],
        "s": [1, 0],
        "q": 0,
    }
    return moveset[action]


def populate_map(world_map, enemies):
    """Add enemies, hero.
    Show map(temporarily to prevent overuse of calling same function)
    """
    collumns = len(world_map[0])  # x
    rows = len(world_map)  # y
    print(f'Map dimensions:\nx:{collumns}\ny:{rows}')
    # hero generation
    generate_hero = random.randint(0, collumns * rows - 1)
    world_map[generate_hero // collumns][generate_hero % collumns] = "H"
    print(f'Hero generated in: x:{generate_hero % collumns + 1}, y:{generate_hero // collumns}')
    enemy_count = 0
    while enemy_count < enemies:
        # check if enemy is actually generated
        for x in range(enemies):
            # simplification: use number, divide and modulo
            generate_enemy = random.randint(0, collumns * rows - 1)
            row = generate_enemy // collumns
            col = generate_enemy % collumns
            if world_map[row][col] == ' ':
                # is field occupied?
                print(f'Enemy generated in: x:{col + 1}, y:{row + 1}')
                world_map[row][col] = "E"
                enemy_count += 1
    for i in range(rows):
        print(world_map[i])
    return map
