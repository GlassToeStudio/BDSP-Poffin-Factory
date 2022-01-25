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

    @abstractmethod
    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnPoffins_Attrs(IPoffinSortInterface):
    """Sort poffins by multiple values in ascending (False) or descenidng (True) order.

    Format = (('attr', Reversed?), ('name', False))

    Notes;\n
            * H: means Higher is better so supply True to the second argument
                - (("coolness", True), )
            * L: means Lower is better so supply False to the second argument
                - (("rarity", False), )
            *  : means neither is better - False for ascending, True for descending
                - (("rarity", False), )
    Attr:
        *  0 | int : smoothness    * L\n
        *  1 | int : main_flavor   *  \n
        *  2 | int : level         * H\n
        *  3 | int : second_level  * H\n
        *  4 | int : name          *  \n
        *  5 | int : num_flavors   *  \n
        *  6 | int : rarity        * L\n
        *  7 | int : __id__ *      *  \n

    https://docs.python.org/3/howto/sorting.html

    Returns:
        list[Poffins]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        for key, reverse in reversed(self._value):
            poffins.sort(key=attrgetter(key), reverse=reverse)
        return poffins


class SortOnPoffins_Smoothness(IPoffinSortInterface):
    """Sort poffins by the value of their smoothness, in ascending order.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.smoothness, reverse=self._reverse)


class SortOnPoffins_MainFlavor(IPoffinSortInterface):
    """Sort poffins by the their main flavor, in ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.main_flavor, reverse=self._reverse)


class SortOnPoffins_Level(IPoffinSortInterface):
    """Sort poffins by the their level, in descending order.

            * Higher is better.
            * List in Descending Order
            * Same as Main Flavor Value

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.level, reverse=not self._reverse)


class SortOnPoffins_SecondLevel(IPoffinSortInterface):
    """Sort poffins by the their second level, in desceding order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.second_level, reverse=not self._reverse)


class SortOnPoffins_Name(IPoffinSortInterface):
    """Sort poffins by the their name, in ascending alphabetical order.

            * List in Ascending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.name, reverse=self._reverse)


class SortOnPoffins_MainFlavorValue(IPoffinSortInterface):
    """Sort poffins by the value of their main flavor, in descending order.

            * Higher is better.
            * List in Descending Order
            * Same as Level

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.level, reverse=not self._reverse)


class SortOnPoffins_NumFlavors(IPoffinSortInterface):
    """Sort poffins by the number of flavors. in descending order.

            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.num_flavors, reverse=not self._reverse)


class SortOnPoffins_LevelToSmoothnessRatio(IPoffinSortInterface):
    """Sort poffins by the level / smoothness, in descending order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: x.level / x.smoothness, reverse=not self._reverse)


class SortOnPoffins_LevelToSmoothnessRatioSum(IPoffinSortInterface):
    """Sort poffins by the sum of their levels / smoothness, in descending order.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[Poffin]: sorted list of poffins
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: ((x.level / x.smoothness) + (x.second_level / x.smoothness)), reverse=not self._reverse)
