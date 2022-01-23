from abc import ABCMeta, abstractmethod

from make_poffins.berry.berry import Berry


class IBerrySortInterface(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, berries: list[Berry]) -> list[Berry]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnBerry_MainFlavorValue(IBerrySortInterface):
    """Sort berries by the value of their main flavor.

    * Higher is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return sorted(berries, key=lambda x: -x.main_flavor_value)


class SortOnBerry_Smoothness(IBerrySortInterface):
    """Sort berries by the value of their smoothness in ascending order.

    * Lower is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return sorted(berries, key=lambda x: x.smoothness)


class SortOnBerry_MainFlavorToSmoothnessRatio(IBerrySortInterface):
    """Sort berries by the level / smoothness in ascending order.

    * Higher is better.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return sorted(berries, key=lambda x: -x.main_flavor_value / x.smoothness)


class SortOnBerry_WeakenedFlavorValue(IBerrySortInterface):
    """Sort berries by their weakened main flavor value.

    * Higher is better.

    Note:
        The weakened main flavor value takes into account
        those values that reduce for the overall amount.
            Spicy weakened by Dry, etc.

    Returns:
        list[Berry]: sorted list of berries
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return sorted(berries, key=lambda x: -x.__weakened_main_flavor_value__)
