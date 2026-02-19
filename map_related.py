def world_settings(map_x=5, map_y=10):
    """Generate map"""
    generate_map = [[" "] * map_y for _ in range(map_x)]
    return generate_map

def move_table(action):
    """Tables used for alternative button"""
    moveset = {
    "w" : [-1,0],
    "a" : [0,-1],
    "d" : [0,1],
    "s" : [1,0],
    "q" : 0,
    }
    return moveset[action]

def populate_map(map, enemies):
    x_dimension = len(map[0])
    y_dimension = len(map)
    print(f'x:{x_dimension}\ny:{y_dimension}')
    map[0][3] = "H"
    for i in range(y_dimension):
        print(map[i])
    pass