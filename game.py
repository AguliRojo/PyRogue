import random

# Player default values
class player_data:
    base_player_health = 50
    base_player_attack = 5
    default_name = "Adam"

class Player:
    def __init__(self, name=player_data.default_name, health=player_data.base_player_health, attack=player_data.base_player_attack):
        self.name = name
        self.health = health
        self.attack = attack

    def your_name(self):
        return f"Your name is {self.name}"

    @staticmethod
    def get_name(self):
        return


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    GRAY = "\033[90m"
    RESET = "\033[0m"


class MapTiles:
    hero = Colors.GREEN + "H" + Colors.RESET
    enemy = Colors.RED + "E" + Colors.RESET
    floor_tile = Colors.GRAY + "F" + Colors.RESET
    treasure = Colors.YELLOW + "T" + Colors.RESET


def colorize(cell):
    """Adds ANSI escape keys for color tiling"""
    if cell == "F":
        return MapTiles.floor_tile  # gray
    elif cell == "H":
        return MapTiles.hero  # green
    elif cell == "E":
        return MapTiles.enemy  # red
    else:
        return str(cell)

def generate_enemy():  # laziest way
    enemy_coordinates = [random.randint(0, len(world_map_dimensions) - 1),
                         random.randint(0, len(world_map_dimensions[0]) - 1)]
    while enemy_coordinates == hero_coordinates:
        enemy_coordinates = [random.randint(0, len(world_map_dimensions) - 1),
                             random.randint(0, len(world_map_dimensions[0]) - 1)]
    return enemy_coordinates

def generate_map():
    world_map_dimensions[hero_coordinates[0]][hero_coordinates[1]] = MapTiles.hero
    world_map_dimensions[enemy_coordinates[0]][enemy_coordinates[1]] = MapTiles.enemy
    return world_map_dimensions


def display_map():
    """Function to generate map. Ensures that generated map values are not written over"""
    world_map = generate_map()
    for row in world_map:
        print(" ".join(colorize(cell) for cell in row))
    return world_map



# Initialize a 5x6 grid with independent values.
sizeof_map_x = 5
sizeof_map_y = 6
world_map_dimensions = [[MapTiles.floor_tile] * sizeof_map_x for _ in range(sizeof_map_y)]
hero_coordinates = [random.randint(0, len(world_map_dimensions) - 1),
                        random.randint(0, len(world_map_dimensions[0]) - 1)]
enemy_coordinates = generate_enemy()

def move_table():
    """Tables used for alternative button"""
    moveset = {
    "w" : [-1,0],
    "a" : [0,-1],
    "d" : [0,1],
    "s" : [1,0],
    "q" : "q",
    }
    return moveset

def move_action(action):
    # hero_location = world_map_dimensions[hero_coordinates[0]][hero_coordinates[1]]
    # print(f'{MapTiles.hero} - hero location\n{hero_coordinates[0]+1} - x\n{hero_coordinates[1]+1} - y')
    if action in move_table():
        # print(move_table())
        dx, dy = move_table()[action]
        print(f'Before move:\nx: {hero_coordinates[1]}, y:{hero_coordinates[0]}')
        hero_coordinates[0] += dx
        hero_coordinates[1] += dy
        print(f'After move:\nx: {hero_coordinates[1]}, y:{hero_coordinates[0]}')
        # if hit a wall return message and don't change positions
        # TODO: display_map() returns map generation, and doesnt have rules so you can call -1 x axis
        #       But you can't call out of bounds so bigger/less than -+len() crashes
        if hero_coordinates[0] < 0 or hero_coordinates[0] > sizeof_map_y:
            # y lock
            hero_coordinates[0] -= dx
            hero_coordinates[1] -= dy
            print("Invalid move, you've hit a wall")
        if hero_coordinates[1] < 0 or hero_coordinates[1] > sizeof_map_x:
            # x lock
            hero_coordinates[0] -= dx
            hero_coordinates[1] -= dy
            print("Invalid move, you've hit a wall")
        # if hit an enemy dont move, but interact
        if hero_coordinates[0] == enemy_coordinates[0] and hero_coordinates[1] == enemy_coordinates[1]:
            hero_coordinates[0] -= dx
            hero_coordinates[1] -= dy
            print(Colors.RED + "Punch!" + Colors.RESET)
        # print(f'{MapTiles.hero} - hero location\n{hero_coordinates[0]+1} - x\n{hero_coordinates[1]+1} - y')
    else:
        print("Invalid move")


# def move_action(action):
#     # hero_location = world_map_dimensions[hero_coordinates[0]][hero_coordinates[1]]
#     # print(f'{MapTiles.hero} - hero location\n{hero_coordinates[0]+1} - x\n{hero_coordinates[1]+1} - y')
#     if action in move_table():
#         # print(move_table())
#         dx, dy = move_table()[action]
#         # if hit a wall return message and don't change positions
#         # TODO: display_map() returns map generation, and doesnt have rules so you can call -1 x axis
#         #       But you can't call out of bounds so bigger/less than -+len() crashes
#         if (hero_coordinates[0]+dx) < 0 or hero_coordinates[0]+dx > sizeof_map_y:
#             # y lock
#             hero_coordinates[0] -= dx
#             hero_coordinates[1] -= dy
#             print("Invalid move, you've hit a wall")
#         if hero_coordinates[1]+dy < 0 or hero_coordinates[1]+dy > sizeof_map_x:
#             # x lock
#             hero_coordinates[0] -= dx
#             hero_coordinates[1] -= dy
#             print("Invalid move, you've hit a wall")
#         # if hit an enemy dont move, but interact
#         if hero_coordinates[0] == enemy_coordinates[0]+dx and hero_coordinates[1]+dy == enemy_coordinates[1]:
#             hero_coordinates[0] -= dx
#             hero_coordinates[1] -= dy
#             print(Colors.RED + "Punch!" + Colors.RESET)
#         else:
#             print(f'Before move:\nx: {hero_coordinates[1]}, y:{hero_coordinates[0]}')
#             hero_coordinates[0] += dx
#             hero_coordinates[1] += dy
#             print(f'After move:\nx: {hero_coordinates[1]}, y:{hero_coordinates[0]}')
#         # print(f'{MapTiles.hero} - hero location\n{hero_coordinates[0]+1} - x\n{hero_coordinates[1]+1} - y')
#     else:
#         print("Invalid move")


def game_loop():
    your_name = input("What is your name traveler?")
    if your_name == "":
        your_name = player_data.default_name
    you = Player(name=your_name)
    print(you.your_name())
    while True:
        display_map()
        action = input("your move: ")
        move_action(action)
        # if action == "q":
        #     return False
game_loop()
