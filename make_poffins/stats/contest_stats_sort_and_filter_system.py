from make_poffins.stats.contest_stats import ContestStats
from make_poffins.stats.interface_contest_stats_filter import \
    IContestStatsFilterInterface
from make_poffins.stats.interface_contest_stats_sort import \
    IContestStatsSortInterface

# pylint: disable=too-few-public-methods


class ContestStatsSortAndFilterSystem:
    def __init__(self, filters: list[IContestStatsSortInterface | IContestStatsFilterInterface]):
        self._sort_filters = filters

    def get_sorted_and_filtered_contest_stats(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        """Get the Filtered and Sorted contest stats."""
        for sort_filter in self._sort_filters:
            stats = sort_filter.execute(contest_stats)
        return stats


if __name__ == "__main__":
    pass
