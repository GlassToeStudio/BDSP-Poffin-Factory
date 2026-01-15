from make_poffins.constants import (BOLD, FLAVOR_COLORS, FLAVORS, ITALIC,
                                    N_BOLD, N_ITALIC, RARITY_TABLE, RESET,
                                    SMOOTHNESS_TABLE, color_256, get_emoji,
                                    subtract_weakening_flavors)


class Berry:
    """A berry with which poffins are made.

    Ex:
        ganlon Dry     40 [0, 30, 10, 30, 0]

    Attributes:
        name : str.lower()\n

        main flavor : str\n

            Ex: Spicy, Dry, Sweet, Bitter, Sour>\n

        smoothness : int\n

        flavor values : list[int, int, int, int, int]\n

            Ex: [0, 30, 10, 30, 0]\n

        main flavor value : int\n

    https://progameguides.com/pokemon/complete-poffin-recipe-guide-for-pokemon-brilliant-diamond-and-shining-pearl/
    """
    __slots__ = [
        'name', 'flavor_values', 'smoothness', 'main_flavor_value',
        'main_flavor', 'num_flavors', 'rarity', '_weakened_flavor_values',
        '_weakened_main_flavor_value', '_weakened_main_flavor',
        '__id__', 'main_flavor_to_smoothness_ratio', 'emoji'
    ]

    def __init__(self, name: str, values: list[int], emoji: str = None):
        """A berry with which poffins are made.

        Arguments:
            name (str): the name of the berry
            values list[int]: the 5 flavor values of this berry

        Attributes:
            name : str.lower()\n
            main flavor : str\n
                Ex: Spicy, Dry, Sweet, Bitter, Sour>\n
            smoothness : int\n
            flavor values : list[int, int, int, int, int]\n
                Ex: [0, 30, 10, 30, 0]\n
            main flavor value : int\n
        """

        self.name = name.lower()
        """The name of the berry"""
        self.flavor_values = values
        """List of 5 values representing the flavors for this berry"""
        self.smoothness = self._get_smoothness()
        """The inherent smoothness of this berry"""
        self.main_flavor_value = max(self.flavor_values)
        """The numerical value for the main flavor"""
        self.main_flavor = self._get_main_flavor()
        """The main flavor of this berry: Spicy, Dry, Sweet, Bitter, or Sour"""
        self.num_flavors = sum(1 for x in self.flavor_values if x > 0)
        """Total number of flavors this berry has"""
        self.rarity = self._get_rarity()
        """The rarity of this berry (1-15), higher is more rare"""

        # Other info
        self._weakened_flavor_values = self._get_weakened_flavor_values()
        """List of 5 values weakened just for filtering/sorting"""
        self._weakened_main_flavor_value = max(self._weakened_flavor_values)
        """The numerical value for the weakened main flavor"""
        self._weakened_main_flavor = self._get_weakened_main_flavor()
        """The main flavor of this berry: Spicy, Dry, Sweet, Bitter, or Sour"""
        self.__id__ = int(''.join(map(str, self.flavor_values)))
        """The 'unique' id of this berry"""
        self.main_flavor_to_smoothness_ratio = self.main_flavor_value / self.smoothness
        """Smoothness / ratio; for sorting"""
        if not emoji:
            self.emoji = self._get_emoji()
        else:
            self.emoji = emoji

    def _get_smoothness(self) -> int:
        """Get the smoothness value for this berry from the SMOOTHNESS_TABLE"""
        for smooth_key, smooth_names in SMOOTHNESS_TABLE.items():
            if self.name in smooth_names:
                return smooth_key
        return 255

    def _get_main_flavor(self) -> str:
        """Return the name of the flavor with the max value"""
        return FLAVORS[self.flavor_values.index(self.main_flavor_value)]

    def _get_weakened_main_flavor(self) -> str:
        """Return the name of the flavor with the max value"""
        return FLAVORS[self._weakened_flavor_values.index(self._weakened_main_flavor_value)]

    def _get_rarity(self) -> int:
        return RARITY_TABLE[self.smoothness]

    def _get_weakened_flavor_values(self) -> list[int]:
        """Get list of 5 values weakened just for filtering/sorting"""
        return subtract_weakening_flavors(self.flavor_values)  # noqa ES501

    def _get_emoji(self):
        return get_emoji(self.main_flavor)

    def print_with_weakened_values(self):
        """ganlon Dry      40 [  0,  30,  10,  30,   0]"""
        printable_flavor_values = "["
        for i in range(5):
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{self._weakened_flavor_values[i]:>3}, ")  # noqa ES501
        printable_flavor_values = f"{printable_flavor_values[:-2]}]"
        r = f"\t{'- weak':<7}{self._weakened_main_flavor:<8}{self.smoothness:>3} {printable_flavor_values}"  # noqa ES501
        return f"{str(self)}\n{r}"

    def __repr__(self) -> str:
        """ganlon (Dry)    40 - Flavors [  0,  30,  10,  30,   0]

            But colored
        """

        printable_flavor_values = "["
        for i, f in enumerate(FLAVORS):
            bold = BOLD if f == self.main_flavor else ""
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{FLAVOR_COLORS[FLAVORS[i]]}"
                                       f"{bold}{self.flavor_values[i]:>3}{RESET}, ")  # noqa ES501

        printable_flavor_values = f"{printable_flavor_values[:-2]}]"
        formated_flavor = f"({ITALIC}{self.main_flavor}{N_ITALIC})"

        return (f"    {self.emoji:>2}{BOLD}{FLAVOR_COLORS[self.main_flavor]}{self.name:<7}{N_BOLD}"  # noqa ES501
                f"{str(formated_flavor):<17}"
                f"{color_256(255)}{self.smoothness:>3}{RESET}"
                f" - {color_256(239)}Flavors{RESET} {printable_flavor_values} Rarity:{self.rarity:>3}")

    def __str__(self):
        """ganlon Dry      40 [  0,  30,  10,  30,   0]"""
        printable_flavor_values = "["
        for i in range(5):
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{self.flavor_values[i]:>3}, ")  # noqa ES501
        printable_flavor_values = f"{printable_flavor_values[:-2]}]"
        return f"\t{self.name:<7}{self.main_flavor:<8}{self.smoothness:>3} {printable_flavor_values} Rarity:{self.rarity:>3}"  # noqa ES501

    def __hash__(self):
        return self.__id__

    def printSoICanMakeAList(self):
        printable_flavor_values = "["
        for i in range(5):
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{self.flavor_values[i]:>1}, ")
        # = Berry("{self.name.capitalize()}", {printable_flavor_values[:-2]}])\n'
        r = (f'{self.name}_berry,')
        # f'"""{self.main_flavor.capitalize()} ({self.smoothness}) -- {printable_flavor_values[:-2]}]"""')
        return r


if __name__ == "__main__":
    ganlon_berry = Berry("Ganlon", [0, 30, 10, 30, 0])
    print(ganlon_berry)
    print(repr(ganlon_berry))
    print(ganlon_berry.print_with_weakened_values())
