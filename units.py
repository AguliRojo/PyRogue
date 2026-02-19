def hero(name="John"):
    """Define hero stats and initial name"""
    default_hp = 50
    default_atk = 10
    current_hp = default_hp
    overview = {
        "name": name,
        "hp": f"{current_hp}/{default_hp}",
        "attack": default_atk,
    }
    return overview


def foe(name="Badddy Bad"):
    default_hp = 20
    default_atk = 5
    current_hp = default_hp
    overview = {
        "name": name,
        "hp": f"{current_hp}/{default_hp}",
        "attack": default_atk,
    }
    return overview
