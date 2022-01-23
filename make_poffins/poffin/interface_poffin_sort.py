from abc import ABCMeta, abstractmethod

from make_poffins.poffin.poffin import Poffin


class IPoffinSortInterface(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnPoffinMainFlavorValue(IPoffinSortInterface):
    """Sort poffins by the value of their main flavor.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -x.level)


class SortOnPoffinSmoothness(IPoffinSortInterface):
    """Sort poffins by the value of their smoothness in ascending order.

    * Lower is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.smoothness)


class SortOnPoffinLevelToSmoothnessRatio(IPoffinSortInterface):
    """Sort poffins by the level / smoothness in ascending order.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -x.level / x.smoothness)


class SortOnPoffinLevelToSmoothnessRatioSum(IPoffinSortInterface):
    """Sort poffins by the sum of their levels / smoothness in ascending order.

    * Higher is better.

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -((x.level / x.smoothness) + (x.second_level / x.smoothness)))
