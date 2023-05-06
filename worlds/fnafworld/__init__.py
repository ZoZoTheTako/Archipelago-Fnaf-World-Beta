from typing import Dict, List, Set, Tuple, TextIO, Union
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Items import get_item_names_per_category
from .Items import item_table, filler_items
from .Locations import get_location_datas, EventId
from .Options import is_option_enabled, get_option_value, fnafworld_options
from .Regions import create_regions_and_locations
from worlds.AutoWorld import World, WebWorld

class FnafWorldWebWorld(WebWorld):
    theme = "ice"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the FNAF World randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["ZoZoTheTako"]
    )


    tutorials = [setup, setup_de]

class FnafWorldWorld(World):
    """
    FNAF World is a cute turn-based RPG! 
    Take your favorite animatronics from the Five Nights at Freddy's series out on a wacky adventure to save animatronica!
    """

    option_definitions = fnafworld_options
    game = "FNAF World"
    topology_present = True
    data_version = 11
    web = FnafWorldWebWorld()
    required_client_version = (0, 4, 0)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {location.name: location.code for location in get_location_datas(None, None, None)}
    item_name_groups = get_item_names_per_category()


    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)


    def create_regions(self) -> None: 
        create_regions_and_locations(self.multiworld, self.player)

    def create_items(self) -> None: 
        self.create_and_assign_event_items()

        excluded_items: Set[str] = self.get_excluded_items()

        self.assign_starter_items(excluded_items)
        self.place_first_progression_item(excluded_items)

        self.multiworld.itempool += self.get_item_pool(excluded_items)

    def set_rules(self) -> None:
        ending: str
        if self.is_option_enabled("Scott"):
            ending = "Defeat Scott Cawthon"
        if self.is_option_enabled("Chipper"):
            ending = "Defeat Chipper's Revenge"
        if self.is_option_enabled("Consequences"):
            ending = "Visit Old Man Consequences"
        else:
            ending = "Collect The Clocks"

        self.multiworld.completion_condition[self.player] = lambda state: state.has(ending, self.player) 

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {}

        ap_specific_settings: Set[str] = {"RisingTidesOverrides", "TrapChance"}

        for option_name in timespinner_options:
            if (option_name not in ap_specific_settings):
                slot_data[option_name] = self.get_option_value(option_name)

        slot_data["StinkyMaw"] = True
        slot_data["ProgressiveVerticalMovement"] = False
        slot_data["ProgressiveKeycards"] = False
        slot_data["PersonalItems"] = self.get_personal_items()
        slot_data["PyramidKeysGate"] = self.precalculated_weights.pyramid_keys_unlock
        slot_data["PresentGate"] = self.precalculated_weights.present_key_unlock
        slot_data["PastGate"] = self.precalculated_weights.past_key_unlock
        slot_data["TimeGate"] = self.precalculated_weights.time_key_unlock
        slot_data["Basement"] = int(self.precalculated_weights.flood_basement) + \
                                int(self.precalculated_weights.flood_basement_high)
        slot_data["Xarion"] = self.precalculated_weights.flood_xarion
        slot_data["Maw"] = self.precalculated_weights.flood_maw
        slot_data["PyramidShaft"] = self.precalculated_weights.flood_pyramid_shaft
        slot_data["BackPyramid"] = self.precalculated_weights.flood_pyramid_back
        slot_data["CastleMoat"] = self.precalculated_weights.flood_moat
        slot_data["CastleCourtyard"] = self.precalculated_weights.flood_courtyard
        slot_data["LakeDesolation"] = self.precalculated_weights.flood_lake_desolation
        slot_data["DryLakeSerene"] = self.precalculated_weights.dry_lake_serene

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        if self.is_option_enabled("UnchainedKeys"):
            spoiler_handle.write(f'Modern Warp Beacon unlock:       {self.precalculated_weights.present_key_unlock}\n')
            spoiler_handle.write(f'Timeworn Warp Beacon unlock:     {self.precalculated_weights.past_key_unlock}\n')

            if self.is_option_enabled("EnterSandman"):
                spoiler_handle.write(f'Mysterious Warp Beacon unlock:   {self.precalculated_weights.time_key_unlock}\n')
        else:
            spoiler_handle.write(f'Twin Pyramid Keys unlock:        {self.precalculated_weights.pyramid_keys_unlock}\n')
       
        if self.is_option_enabled("RisingTides"):
            flooded_areas: List[str] = []

            if self.precalculated_weights.flood_basement:
                if self.precalculated_weights.flood_basement_high:
                    flooded_areas.append("Castle Basement")
                else:
                    flooded_areas.append("Castle Basement (Savepoint available)")
            if self.precalculated_weights.flood_xarion:
                flooded_areas.append("Xarion (boss)")
            if self.precalculated_weights.flood_maw:
                flooded_areas.append("Maw (caves + boss)")
            if self.precalculated_weights.flood_pyramid_shaft:
                flooded_areas.append("Ancient Pyramid Shaft")
            if self.precalculated_weights.flood_pyramid_back:
                flooded_areas.append("Sandman\\Nightmare (boss)")
            if self.precalculated_weights.flood_moat:
                flooded_areas.append("Castle Ramparts Moat")
            if self.precalculated_weights.flood_courtyard:
                flooded_areas.append("Castle Courtyard")
            if self.precalculated_weights.flood_lake_desolation:
                flooded_areas.append("Lake Desolation")
            if not self.precalculated_weights.dry_lake_serene:
                flooded_areas.append("Lake Serene")

            if len(flooded_areas) == 0:
                flooded_areas_string: str = "None"
            else:
                flooded_areas_string: str = ", ".join(flooded_areas)

            spoiler_handle.write(f'Flooded Areas:                   {flooded_areas_string}\n')

    def create_item(self, name: str) -> Item:
        data = item_table[name]

        if data.useful:
            classification = ItemClassification.useful
        elif data.progression:
            classification = ItemClassification.progression
        elif data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
            
        item = Item(name, classification, data.code, self.player)

        if not item.advancement:
            return item

        if (name == 'Tablet' or name == 'Library Keycard V') and not self.is_option_enabled("DownloadableItems"):
            item.classification = ItemClassification.filler
        elif name == 'Oculus Ring' and not self.is_option_enabled("EyeSpy"):
            item.classification = ItemClassification.filler
        elif (name == 'Kobo' or name == 'Merchant Crow') and not self.is_option_enabled("GyreArchives"):
            item.classification = ItemClassification.filler
        elif name in {"Timeworn Warp Beacon", "Modern Warp Beacon", "Mysterious Warp Beacon"} \
                and not self.is_option_enabled("UnchainedKeys"):
            item.classification = ItemClassification.filler

        return item

    def get_filler_item_name(self) -> str:
        trap_chance: int = self.get_option_value("TrapChance")
        enabled_traps: List[str] = self.get_option_value("Traps")

        if self.multiworld.random.random() < (trap_chance / 100) and enabled_traps:
            return self.multiworld.random.choice(enabled_traps)
        else:
            return self.multiworld.random.choice(filler_items) 

    def get_excluded_items(self) -> Set[str]:
        excluded_items: Set[str] = set()

        if self.is_option_enabled("StartWithJewelryBox"):
            excluded_items.add('Jewelry Box')
        if self.is_option_enabled("StartWithMeyef"):
            excluded_items.add('Meyef')
        if self.is_option_enabled("QuickSeed"):
            excluded_items.add('Talaria Attachment')

        if self.is_option_enabled("UnchainedKeys"):
            excluded_items.add('Twin Pyramid Key')

            if not self.is_option_enabled("EnterSandman"):
                excluded_items.add('Mysterious Warp Beacon')
        else:
            excluded_items.add('Timeworn Warp Beacon')
            excluded_items.add('Modern Warp Beacon')
            excluded_items.add('Mysterious Warp Beacon')

        for item in self.multiworld.precollected_items[self.player]:
            if item.name not in self.item_name_groups['UseItem']:
                excluded_items.add(item.name)

        return excluded_items

    def assign_starter_items(self, excluded_items: Set[str]) -> None:
        non_local_items: Set[str] = self.multiworld.non_local_items[self.player].value

        local_starter_melee_weapons = tuple(item for item in starter_melee_weapons if item not in non_local_items)
        if not local_starter_melee_weapons:
            if 'Plasma Orb' in non_local_items:
                raise Exception("Atleast one melee orb must be local")
            else:
                local_starter_melee_weapons = ('Plasma Orb',)

        local_starter_spells = tuple(item for item in starter_spells if item not in non_local_items)
        if not local_starter_spells:
            if 'Lightwall' in non_local_items:
                raise Exception("Atleast one spell must be local")
            else:
                local_starter_spells = ('Lightwall',)

        self.assign_starter_item(excluded_items, 'Tutorial: Yo Momma 1', local_starter_melee_weapons)
        self.assign_starter_item(excluded_items, 'Tutorial: Yo Momma 2', local_starter_spells)

    def assign_starter_item(self, excluded_items: Set[str], location: str, item_list: Tuple[str, ...]) -> None:
        item_name = self.multiworld.random.choice(item_list)

        self.place_locked_item(excluded_items, location, item_name)

    def place_first_progression_item(self, excluded_items: Set[str]) -> None:
        if self.is_option_enabled("QuickSeed") or self.is_option_enabled("Inverted") \
                or self.precalculated_weights.flood_lake_desolation:
            return

        for item in self.multiworld.precollected_items[self.player]:
            if item.name in starter_progression_items and not item.name in excluded_items:
                return

        local_starter_progression_items = tuple(
            item for item in starter_progression_items 
                if item not in excluded_items and item not in self.multiworld.non_local_items[self.player].value)

        if not local_starter_progression_items:
            return

        progression_item = self.multiworld.random.choice(local_starter_progression_items)

        self.multiworld.local_early_items[self.player][progression_item] = 1

    def place_locked_item(self, excluded_items: Set[str], location: str, item: str) -> None:
        excluded_items.add(item)

        item = self.create_item(item)

        self.multiworld.get_location(location, self.player).place_locked_item(item)

    def get_item_pool(self, excluded_items: Set[str]) -> List[Item]:
        pool: List[Item] = []

        for name, data in item_table.items():
            if name not in excluded_items:
                for _ in range(data.count):
                    item = self.create_item(name)
                    pool.append(item)

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(pool)):
            item = self.create_item(self.get_filler_item_name())
            pool.append(item)

        return pool

    def create_and_assign_event_items(self) -> None:
        for location in self.multiworld.get_locations(self.player):
            if location.address == EventId:
                item = Item(location.name, ItemClassification.progression, EventId, self.player)
                location.place_locked_item(item)

    def get_personal_items(self) -> Dict[int, int]:
        personal_items: Dict[int, int] = {}

        for location in self.multiworld.get_locations(self.player):
            if location.address and location.item and location.item.code and location.item.player == self.player:
                personal_items[location.address] = location.item.code

        return personal_items
    
    def is_option_enabled(self, option: str) -> bool:
        return is_option_enabled(self.multiworld, self.player, option)

    def get_option_value(self, option: str) -> Union[int, Dict, List]:
        return get_option_value(self.multiworld, self.player, option)
