
from make_poffins.berry import berry_library
from make_poffins.berry.berry import Berry
from make_poffins.constants import (BOLD, FLAVOR_COLORS, FLAVORS, N_BOLD,
                                    RESET, color_256, foul_poffin, mild_poffin,
                                    outline, overripe_poffin, rich_poffin,
                                    sort_flavors, super_mild_poffin)


class Poffin:
    """
    A poffin with which to increase contest stats.

    Attributes:
        Flavor Values: [int, int, int, int, int]
        Smoothness: int
        Berries (aka recipe): list[Berry] (up to 4)
        Flavor Names: list[str]
        Level: int
        Second Level: int
        repr name: str
        name: str
        __id__: int
    """

    def __init__(self, flavor_values: list[int], smoothness: int, berries: list[Berry]):  # noqa ES501
        """
        A poffin with which to increase contest stats.

        Attributes:
            Flavor Values: [int, int, int, int, int]
            Smoothness: int
            Berries (aka recipe): list[Berry] (up to 4)
            Flavor Names: list[str]
            Level: int
            Second Level: int
            repr name: str
            name: str
            __id__: int
        """
        self.flavor_values = flavor_values
        """Values of the flavors - unaltered. Ex: [10, 0, 0, 10, 0]"""
        self.smoothness = smoothness
        """Calcualted smoothness of thisw poffin"""
        self.berries = berries
        """The berries used to make this poffin: 1 - 4 berries."""
        self.flavor_names = self._get_flavors()
        """Get a lsit of all flavor names - ["Sweet", "Dry", "Bitter"] for example"""  # noqa ES501
        self.main_flavor = self._get_main_flavor()
        """The main flavor - "Sweet" for example"""
        self.level = self._get_level()
        """The value of the strongest flavor"""
        self.second_level = self._get_second_level()
        """The value of the second strongest flavor - maybe helpful in raking"""  # noqa ES501
        self.name = ""
        """The name of the poffin - Super Mild Poffin for example"""
        self.repr_name = ""
        """The fancy colored version of the poffins name"""
        self.num_flavors = self._num_flavors()
        """Total number of flavors for this poffin"""
        self.rarity = sum(x.rarity for x in berries)
        """The total rarity (in berriy rarity) for this poffin"""
        self.__id__ = int(''.join(map(str, self.flavor_values)))
        """The 'unique' id of this poffin"""
        self.level_to_smoothness_ratio = self.level/self.smoothness
        """ level / smoothness"""
        self.level_to_smoothness_ratio_sum = (self.level + self.second_level)/self.smoothness
        """ level / smoothness"""
        self._set_names()

    def _get_flavors(self) -> list[str]:
        flavor_list = [(flavor, FLAVORS[i]) for i, flavor in enumerate(self.flavor_values) if flavor > 0]  # noqa ES501
        sorted_list = [flavor for _, flavor in sort_flavors(flavor_list)]

        if len(sorted_list) == 0 or sorted_list is None:
            sorted_list = ["Spicy", "Dry", "Sweet"]

        return sorted_list

    def _get_main_flavor(self):
        return self.flavor_names[0]

    def _get_level(self):
        return max(self.flavor_values)

    def _get_second_level(self):
        temp_list = self.flavor_values.copy()
        temp_list.remove(self.level)
        return max(max(temp_list), 0)

    def _set_names(self):
        if self.level == 0 or len(self.berries) != len(set(self.berries)):
            self.level = 2
            self.repr_name = foul_poffin
            self.name = "foul poffin"
        elif self.level >= 100:
            self.repr_name = super_mild_poffin
            self.name = "super mild poffin"  # noqa ES501
        elif self.level >= 50:
            self.repr_name = mild_poffin
            self.name = "mild poffin"
        elif self._num_flavors() == 4:
            self.repr_name = overripe_poffin
            self.name = "overripe poffin"
        elif self._num_flavors() == 3:
            self.repr_name = rich_poffin
            self.name = "rich poffin"
        else:
            self.repr_name = self.name = f"{' '.join(map(str, self.flavor_names))}"  # noqa ES501

    def _num_flavors(self):
        return len(self.flavor_names)

    def __repr__(self) -> str:
        """
        Level: 148 - Super Mild Poffin   Smoothness: 30
            [148, 0, 0, 28, 0]
            Main Flavor: Spicy
            All Flavors: Spicy - Bitter
            Second strongest flavor value: 28
        """
        printable_flavor_values = f"{RESET}["
        for i, f in enumerate(FLAVORS):
            bold = BOLD if f == self.main_flavor else ""
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{FLAVOR_COLORS[FLAVORS[i]]}"
                                       f"{bold}{self.flavor_values[i]:>3}{RESET}, ")  # noqa ES501
        printable_flavor_values = f"{printable_flavor_values[:-2]}]"

        string_of_all_flavors = "".join([f"{BOLD}{FLAVOR_COLORS[x]}{x:<7}{RESET}" for x in self.flavor_names])  # noqa ES501
        join_berries = '\n'.join(map(repr, self.berries))
        formated_berry_string = f"* {color_256(239)}Berries used:{RESET}\n{join_berries}"  # noqa ES501
        name_for_printing = self.repr_name if self.repr_name != self.name else f'{f"{BOLD}{string_of_all_flavors}{RESET}":<28}'  # noqa ES501
        amt = 75
        return (
            "\n"
            f"{outline}{'-'*amt}{RESET}\n"
            f"{BOLD}{self.level} - {name_for_printing:<37}{BOLD} {self.smoothness}{N_BOLD}"  # noqa ES501
            f" - {color_256(239)}Flavors{RESET} {printable_flavor_values} Rarity: {self.rarity}\n"
            f"{outline}{'-'*amt}{RESET}\n"
            f"* {string_of_all_flavors} ({self.level}, {self.second_level})\n"  # noqa ES501
            f"{formated_berry_string}\n"
            f"{outline}{'-'*amt}{RESET}\n")

    def __str__(self) -> str:
        formated_berry_string = '\n'.join(map(str, self.berries))
        printable_flavor_values = "["
        for i in range(5):
            printable_flavor_values = (f"{printable_flavor_values}"
                                       f"{self.flavor_values[i]:>3}, ")
        printable_flavor_values = f"{printable_flavor_values[:-2]}]"
        return f"{self.level:<4}{self.name:<20}{self.smoothness:>2} {printable_flavor_values} Rarity: {self.rarity}\n{formated_berry_string}"  # noqa ES501

    def __eq__(self, other):
        return self.__id__ == other.__id__

    def __hash__(self):
        return self.__id__


def main():
    test_poffin = Poffin([148, 0, 0, 28, 0], 30, berry_library.single_recipe)  # noqa ES501
    print(repr(test_poffin))
    print(str(test_poffin))


if __name__ == "__main__":
    main()
