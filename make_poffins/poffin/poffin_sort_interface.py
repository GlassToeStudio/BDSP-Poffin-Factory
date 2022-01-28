from abc import ABCMeta, abstractmethod
from operator import attrgetter

from make_poffins.poffin.poffin import Poffin


class IPoffinSortInterface(metaclass=ABCMeta):
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

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        poffins.sort(key=attrgetter(self.value), reverse=self.reverse)
        return poffins

    def __str__(self):
        return self.__class__.__name__


class SortOnPoffins_Smoothness(IPoffinSortInterface):
    """Sort poffins by the value of their smoothness, in ascending order.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "smoothness"

    @property
    def reverse(self):
        return self._reverse


class SortOnPoffins_MainFlavor(IPoffinSortInterface):
    """Sort poffins by the their main flavor, in ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "main_flavor"

    @property
    def reverse(self):
        return self._reverse


class SortOnPoffins_Level(IPoffinSortInterface):
    """Sort poffins by the their level, in descending order.

            * Higher is better.
            * List in Descending Order
            * Same as Main Flavor Value

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "level"

    @property
    def reverse(self):
        return not self._reverse


class SortOnPoffins_SecondLevel(IPoffinSortInterface):
    """Sort poffins by the their second level, in desceding order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "second_level"

    @property
    def reverse(self):
        return not self._reverse


class SortOnPoffins_Name(IPoffinSortInterface):
    """Sort poffins by the their name, in ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "name"

    @property
    def reverse(self):
        return self._reverse


class SortOnPoffins_MainFlavorValue(IPoffinSortInterface):
    """Sort poffins by the value of their main flavor, in descending order.

            * Higher is better.
            * List in Descending Order
            * Same as Level

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "level"

    @property
    def reverse(self):
        return not self._reverse


class SortOnPoffins_NumFlavors(IPoffinSortInterface):
    """Sort poffins by the number of flavors. in descending order.

            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "num_flavors"

    @property
    def reverse(self):
        return not self._reverse


class SortOnPoffins_LevelToSmoothnessRatio(IPoffinSortInterface):
    """Sort poffins by the level / smoothness, in descending order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "level_to_smoothness_ratio"

    @property
    def reverse(self):
        return not self._reverse


class SortOnPoffins_LevelToSmoothnessRatioSum(IPoffinSortInterface):
    """Sort poffins by the sum of their levels / smoothness, in descending order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """
    @property
    def value(self):
        return "level_to_smoothness_ratio_sum"

    @property
    def reverse(self):
        return not self._reverse
