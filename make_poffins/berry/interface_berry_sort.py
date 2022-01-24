from abc import ABCMeta, abstractmethod
from operator import attrgetter

from make_poffins.berry.berry import Berry


class IBerrySortInterface(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self.value = value
        """Check criteria against this value"""
        self.reverse = reverse
        """Rverse the order of the list if True

        Note:\n
                * default: False
                * by defualt sorters are sorted by best to worst.
        """

    @abstractmethod
    def execute(self, berries: list[Berry]) -> list[Berry]:
        """Process the berries according to this sorting rule.

        Args:
            berries (list[Berry]): berries to sort

        Raises:
            NotImplementedError: Part of interface

        Returns:
            list[Berry]: sorted berries
        """
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnBerry_Attrs(IBerrySortInterface):
    """Sort berries by multiple values in ascending (False) or descenidng (True) order.

    Notes;\n
            * H: means Higher is better so supply True to the second argument
                - (("coolness", True), )
            * L: means Lower is better so supply False to the second argument
                - (("rarity", False), )
            * -: means neither is better - False for ascending, True for descending
                - (("rarity", False), )

    Attr:
        *  0 | str   : name                          * - \n
        *  1 | [int] : flavor_values                 * H \n
        *  2 | int   : smoothness                    * L \n
        *  3 | int   : main_flavor_value             * H \n
        *  4 | str   : main_flavor                   * - \n
        *  5 | int   : num_flavors                   * H \n
        *  6 | int   : rarity                        * L \n
        *  7 | [int] : _weakened_flavor_values       * H \n
        *  8 | int   : _weakened_main_flavor_value   * H \n
        *  9 | int   : _weakened_main_flavor         * - \n
        * 10 | int   : __id__                        * - \n

    https://docs.python.org/3/howto/sorting.html

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        for key, reverse in reversed(self._value):
            berries.sort(key=attrgetter(key), reverse=reverse)
        return berries


class SortOnBerry_Name(IBerrySortInterface):
    """Sort berries by their name, ascending.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('name'), reverse=self._reverse)
        return berries


class SortOnBerry_Smoothness(IBerrySortInterface):
    """Sort berries by the value of their smoothness in ascending order.

    * Lower is better.

    Notes:
        Opposite of sorting by rarity

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('smoothness'), reverse=self._reverse)
        return berries


class SortOnBerry_MainFlavorValue(IBerrySortInterface):
    """Sort berries by the value of their main flavor, descending.

    * Higher is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('main_flavor_value'), reverse=not self._reverse)
        return berries


class SortOnBerry_MainFlavor(IBerrySortInterface):
    """Sort berries by their main flavor name, ascending.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('main_flavor'), reverse=self._reverse)
        return berries


class SortOnBerry_NumFlavors(IBerrySortInterface):
    """Sort berries by the number of flavors they have, descending.

    * Higher is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('num_flavors'), reverse=not self._reverse)
        return berries


class SortOnBerry_Rarity(IBerrySortInterface):
    """Sort berries by thier rarity, ascending.

    * Lower is better.

    Notes:
        Opposite of sorting by smoothness

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('rarity'), reverse=self._reverse)
        return berries


class SortOnBerry_WeakenedMainFlavorValue(IBerrySortInterface):
    """Sort berries by their weakened main flavor value, in descending order.

    * Higher is better.

    Note:
        The weakened main flavor value takes into account
        those values that reduce for the overall amount.
            Spicy weakened by Dry, etc.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('_weakened_main_flavor_value'), reverse=not self._reverse)
        return berries


class SortOnBerry_WeakenedMainFlavor(IBerrySortInterface):
    """Sort berries by their weakened flavor name, ascending.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('_weakened_main_flavor'), reverse=self._reverse)
        return berries


class SortOnBerry__id__(IBerrySortInterface):
    """Sort berries by their weakened flavor name, descending.

    * Higher is not better or worse than lower

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=attrgetter('__id__'), reverse=not self._reverse)
        return berries


class SortOnBerry_MainFlavorToSmoothnessRatio(IBerrySortInterface):
    """Sort berries by the level / smoothness in descending order.

    * Higher is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        berries.sort(key=lambda x: x.main_flavor_value / x.smoothness, reverse=not self._reverse)
        return berries
