from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld, CollectionState
from .Options import is_option_enabled

EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable[[CollectionState], bool] = lambda state: True


# SW: Probably don't need the PreCalculatedWeights thing
def get_location_datas(world: Optional[MultiWorld], player: Optional[int],
                       precalculated_weights: PreCalculatedWeights) -> Tuple[LocationData, ...]:

    flooded: PreCalculatedWeights = precalculated_weights
    logic = TimespinnerLogic(world, player, precalculated_weights)

    # 19878173000 - 19878173155 Generic locations
    # 19878173171 - 19878173175 New Pickup checks
    # 19878173246 - 19878173249 Ancient Pyramid
    location_table: List[LocationData] = [
        # overworld
        LocationData('World', 'Headstart: Defense Chest',  19878173000),
        LocationData('World', 'Headstart: Strength Chest',  19878173001),
        LocationData('World', 'Headstart: Speed Chest',  19878173002),
        LocationData('World', 'Evercomet: Weak Chest',  19878173003),
        LocationData('World', 'Quickstart: Party Chest',  19878173004),
        LocationData('World', 'Block: Jumpscare Chest',  19878173005),
        LocationData('World', 'Run: Luck Chest',  19878173006),
        LocationData('World', 'Endless: Defense Chest', 19878173007),
        LocationData('World', 'Endless: Strength Chest',  19878173008),
        LocationData('World', 'Endless: Speed Chest',  19878173009),
        LocationData('World', 'Evercomet: Strong Chest',  19878173010),
        LocationData('World', 'Auto: Giftboxes Chest',  19878173011),
        LocationData('World', 'Auto: Regen Chest',  19878173012),
        LocationData('World', 'Find: Characters Chest',  19878173013),
        LocationData('World', 'Curse: Status Chest',  19878173014),
        LocationData('World', 'Freddle: Fury Chest',  19878173015),
        LocationData('World', 'Auto: Shield Chest',  19878173016),
        LocationData('World', 'Auto: Mimic Chest',  19878173017),
        LocationData('World', 'Counter: Bite Chest',  19878173018),
        LocationData('World', 'Pizza: Fury Chest',  19878173019),
        LocationData('World', 'Block: Unscrew Chest',  19878173020),
        # characters
        LocationData('World', 'Recruit Balloon Boy',  19878173021),
        LocationData('World', 'Recruit JJ',  19878173022),
        LocationData('World', 'Recruit Phantom Freddy',  19878173023),
        LocationData('World', 'Recruit Phantom Chica',  19878173024),
        LocationData('World', 'Recruit Phantom BB',  19878173025),
        LocationData('World', 'Recruit Phantom Foxy',  19878173026),
        LocationData('World', 'Recruit Phantom Mangle',  19878173027),
        LocationData('World', 'Recruit Withered Bonnie',  19878173028),
        LocationData('World', 'Recruit Withered Chica',  19878173029),
        LocationData('World', 'Recruit Withered Freddy',  19878173030),
        LocationData('World', 'Recruit Withered Foxy',  19878173031),
        LocationData('World', 'Recruit Shadow Freddy',  19878173032),
        LocationData('World', 'Recruit The Marionette',  19878173033),
        LocationData('World', 'Recruit Phantom Marionette',  19878173034),
        LocationData('World', 'Recruit Golden Freddy',  19878173035),
        LocationData('World', 'Recruit The Paperpals',  19878173036),
        LocationData('World', 'Recruit Nightmare Freddy',  19878173037),
        LocationData('World', 'Recruit Nightmare Bonnie',  19878173038),
        LocationData('World', 'Recruit Nightmare Chica',  19878173039),
        LocationData('World', 'Recruit Nightmare Foxy',  19878173040),
        LocationData('World', 'Recruit Endo-01',  19878173041),
        LocationData('World', 'Recruit Endo-02',  19878173042),
        LocationData('World', 'Recruit Plushtrap',  19878173043),
        LocationData('World', 'Recruit Endoplush',  19878173044),
        LocationData('World', 'Recruit Springtrap',  19878173045),
        LocationData('World', 'Recruit RWQFSFASXC',  19878173046),
        LocationData('World', 'Recruit The Crying Child',  19878173047),
        LocationData('World', 'Recruit Funtime Foxy',  19878173048),
        LocationData('World', 'Recruit Nightmare Fredbear',  19878173049),
        LocationData('World', 'Recruit Nightmare',  19878173050),
        LocationData('World', 'Recruit Fredbear',  19878173051),
        LocationData('World', 'Recruit Spring Bonnie',  19878173052),
        # minigames
        LocationData('World', 'Complete Foxy.exe',  19878173053),
        LocationData('World', 'Complete Foxy Fighters - A Rank',  19878173054),
        LocationData('World', 'Complete Foxy Fighters - B Rank or below',  19878173055),
        LocationData('World', 'Complete Freddy In Space - Any%',  19878173059),
        LocationData('World', 'Complete Freddy In Space - 100%',  19878173060),
        # shops
        LocationData('World', 'Fazbear Hills Lolbit - Purchase Gnat',  19878173061),
        LocationData('World', 'Fazbear Hills Lolbit - Purchase Neon Bee',  19878173062),
        LocationData('World', 'Fazbear Hills Lolbit - Purchase Neon Wasp',  19878173063),
        LocationData('World', 'Choppy\'s Woods Lolbit - Purchase Medpod1',  19878173064),
        LocationData('World', 'Choppy\'s Woods Lolbit - Purchase Medpod2',  19878173065),
        LocationData('World', 'Choppy\'s Woods Lolbit - Purchase Mega-Med',  19878173066),
        LocationData('World', 'Dusting Fields Lolbit - Purchase Mini Reaper',  19878173067),
        LocationData('World', 'Dusting Fields Lolbit - Purchase Reaper',  19878173068),
        LocationData('World', 'Dusting Fields Lolbit - Purchase X-Reaper',  19878173069),
        LocationData('World', 'Pinwheel Circus Lolbit - Purchase Mini-FO',  19878173070),
        LocationData('World', 'Pinwheel Circus Lolbit - Purchase UFO',  19878173071),
        LocationData('World', 'Pinwheel Circus Lolbit - Purchase X-FO',  19878173072),
        LocationData('World', 'Mysterious Mine Lolbit - Purchase Block5',  19878173073),
        LocationData('World', 'Mysterious Mine Lolbit - Purchase Block20',  19878173074),
        LocationData('World', 'Mysterious Mine Lolbit - Purchase Block50',  19878173075),
        LocationData('World', 'Blacktomb Yard Lolbit - Purchase Pop-Pop',  19878173076),
        LocationData('World', 'Blacktomb Yard Lolbit - Purchase BOOM!',  19878173077),
        LocationData('World', 'Blacktomb Yard Lolbit - Purchase KABOOM!!',  19878173078),
        LocationData('World', 'Deep-Metal Mine Lolbit - Purchase BossDrain01',  19878173079),
        LocationData('World', 'Deep-Metal Mine Lolbit - Purchase BossDrain02',  19878173080),
        LocationData('World', 'Deep-Metal Mine Lolbit - Purchase BossDrain-X',  19878173081),
        LocationData('World', 'Mendo - Purchase Reinforced Endoskeleton',  19878173082),
        LocationData('World', 'Mendo - Purchase Steel Endoskeleton',  19878173083),
        LocationData('World', 'Mendo - Purchase Titanium Endoskeleton',  19878173084),
        LocationData('World', 'Pearl',  19878173085),
        LocationData('World', 'Key', EventId),

        # da buttons
        LocationData('World', 'Fazbear Hills Button', 19878173086, lambda state: state.has('Key', player)),
        LocationData('World', 'Dusting Fields Button', 19878173087, lambda state: state.has('Key', player)),
        LocationData('World', 'Lilygear Lake Button', 19878173088, lambda state: state.has('Key', player)),
        LocationData('World', 'Deep-Metal Mine Button', 19878173089, lambda state: state.has('Key', player))
    ]

    if not world or is_option_enabled(world, player, "EnableChicasMagicRainbow"):
        location_table += (
            LocationData('World', 'Complete Chica\'s Magic Rainbow - Standard',  19878173056),
            LocationData('World', 'Complete Chica\'s Magic Rainbow - Under 3 minutes',  19878173057)
        )
    if not world or is_option_enabled(world, player, "EnableFreddyInSpace0"):
        location_table += (
            LocationData('World', 'Complete Freddy In Space - 0%',  19878173058)
            )
 
    return tuple(location_table)
