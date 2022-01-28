from operator import attrgetter

from make_poffins.poffin.interface_poffin_filter import IPoffinFilterInterface
from make_poffins.poffin.interface_poffin_sort import (
    IPoffinSortInterface, SortOnPoffins_MainFlavor)
from make_poffins.poffin.poffin import Poffin


# pylint: disable=too-few-public-methods
class _SortOnPoffins_Attrs(IPoffinSortInterface):
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
    @property
    def value(self):
        return self._value

    @property
    def reverse(self):
        return self._reverse

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        for key, reverse in reversed(self.value):
            poffins.sort(key=attrgetter(key), reverse=reverse)
        return poffins


class PoffinSortAndFilterSystem:
    def __init__(self, _filters: list[IPoffinSortInterface | IPoffinFilterInterface]):
        self._sort_filters = _filters
        self._split_and_reconstruct_sort_filters()

    def get_filtered_and_sorted_poffins(self, poffins: list[Poffin]) -> list[Poffin]:
        """Return filtered and sorted poffins based on the passed in rules

        Args:
            poffins (list[Poffin]): unfiltered, unsorted poffins

        Returns:
            list[Poffin]: filtered, sorted poffins
        """
        if self._sort_filters:
            for sort_filter in self._sort_filters:
                if not poffins:
                    return None
                poffins = sort_filter.execute(poffins)
            return poffins

    def _split_and_reconstruct_sort_filters(self):
        sorters = [s for s in self._sort_filters if isinstance(s, IPoffinSortInterface)]
        if sorters:
            self._sort_filters = [f for f in self._sort_filters if isinstance(f, IPoffinFilterInterface)]

            args = [(i.value, i.reverse) for i in sorters]
            self._sort_filters.append(_SortOnPoffins_Attrs(args))


if __name__ == "__main__":
    pass
