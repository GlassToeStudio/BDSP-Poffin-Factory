from abc import ABCMeta, abstractmethod

from make_poffins.berry import berry_factory
from make_poffins.poffin import poffin_sorter
from make_poffins.poffin.poffin import Poffin

# pylint: disable=too-few-public-methods


class PoffinFilterData:
    def __init__(self, level, flavor, num_flavors, min_flavor_value, num_same):
        self.level = level
        self.flavor = flavor
        self.num_flavors = num_flavors
        self.min_flavor_value = min_flavor_value
        self.num_same = num_same


class IPoffinSortInterface(metaclass=ABCMeta):

    @abstractmethod
    def sort(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnPoffinMainFlavor(IPoffinSortInterface):
    """Create an ISortInterface to sort by main flavor value."""

    def sort(self, poffins: list[Poffin]) -> list[Poffin]:
        """Sort poffins by the value of their main flavor. Higher is better.

        Args:
            poffins (list[Poffin]): unsorted list of poffins

        Returns:
            list[Poffin]: sorted list of poffins
        """
        return sorted(poffins, key=lambda x: -x.level)


class SortOnPoffinSmoothness(IPoffinSortInterface):
    """Create an ISortInterface to sort by main poffin smoothness."""

    def sort(self, poffins: list[Poffin]) -> list[Poffin]:
        """Sort poffins by the value of their smoothness. Higher is better.

        Args:
            poffins (list[Poffin]): unsorted list of poffins

        Returns:
            list[Poffin]: sorted list of poffins
        """
        return sorted(poffins, key=lambda x: -x.smoothness)


class SortOnPoffinLevelToSmoothnessRatio(IPoffinSortInterface):
    def sort(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -x.level / x.smoothness)


class SortOnPoffinLevelToSmoothnessRatioSum(IPoffinSortInterface):
    def sort(self, poffins: list[Poffin]) -> list[Poffin]:
        return sorted(poffins, key=lambda x: -((x.level / x.smoothness) + (x.second_level / x.smoothness)))


class IPoffinFilterInterface(metaclass=ABCMeta):

    @abstractmethod
    def filter(self, poffins: list[Poffin], *args) -> list[Poffin]:
        raise NotImplementedError


class FilterPoffinsByLevel(IPoffinFilterInterface):
    def filter(self, poffins: list[Poffin], *args: int) -> list[Poffin]:
        return [p for p in poffins if p.level >= args[0]]


class FilterPoffinsByFlavor(IPoffinFilterInterface):
    def filter(self, poffins: list[Poffin], *args: str) -> list[Poffin]:
        return [p for p in poffins if p.main_flavor.lower() == args[0].lower()]


class FilterPoffinsByNumberOfFlavors(IPoffinFilterInterface):
    def filter(self, poffins: list[Poffin], *args: int) -> list[Poffin]:
        return [p for p in poffins if p.__num_flavors__() >= args[0]]


class FilterPoffinsByAnyFlavorValueLessThan(IPoffinFilterInterface):
    def filter(self, poffins: list[Poffin], *args: int) -> list[Poffin]:
        temp_list = poffins.copy()
        for p in temp_list:
            for i in range(5):
                if 0 < p.flavor_values[i] < args[0]:
                    poffins.remove(p)
                    break
        return poffins


class FilterPoffinsToMaxNSimilar(IPoffinFilterInterface):
    def filter(self, poffins: list[Poffin], *args: int) -> list[Poffin]:
        dict_similar_poffin_count = {}
        poffins_copy = poffins.copy()
        for similar_poffins in poffins_copy:
            hahsable_poffin_values = tuple(similar_poffins.flavor_values)
            if hahsable_poffin_values in dict_similar_poffin_count:
                if dict_similar_poffin_count[hahsable_poffin_values] == args[0]:
                    poffins.remove(similar_poffins)
                    continue
                dict_similar_poffin_count[hahsable_poffin_values] += 1
            else:
                dict_similar_poffin_count[hahsable_poffin_values] = 1
        return poffins


class PoffinSortBuilder:
    def __init__(self, sorters: list[IPoffinSortInterface]):
        self.__sorters__ = sorters

    def get_sorted_poffins(self, poffins: list[Poffin]) -> list[Poffin]:
        for sorter in self.__sorters__:
            poffins = sorter.sort(poffins)
        return poffins


class PoffinSorter():
    """A class with functionality to sort poffins on various attributes"""

    # Sorters
    @staticmethod
    def sort_on_main_flavor_value(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their main flavor value.

        If value == True, list is in descending order (higher is better)

        If value == False, list is in ascending order (lower is berrer)

        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.level, reverse=value)

    @staticmethod
    def sort_on_smoothness(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)

        If value == False, list is in ascending order (lower is berrer)

        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.smoothness, reverse=value)

    @staticmethod
    def sort_on_sum_of_main_flavor_smoothness_ratios(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)
        If value == False, list is in ascending order (lower is berrer)


        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: (x.level / x.smoothness)+(x.second_level / x.smoothness), reverse=value)  # noqa ES501

    @staticmethod
    def sort_on_main_flavor_smoothness_ratio(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)
        If value == False, list is in ascending order (lower is berrer)


        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.level / x.smoothness, reverse=value)  # noqa ES501

    @staticmethod
    def filter_poffins_by_flavor(poffins: list[Poffin], flavor: str) -> list[Poffin]:  # noqa ES501
        """Return the list of only <flavor> poffins."""

        return [p for p in poffins if p.main_flavor.lower() == flavor.lower()]  # noqa ES501

    # Filters
    @staticmethod
    def filter_poffins_by_level(poffins: list[Poffin], level: int) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins with a level >= level"""

        return [p for p in poffins if p.level >= level]  # noqa ES501

    @staticmethod
    def filter_by_num_flavors(poffins: list[Poffin], num_favors: int) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins with a number of flavors  >= num_favors"""  # noqa ES501

        return [p for p in poffins if p.__num_flavors__() >= num_favors]  # noqa ES501

    @staticmethod
    def filter_if_any_value_less_than(poffins: list[Poffin], min_flavor_value: int = 25) -> list[Poffin]:  # noqa ES501
        """Remove any poffin from the list if one of their non-zero flavor values is < min_flavor_value"""  # noqa ES501

        temp_list = poffins.copy()
        for p in temp_list:
            for i in range(5):
                if 0 < p.flavor_values[i] < min_flavor_value:
                    poffins.remove(p)
                    break
        return poffins  # noqa ES501

    @staticmethod
    def filter_similar_poffins_to_four(poffins: list[Poffin]) -> list[Poffin]:
        dict_similar_poffin_count = {}
        poffins_copy = poffins.copy()
        for similar_poffins in poffins_copy:
            hahsable_poffin_values = tuple(similar_poffins.flavor_values)
            if hahsable_poffin_values in dict_similar_poffin_count:
                if dict_similar_poffin_count[hahsable_poffin_values] == 4:
                    poffins.remove(similar_poffins)
                    continue
                dict_similar_poffin_count[hahsable_poffin_values] += 1
            else:
                dict_similar_poffin_count[hahsable_poffin_values] = 1
        return poffins


if __name__ == "__main__":
    _poffins = [Poffin([148, 0, 0, 28, 0], 30, berry_factory.single_recipe),
                Poffin([148, 0, 0, 28, 0], 33, berry_factory.single_recipe),
                Poffin([5, 0, 0, 28, 0], 20, berry_factory.single_recipe),
                Poffin([168, 0, 0, 28, 0], 40, berry_factory.single_recipe)]
    sort_class1 = SortOnPoffinMainFlavor()
    sort_class2 = SortOnPoffinSmoothness()

    sorters = [sort_class1, sort_class2]
    poffin_sorter = PoffinSortBuilder(sorters)
    _poffins = poffin_sorter.get_sorted_poffins(_poffins)
    print(_poffins)
    print(sort_class1)
