from abc import ABCMeta, abstractmethod
from operator import attrgetter, itemgetter

from make_poffins.berry.berry import Berry


class IBerrySortInterface(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self._value = value
        self._reverse = reverse

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

    Format = (('attr', Reversed?), ('name', False))

    Attr:
       0 | str   : name                           \n
       1 | [int] : flavor_values                  \n
       2 | int   : smoothness                     \n
       3 | int   : main_flavor_value              \n
       4 | str   : main_flavor                    \n
       5 | int   : num_flavors                    \n
       6 | int   : rarity                         \n
       7 | [int] : __weakened_flavor_values__     \n
       8 | int   : __weakened_main_flavor_value__ \n
       9 | int   : __weakened_main_flavor__       \n
      10 | int   : __id__                         \n

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
