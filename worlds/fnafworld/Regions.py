from typing import List, Set, Dict, Tuple, Optional, Callable
from BaseClasses import CollectionState, MultiWorld, Region, Entrance, Location
from .Options import is_option_enabled
from .Locations import LocationData, get_location_datas


def create_regions_and_locations(world: MultiWorld, player: int):
    locationn_datas: Tuple[LocationData] = get_location_datas(world, player)

    locations_per_region: Dict[str, List[LocationData]] = split_location_datas_per_region(locationn_datas)

    regions = [
        create_region(world, player, locations_per_region, 'Menu'),
        create_region(world, player, locations_per_region, 'World'),


def throwIfAnyLocationIsNotAssignedToARegion(regions: List[Region], regionNames: Set[str]):
    existingRegions: Set[str] = set()

    for region in regions:
        existingRegions.add(region.name)

    if (regionNames - existingRegions):
        raise Exception("FnafWorld: the following regions are used in locations: {}, but no such region exists".format(regionNames - existingRegions))


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


def connectStartingRegion(world: MultiWorld, player: int):
    menu = world.get_region('Menu', player)
    overworld = world.get_region('World', player)

    menu_to_overworld = Entrance(player, 'World', menu)
    menu_to_overworld.connect(overworld)
    menu.exits.append(menu_to_overworld)


def connect(world: MultiWorld, player: int, source: str, target: str, 
            rule: Optional[Callable[[CollectionState], bool]] = None):
    
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, "", sourceRegion)

    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)


def split_location_datas_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]]  = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region
