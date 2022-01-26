from abc import ABCMeta, abstractmethod
from operator import attrgetter

from make_poffins.berry.berry import Berry


class IBerrySortInterface(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self._value = value
        """Check criteria against this value"""
        self._reverse = reverse
        """Rverse the order of the list if True

        Note:\n
                * default: False
                * by defualt sorters are sorted by best to worst.
        """
    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def reverse(self):
        raise NotImplementedError

    def execute(self, berries: list[Berry]) -> list[Berry]:
        """Process the berries according to this sorting rule.

        Args:
            berries (list[Berry]): berries to sort

        Raises:
            NotImplementedError: Part of interface

        Returns:
            list[Berry]: sorted berries
        """
        berries.sort(key=attrgetter(self.value), reverse=self.reverse)
        return berries

    def __str__(self):
        return self.__class__.__name__


class SortOnBerry_Name(IBerrySortInterface):
    """Sort berries by their name, ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "name"

    @property
    def reverse(self):
        return self._reverse


class SortOnBerry_Smoothness(IBerrySortInterface):
    """Sort berries by the value of their smoothness, in ascending order.

            * Lower is better.
            * List in Ascending Order

    Notes:
        Opposite of sorting by rarity

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "smoothness"

    @property
    def reverse(self):
        return self._reverse


class SortOnBerry_Main_Flavor_Value(IBerrySortInterface):
    """Sort berries by the value of their main flavor, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "main_flavor_value"

    @property
    def reverse(self):
        return not self._reverse


class SortOnBerry_Main_Flavor(IBerrySortInterface):
    """Sort berries by their main flavor name, ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "main_flavor"

    @property
    def reverse(self):
        return self._reverse


class SortOnBerry_Num_Flavors(IBerrySortInterface):
    """Sort berries by the number of flavors they have, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "num_flavors"

    @property
    def reverse(self):
        return not self._reverse


class SortOnBerry_Rarity(IBerrySortInterface):
    """Sort berries by thier rarity, ascending.

            * Lower is better.
            * List in Ascending Order

    Notes:
        Opposite of sorting by smoothness

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "rarity"

    @property
    def reverse(self):
        return self._reverse


class SortOnBerry__Weakened_Main_Flavor_Value(IBerrySortInterface):
    """Sort berries by their weakened main flavor value, in descending order.

            * Higher is better.
            * List in Descending Order

    Note:
        The weakened main flavor value takes into account
        those values that reduce for the overall amount.
            Spicy weakened by Dry, etc.

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "_weakened_main_flavor_value"

    @property
    def reverse(self):
        return not self._reverse


class SortOnBerry__Weakened_Main_Flavor(IBerrySortInterface):
    """Sort berries by their weakened flavor name, ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "_weakened_main_flavor"

    @property
    def reverse(self):
        return self._reverse


class SortOnBerry___id__(IBerrySortInterface):
    """Sort berries by their weakened flavor name, descending.

            * Higher is not better or worse than lower
            * List in Descending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "__id__"

    @property
    def reverse(self):
        return not self._reverse


class SortOnBerry_Main_Flavor_To_Smoothness_Ratio(IBerrySortInterface):
    """Sort berries by the level / smoothness, in descending order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return "main_flavor_to_smoothness_ratio"

    @property
    def reverse(self):
        return not self._reverse
