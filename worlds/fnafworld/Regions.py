from typing import List, Set, Dict, Tuple, Optional, Callable
from BaseClasses import CollectionState, MultiWorld, Region, Entrance, Location
from .Locations import LocationData, get_location_datas


def create_regions_and_locations(world: MultiWorld, player: int):
    location_data: Tuple[LocationData] = get_location_datas(world, player)

    locations_per_region: Dict[str, List[LocationData]] = split_location_datas_per_region(location_data)

    regions = [
        create_region(world, player, locations_per_region, 'Menu'),
        create_region(world, player, locations_per_region, 'World'),
    ]


def throw_if_any_location_is_not_assigned_to_a_region(regions: List[Region], region_names: Set[str]):
    existing_regions: Set[str] = set()

    for region in regions:
        existing_regions.add(region.name)

    if region_names - existing_regions:
        raise Exception("FnafWorld: the following regions are used in locations: {},"
                        " but no such region exists".format(region_names - existing_regions))


def create_location(player: int, location_data: LocationData, region: Region) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    if id is None:
        location.event = True
        location.locked = True

    return location


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]], name: str) -> Region:
    region = Region(name, player, world)

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region)
            region.locations.append(location)

    return region


def connect_starting_region(world: MultiWorld, player: int):
    menu = world.get_region('Menu', player)
    overworld = world.get_region('World', player)

    menu_to_overworld = Entrance(player, 'World', menu)
    menu_to_overworld.connect(overworld)
    menu.exits.append(menu_to_overworld)


def connect(world: MultiWorld, player: int, source: str, target: str, 
            rule: Optional[Callable[[CollectionState], bool]] = None):
    
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)

    connection = Entrance(player, "", source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)


def split_location_datas_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region
