from typing import Dict, Set, Tuple, NamedTuple

class ItemData(NamedTuple):
    category: str
    code: int
    count: int = 1
    progression: bool = False
    useful: bool = False
    trap: bool = False

#im so tired
item_table: Dict[str, ItemData] = {
    #characters
    'Balloon Boy': ItemData('Character', 19878173001, progression=True),
    'JJ': ItemData('Character', 19878173002, progression=True),
    'Phantom Freddy': ItemData('Character', 19878173003, progression=True),
    'Phantom Chica': ItemData('Character', 19878173003, progression=True),
    'Phantom BB': ItemData('Character', 19878173004, progression=True),
    'Phantom Foxy': ItemData('Character', 19878173005, progression=True),
    'Phantom Mangle': ItemData('Character', 19878173006, progression=True),
    'Withered Bonnie': ItemData('Character', 19878173007, progression=True),
    'Withered Chica': ItemData('Character', 19878173008, progression=True),
    'Withered Freddy': ItemData('Character', 19878173009, progression=True),
    'Withered Foxy': ItemData('Character', 19878173010, progression=True),
    'Shadow Freddy': ItemData('Character', 19878173011, progression=True),
    'Marionette': ItemData('Character', 19878173012, progression=True),
    'Phantom Marionette': ItemData('Character', 19878173013, progression=True),
    'Golden Freddy': ItemData('Character', 19878173014, progression=True),
    'Paperpals': ItemData('Character', 19878173015, progression=True),
    'Nightmare Freddy': ItemData('Character', 19878173016, progression=True),
    'Nightmare Bonnie': ItemData('Character', 19878173017, progression=True),
    'Nightmare Chica': ItemData('Character', 19878173018, progression=True),
    'Nightmare Foxy': ItemData('Character', 19878173019, progression=True),
    'Endo-01': ItemData('Character', 19878173020, progression=True),
    'Endo-02': ItemData('Character', 19878173021, progression=True),
    'Plushtrap': ItemData('Character', 19878173022, progression=True),
    'Endoplush': ItemData('Character', 19878173023, progression=True),
    'Springtrap': ItemData('Character', 19878173024, progression=True),
    'RWQFSFASXC': ItemData('Character', 19878173025, progression=True),
    'Crying Child': ItemData('Character', 19878173026, progression=True),
    'Funtime Foxy': ItemData('Character', 19878173027, progression=True),
    'Nightmare Fredbear': ItemData('Character', 19878173028, progression=True),
    'Nightmare': ItemData('Character', 19878173029, progression=True),
    'Fredbear': ItemData('Character', 19878173030, progression=True),
    'Spring Bonnie': ItemData('Character', 19878173031, progression=True),
    'Jack-O-Bonnie': ItemData('Character', 19878173032, progression=True),
    'Jack-O-Chica': ItemData('Character', 19878173033, progression=True),
    'Animdude': ItemData('Character', 19878173034, progression=True),
    'Mr. Chipper': ItemData('Character', 19878173035, progression=True),
    'Nightmare BB': ItemData('Character', 19878173036, progression=True),
    'Nightmarionne': ItemData('Character', 19878173037, progression=True),
    'Coffee': ItemData('Character', 19878173038, progression=True),
    'Purple Guy': ItemData('Character', 19878173039, progression=True),
    #chips
    'Headstart: Defense': ItemData('Chip', 19878173040, useful=True),
    'Endless: Defense': ItemData('Chip', 19878173041, useful=True),
    'Progressive: Defense': ItemData('Progressive Chip', 19878173042, 2, useful=True),
    'Headstart: Strength': ItemData('Chip', 19878173043, useful=True),
    'Endless: Strength': ItemData('Chip', 19878173044, useful=True),
    'Progressive: Strength': ItemData('Progressive Chip', 19878173045, 2, useful=True),
    'Headstart: Speed': ItemData('Chip', 19878173046, useful=True),
    'Endless: Speed': ItemData('Chip', 19878173047, useful=True),
    'Progressive: Speed': ItemData('Progressive Chip', 19878173048, 2, useful=True),
    'Quickstart: Party': ItemData('Chip', 19878173049, useful=True),
    'Block: Jumpscare': ItemData('Chip', 19878173050, useful=True),
    'Run: Luck': ItemData('Chip', 19878173051, useful=True),
    'Evercomet: Weak': ItemData('Chip', 19878173052, useful=True),
    'Evercomet: Strong': ItemData('Chip', 19878173053, useful=True),
    'Progressive: Evercomet': ItemData('Progressive Chip', 19878173054, 2, useful=True),
    'Auto: Giftboxes': ItemData('Chip', 19878173055, useful=True),
    'Auto: Regen': ItemData('Chip', 19878173056, useful=True),
    'Find: Characters': ItemData('Chip', 19878173057, useful=True),
    'Curse: Status': ItemData('Chip', 19878173058, useful=True),
    'Freddle: Fury': ItemData('Chip', 19878173059, useful=True),
    'Auto: Shield': ItemData('Chip', 19878173060, useful=True),
    'Auto: Mimic': ItemData('Chip', 19878173061, useful=True),
    'Counter: Bite': ItemData('Chip', 19878173062, useful=True),
    'Pizza: Fury': ItemData('Chip', 19878173063, useful=True),
    'Block: Unscrew': ItemData('Chip', 19878173064, useful=True),
    #bytes
    'Gnat': ItemData('Byte', 19878173065, useful=True),
    'Neon Bee': ItemData('Byte', 19878173066, useful=True),
    'Neon Wasp': ItemData('Byte', 19878173067, useful=True),
    'Progressive Bee Byte': ItemData('Progressive Byte', 19878173068, 3, useful=True),
    'Medpod1': ItemData('Byte', 19878173069, useful=True),
    'Medpod2': ItemData('Byte', 19878173070, useful=True),
    'Mega-Med': ItemData('Byte', 19878173071, useful=True),
    'Progressive Medpod Byte': ItemData('Progressive Byte', 19878173072, 3, useful=True),
    'Mini Reaper': ItemData('Byte', 19878173073, useful=True),
    'Reaper': ItemData('Byte', 19878173074, useful=True),
    'X-Reaper': ItemData('Byte', 19878173075, useful=True),
    'Progressive Reaper Byte': ItemData('Progressive Byte', 19878173076, 3, useful=True),
    'Mini-FO': ItemData('Byte', 19878173077, useful=True),
    'UFO': ItemData('Byte', 19878173078, useful=True),
    'X-FO': ItemData('Byte', 19878173079, useful=True),
    'Progressive UFO Byte': ItemData('Progressive Byte', 19878173080, 3, useful=True),
    'Block5': ItemData('Byte', 19878173081, useful=True),
    'Block20': ItemData('Byte', 19878173082, useful=True),
    'Block50': ItemData('Byte', 19878173083, useful=True),
    'Progressive Block Byte': ItemData('Progressive Byte', 19878173084, 3, useful=True),
    'Pop-Pop': ItemData('Byte', 19878173085, useful=True),
    # 19878173086 Used NOWHERE >:)
    'BOOM!': ItemData('Byte', 19878173087, useful=True),
    'KABOOM!!': ItemData('Byte', 19878173088, useful=True),
    'Progressive Bomb Byte': ItemData('Progressive Byte', 19878173089, 3, useful=True),
    'BossDrain01': ItemData('Byte', 19878173090, useful=True),
    'BossDrain02': ItemData('Byte', 19878173091, useful=True),
    'BossDrain-X': ItemData('Byte', 19878173092, useful=True),
    'Progressive BossDrain Byte': ItemData('Progressive Byte', 19878173093, 3, useful=True),
    #other shit
    'Key': ItemData('Major Item', 19878173094, progression=True),
    'Backstage Portal': ItemData('Other', 19878173095, progression=True),
    'Fazbear Hills Button': ItemData('Major Item', 19878173096, progression=True),
    'Dusting Fields Button': ItemData('Major Item', 19878173097, progression=True),
    'Lilygear Lake Button': ItemData('Major Item', 19878173098, progression=True),
    'Deep-Metal Mine Button': ItemData('Major Item', 19878173099, progression=True),
    'Choppy\'s Woods Warp': ItemData('Warp', 19878173100, progression=True),
    'Dusting Fields Warp': ItemData('Warp', 19878173101, progression=True),
    'Lilygear Lake Warp': ItemData('Warp', 19878173102, progression=True),
    'Blacktomb Yard Warp': ItemData('Warp', 19878173103, progression=True),
    'Pinwheel Circus Warp': ItemData('Warp', 19878173104, progression=True),
    'Faz-Tokens (10)': ItemData('Money', 19878173105, 0),
    'Faz-Tokens (50)': ItemData('Money', 19878173105, 0),
    'Faz-Tokens (100)': ItemData('Money', 19878173105, 0)
}

filler_items: Tuple[str, ...] = (
    'Faz-Tokens (10)',
    'Faz-Tokens (50)',
    'Faz-Tokens (100)'
)

def get_item_names_per_category() -> Dict[str, Set[str]]:
    categories: Dict[str, Set[str]] = {}

    for name, data in item_table.items():
        categories.setdefault(data.category, set()).add(name)

    return categories