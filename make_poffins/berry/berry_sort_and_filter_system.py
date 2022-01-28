# pylint: disable=too-few-public-methods
from operator import attrgetter

from make_poffins.berry import berry_library
from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_filter_interface import (
    FilterBerriessBy_Rarity_LessThan, IBerryFilterInterface)
from make_poffins.berry.berry_sort_interface import (IBerrySortInterface,
                                                     SortOnBerry_Name,
                                                     SortOnBerry_Rarity)


class _SortOnBerry_Attrs(IBerrySortInterface):
    """Sort berries by multiple values in ascending (False) or descenidng (True) order.

    Notes;\n
            * H: means Higher is better so supply True to the second argument
                - (("coolness", True), )
            * L: means Lower is better so supply False to the second argument
                - (("rarity", False), )
            *  : means neither is better - False for ascending, True for descending
                - (("rarity", False), )

    Attr:
        *  0 | str   : name                          *   \n
        *  1 | [int] : flavor_values                 * H \n
        *  2 | int   : smoothness                    * L \n
        *  3 | int   : main_flavor_value             * H \n
        *  4 | str   : main_flavor                   *   \n
        *  5 | int   : num_flavors                   * H \n
        *  6 | int   : rarity                        * L \n
        *  7 | [int] : _weakened_flavor_values       * H \n
        *  8 | int   : _weakened_main_flavor_value   * H \n
        *  9 | int   : _weakened_main_flavor         *   \n
        * 10 | int   : __id__                        *   \n

    https://docs.python.org/3/howto/sorting.html

    Returns:
        list[Berry]: sorted list of berries
    """
    @property
    def value(self):
        return self._value

    @property
    def reverse(self):
        return self._reverse

    def execute(self, berries: list[Berry]) -> list[Berry]:
        for key, reverse in reversed(self.value):
            berries.sort(key=attrgetter(key), reverse=reverse)
        return berries


class BerrySortAndFilterSystem:
    """Takes a list of IBerrySortInterface and IBerryFilterInterface rules and
    applies them to a list of berries.
    """

    def __init__(self, filters: list[IBerrySortInterface | IBerryFilterInterface]):
        self._sort_filters = filters
        self._split_and_reconstruct_sort_filters()

    def get_filtered_and_sorted_berries(self, berries: list[Berry]) -> list[Berry]:
        """Return filtered and sorted berries based on the passed in rules

        Args:
            berries (list[Berry]): unfiltered, unsorted berries

        Returns:
            list[Berry]: filtered, sorted berries
        """
        if self._sort_filters:
            for sort_filter in self._sort_filters:
                if not berries:
                    return None
                berries = sort_filter.execute(berries)
        return berries

    def _split_and_reconstruct_sort_filters(self):
        sorters = [s for s in self._sort_filters if isinstance(s, IBerrySortInterface)]
        if sorters:
            self._sort_filters = [f for f in self._sort_filters if isinstance(f, IBerryFilterInterface)]

            args = [(i.value, i.reverse) for i in sorters]
            self._sort_filters.append(_SortOnBerry_Attrs(args))


if __name__ == "__main__":
    sorters = [
        SortOnBerry_Rarity(),
        SortOnBerry_Name(),
        FilterBerriessBy_Rarity_LessThan(4),
    ]
    bsf = BerrySortAndFilterSystem(sorters)
    berries = bsf.get_filtered_and_sorted_berries(berry_library.every_berry)
    for _ in berries:
        print(_)
