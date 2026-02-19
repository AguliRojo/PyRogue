import map_related


def main_loop():
    world = map_related.world_settings(10, 5)
    map_related.populate_map(world,2)
    move = 1
    while move !=0:
        action = input("Your move:")
        move = map_related.move_table(action)
        print(move)

main_loop()
