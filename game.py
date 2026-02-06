import random

# Player default values
base_player_health = 50
base_player_attack = 5
default_name = "Adam"


class Player:
    def __init__(self, name=default_name, health=base_player_health, attack=base_player_attack):
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
    world_map = world_map_dimensions
    world_map[hero_coordinates[0]][hero_coordinates[1]] = MapTiles.hero
    world_map[enemy_coordinates[0]][enemy_coordinates[1]] = MapTiles.enemy
    return world_map


def display_map():
    """Function to generate map. Ensures that generated map values are not written over"""
    world_map = generate_map()
    for row in world_map:
        print(" ".join(colorize(cell) for cell in row))
    return world_map


Your_name = input("What is your name traveler?")
# Initialize a 5x6 grid with independent values.
world_map_dimensions = [[MapTiles.floor_tile] * 5 for _ in range(6)]
hero_coordinates = [random.randint(0, len(world_map_dimensions) - 1),
                        random.randint(0, len(world_map_dimensions[0]) - 1)]
enemy_coordinates = generate_enemy()

def action_table():
    """moving of entities, calling functions for utility"""
    north=[-1,0]
    west=[0,-1]
    east=[0,1]
    south=[1,0]

def move_table():
    """Tables used for alternative button"""
    up = ["w"]
    left = ["a"]
    right = ["d"]
    down = ["s"]
    quit = ["q"]


def game_loop(your_name):
    if your_name == "":
        your_name = "Adam"
    you = Player(name=your_name)
    print(you.your_name())
    while True:
        display_map()
        action = input("your move: ")
        if action == "q":
            return False
game_loop(Your_name)
