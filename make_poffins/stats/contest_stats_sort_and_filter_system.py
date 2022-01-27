from operator import attrgetter

from make_poffins.stats.contest_stats import ContestStats
from make_poffins.stats.interface_contest_stats_filter import \
    IContestStatsFilterInterface
from make_poffins.stats.interface_contest_stats_sort import \
    IContestStatsSortInterface

# pylint: disable=too-few-public-methods


class _SortOnContestStats_Attrs(IContestStatsSortInterface):
    """Sort contst stats by multiple values in ascending (False) or descenidng (True) order.

        - Format = (('attr', Reversed?), ('name', False))

    Notes;\n
            * H: means Higher is better so supply True to the second argument
                - (("coolness", True), )\n
            * L: means Lower is better so supply False to the second argument
                - (("rarity", False), )\n

    Attr:
        *  0 | int : coolness           * H\n
        *  1 | int : beauty             * H\n
        *  2 | int : cuteness           * H\n
        *  3 | int : cleverness         * H\n
        *  4 | int : toughness          * H\n
        *  5 | int : sheen              * H\n
        *  6 | int : rank               * L\n
        *  7 | int : rarity             * L\n
        *  8 | int : poffins_eaten      * L\n
        *  9 | int : unique_berries     * L\n
        * 10 | int : num_perfect_values * H\n

    https://docs.python.org/3/howto/sorting.html

    Returns:
        list[ContestStats]: sorted list of contest stats
    """
    @property
    def value(self):
        return self._value

    @property
    def reverse(self):
        return self._reverse

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        for key, reverse in reversed(self.value):
            contest_stats.sort(key=attrgetter(key), reverse=reverse)
        return contest_stats


class ContestStatsSortAndFilterSystem:
    """System to process a lsit of ContestStats through numerous filters and sorting rules.

        Filters:\n
                * Rank\n
                * Rarity\n
                * Poffins Eaten\n
    """

    def __init__(self, sort_filters: list[IContestStatsSortInterface | IContestStatsFilterInterface]):
        self._sort_filters = sort_filters
        self._filters: list[IContestStatsFilterInterface] = []
        self._split_and_reconstruct_sort_filters()

    @property
    def filters(self):
        return self._filters

    def get_sorted_and_filtered_contest_stats(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        """Return filtered and sorted contest stats based on the passed in rules

        Args:
            contest_stats (list[ContestStats]): unfiltered, unsorted contest stats

        Returns:
            list[ContestStats]: filtered, sorted contest stats
        """

        if self._sort_filters:
            for sort_filter in self._sort_filters:
                if not contest_stats:
                    return None
                contest_stats = sort_filter.execute(contest_stats)
            return contest_stats

    def _split_and_reconstruct_sort_filters(self):
        self._filters = [f for f in self._sort_filters if isinstance(f, IContestStatsFilterInterface)]
        sorters = [s for s in self._sort_filters if isinstance(s, IContestStatsSortInterface)]
        args = [(i.value, i.reverse) for i in sorters]
        for arg in args:
            print(arg)
        self._sort_filters.append(_SortOnContestStats_Attrs(args))


if __name__ == "__main__":
    pass
