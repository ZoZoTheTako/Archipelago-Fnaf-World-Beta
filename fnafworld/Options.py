from typing import Dict, Union, List
from BaseClasses import MultiWorld
from Options import Toggle, DefaultOnToggle, Choice, Range, Option, OptionDict, OptionList
from schema import Schema, And, Optional, Or

class Goal(Choice):
    "Determine what your playthrough goal will be."
    display_name = "Goal"
    option_Scott = 0
    option_Chipper = 1
    option_Consequences = 2
    option_Clocks = 3

    def get_event_name(self) -> str:
            return {
                self.option_Scott: "Defeat Scott Cawthon",
                self.option_Chipper: "Defeat Chipper's Revenge",
                self.option_Consequences: "Visit Old Man Consequences",
                self.option_Clocks: "Find The Clocks"
            }[self.value]
class EnableChicasMagicRainbow(Toggle):
    "Randomize Chica's Magic Rainbow. Will give junk checks otherwise."
    display_name = "RandomizeChicasMagicRainbow"


class EnableFreddyInSpace0(Toggle):
    "Randomize 0% for Freddy In Space."
    display_name = "RandomizeFreddyInSpace0%"


class ProgressiveBytes(DefaultOnToggle):
    "Determine wether bytes are separate or progressive."
    display_name = "ProgressiveBytes"


class ProgressiveChips(DefaultOnToggle):
    "Determine wether the Strength, Defense, Speed, and Evercomet chips are separate or progressive."
    display_name = "ProgressiveChips"


class ProgressiveArmor(DefaultOnToggle):
    "Determine wether the armor upgrades are separate or progressive."
    display_name = "ProgressiveArmor"

# S
fnafworld_options: Dict[str, Option] = {
    "RandomizeChicasMagicRainbow": RandomizeChicasMagicRainbow,
    "RandomizeFreddyInSpace0%": RandomizeFreddyInSpace0,
    "ProgressiveBytes": ProgressiveBytes,
    "ProgressiveChips": ProgressiveChips,
    "ProgressiveArmor": ProgressiveArmor
}


def is_option_enabled(world: MultiWorld, player: int, name: str) -> bool:
    return get_option_value(world, player, name) > 0


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[int, Dict, List]:
    option = getattr(world, name, None)
    if option == None:
        return 0

    return option[player].value
