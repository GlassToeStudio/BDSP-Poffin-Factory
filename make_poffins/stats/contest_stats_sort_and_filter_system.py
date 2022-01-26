from copy import deepcopy
from os import stat

from make_poffins.stats.contest_stats import ContestStats
from make_poffins.stats.interface_contest_stats_filter import \
    IContestStatsFilterInterface
from make_poffins.stats.interface_contest_stats_sort import \
    IContestStatsSortInterface

# pylint: disable=too-few-public-methods


class ContestStatsSortAndFilterSystem:
    """System to process a lsit of ContestStats through numerous filters and sorting rules.

        Filters:\n
                * Rank\n
                * Rarity\n
                * Poffins Eaten\n
    """

    def __init__(self, sort_filters: list[IContestStatsSortInterface | IContestStatsFilterInterface]):
        self._sort_filters = sort_filters
        self._sorters: list[IContestStatsSortInterface] = []
        self._filters: list[IContestStatsFilterInterface] = []
        self._split_filters_and_sorters()

    @property
    def filters(self):
        return self._filters

    def get_sorted_and_filtered_contest_stats(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        """Get the Filtered and Sorted contest stats."""
        if not self._sorters:
            return None

        for sorter in self._sorters:
            if not contest_stats:
                return None
            contest_stats = sorter.execute(contest_stats)
        return contest_stats

    def _split_filters_and_sorters(self):
        for f_s in self._sort_filters:
            if isinstance(f_s, IContestStatsFilterInterface):
                self._filters.append(f_s)
            elif isinstance(f_s, IContestStatsSortInterface):
                self._sorters.append(f_s)


if __name__ == "__main__":
    pass
