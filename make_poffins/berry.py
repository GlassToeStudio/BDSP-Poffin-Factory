from make_poffins.constants import (BOLD, FLAVOR_COLORS, FLAVORS, ITALIC,
                                    N_BOLD, N_ITALIC, RESET, SMOOTHNESS_TABLE,
                                    color_256, sort_flavors,
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
            Ex: [0, 30, 10, 30, 0]
        main flavor value : int\n
    """

    def __init__(self, name: str, values: list[int]):
        self.name = name.lower()
        """The name of the berry"""
        self.flavor_values = values
        """List of 5 values representing the flavors for this berry"""
        self.__weakened_flavor_values__ = None
        """List of 5 values weakened just forfiltering/sorting"""
        self.smoothness = self.__get_smoothness__()
        """The inherent smoothness of this berry"""
        self.main_flavor = self.__get_main_flavor__()
        """The main flavor of this berry: Spicy, Dry, Sweet, Bitter, or Sour"""
        self.main_flavor_value = max(self.flavor_values)
        """The numerical value for the mainflavor"""

        self.__id__ = int(''.join(map(str, self.flavor_values)))
        """The 'unique' id of this berry"""

    def __get_smoothness__(self):
        for smooth_key, smooth_names in SMOOTHNESS_TABLE.items():
            if self.name in smooth_names:
                return smooth_key
        return 255

    def __get_main_flavor__(self):
        self.__weakened_flavor_values__ = subtract_weakening_flavors(self.flavor_values)  # noqa ES501
        flavor_list = [(flavor, FLAVORS[i]) for i, flavor in enumerate(self.flavor_values) if flavor > 0]  # noqa ES501
        sorted_list = [flavor for _, flavor in sort_flavors(flavor_list)]
        return sorted_list[0]

    def __repr__(self) -> str:
        """spelon (Spicy) 35 - Flavors [ 30,  10,   0,   0,   0]

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

        return (f"\t{BOLD}{FLAVOR_COLORS[self.main_flavor]}{self.name:<7}{N_BOLD}"  # noqa ES501
                f"{str(formated_flavor):<17}"
                f"{color_256(255)}{self.smoothness:>3}{RESET}"
                f" - {color_256(239)}Flavors{RESET} {printable_flavor_values}")

    def __str__(self):
        """spelon (Spicy) 35 - Flavors [30, 10,  0,  0,  0]"""
        printable_flavor_values = "["
        for i in range(5):
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{self.flavor_values[i]:>3}, ")  # noqa ES501
        printable_flavor_values = f"{printable_flavor_values[:-2]}]"
        return f"\t{self.name:<7}{self.main_flavor:<8}{self.smoothness:>3} {printable_flavor_values}"  # noqa ES501

    def __eq__(self, other):
        return self.__id__ == other.__id__

    def __hash__(self):
        return self.__id__


if __name__ == "__main__":
    ganlon_berry = Berry("Ganlon", [0, 30, 10, 30, 0])
    print(ganlon_berry)
    print(repr(ganlon_berry))
