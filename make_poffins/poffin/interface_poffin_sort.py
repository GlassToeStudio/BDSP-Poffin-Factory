from abc import ABCMeta, abstractmethod

from make_poffins.poffin.poffin import Poffin


class IPoffinSortInterface(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self.value = value
        self.reverse = reverse

    @abstractmethod
    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnPoffins_MainFlavorValue(IPoffinSortInterface):
    """Sort poffins by the value of their main flavor.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -x.level, reverse=self.reverse)


class SortOnPoffins_Smoothness(IPoffinSortInterface):
    """Sort poffins by the value of their smoothness in ascending order.

    * Lower is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.smoothness, reverse=self.reverse)


class SortOnPoffins_LevelToSmoothnessRatio(IPoffinSortInterface):
    """Sort poffins by the level / smoothness in ascending order.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -x.level / x.smoothness, reverse=self.reverse)


class SortOnPoffins_LevelToSmoothnessRatioSum(IPoffinSortInterface):
    """Sort poffins by the sum of their levels / smoothness in ascending order.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -((x.level / x.smoothness) + (x.second_level / x.smoothness)), reverse=self.reverse)
