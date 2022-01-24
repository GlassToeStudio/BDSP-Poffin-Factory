from functools import cache

from make_poffins.poffin.poffin import Poffin
from make_poffins.stats.contest_stats import ContestStats
from make_poffins.stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem


class ContestStatsFactory():
    def __init__(self, poffin_combos: list[tuple[Poffin]], stats_filter_system: ContestStatsSortAndFilterSystem = None, _top_x=10, _min_rank: int = 1, _max_eaten: int = 10, print_file=None):  # noqa ES501
        self._poffin_combos = poffin_combos
        self._stats_filter_system = stats_filter_system

        self._contest_stats = None
        self._filtered_contest_stats = None
        print("\nSetting Up StatsFactory")

    @property
    def contest_stats(self) -> list[ContestStats]:
        """List of all contest stats from the given list of poffins

        Note:\n
                * Internal cutoff @ 100 records
                * Internal min rank @ 1
                * Internal max eaten @ 20

        Returns:
            list[ContestStats]: Unfilter and Unsorted Contest Stats List
        """
        print("Trying to Get the Contest Stats List", self._contest_stats)

        if self._contest_stats is None:
            print("Contest Stats are Empty")

            self._contest_stats = self._generate_contest_stats()
        print(f"Returning {len(self._contest_stats)} Contest Stats!")

        return self._contest_stats

    @property
    def filtered_contest_stats(self) -> list[ContestStats]:
        """List of foltered and sorted contest stats from the given list of poffins

        Note:\n
                * Internal cutoff @ 100 records
                * Internal min rank @ 1
                * Internal max eaten @ 20

        Returns:
            list[ContestStats]: Filtered and Sorted Contest Stats List
        """
        print("Trying to Get Filtered Poffins")

        if self._filtered_contest_stats is None:
            print("Have to Generate Contest Stats")

            self._filtered_contest_stats = self._stats_filter_system.get_sorted_and_filtered_contest_stats(self.contest_stats)

        print(f"Returning {len(self._filtered_contest_stats)} Filtered Poffins")

        return self._filtered_contest_stats

    @cache
    def _generate_contest_stats(self, _min_rank: int = 1, _max_eaten: int = 20) -> list[ContestStats]:
        self._contest_stats = []
        for poffin_combo in self._poffin_combos:
            current_stat = ContestStats()
            current_stat.apply_poffins(poffin_combo)

            # TODO: Do we filter here or later?
            if current_stat.rank > _min_rank or current_stat.poffins_eaten > _max_eaten:
                continue
            self._contest_stats.append(current_stat)

            if len(self._contest_stats) >= 100:
                print("\t100 records found! Exiting!")
                break

        self._contest_stats = sorted(self._contest_stats, key=lambda x: (x.rarity, x.unique_berries, -x.poffins_eaten))
        return self._contest_stats

    def get_filtered_and_sorted_contest_stats(self):
        return self.filtered_contest_stats
