from functools import cache

from make_poffins.constants import calculate_time, stat_counter
from make_poffins.poffin.poffin import Poffin
from make_poffins.stats.contest_stats import ContestStats
from make_poffins.stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.stats.interface_contest_stats_filter import \
    IContestStatsFilterInterface


class ContestStatsFactory():
    def __init__(self, poffin_combos: list[tuple[Poffin]], stats_filter_system: ContestStatsSortAndFilterSystem):
        # passed in
        self._poffin_combos = poffin_combos
        self._stats_filter_system = stats_filter_system

        # For filtering
        self._filter_dict = {}
        if self._stats_filter_system.filters:
            self._construct_filter_dict()

        self._contest_stats = []
        self._filtered_contest_stats = []
        print("\nSetting Up StatsFactory")

    @property
    def contest_stats(self) -> list[ContestStats]:
        """List of all contest stats from the given list of poffins

        Note:\n
                * Internal cutoff @ 10E6 records
                * Internal min rank @ 1
                * Internal max eaten @ 20

        Returns:
            list[ContestStats]: Unfiltered and Unsorted Contest Stats List
        """

        if self._contest_stats is None:
            self._contest_stats = self._generate_contest_stats()

        print(f"Returning {len(self._contest_stats)} UNFILTERED Contest Stats!")
        return self._contest_stats

    @property
    def filtered_contest_stats(self) -> list[ContestStats]:
        """List of foltered and sorted contest stats from the given list of poffins

        Note:\n
                * Internal cutoff @ 10E6 records
                * Internal min rank @ 1
                * Internal max eaten @ 20

        Returns:
            list[ContestStats]: Filtered and Sorted Contest Stats List
        """
        if self._filtered_contest_stats is None:
            self._filtered_contest_stats = self._stats_filter_system.get_filtered_and_sorted_contest_stats(self.contest_stats)

         print(f"Returning {None if self._filtered_contest_stats is None else len(self._filtered_contest_stats)} Filtered Contest Stats")
        return self._filtered_contest_stats

    @calculate_time
    @cache
    def _generate_contest_stats(self) -> list[ContestStats]:
        running_count = 0
        for poffin_combo in self._poffin_combos:
            running_count = stat_counter(running_count, 100000)
            current_stat = ContestStats(poffin_combo)
            if not self._check_rule(current_stat):
                continue

            self._contest_stats.append(current_stat)
            if len(self._contest_stats) >= 10E6 or running_count >= 10E6:  # TODO: Maybe not hard code this 🤔
                return self._contest_stats

        return self._contest_stats

    def _construct_filter_dict(self):
        """Construct a filter disctionary from the data provide by the available filters

        Info:
            attribute = filter.attribute\n
            op = filter.op  < or >\n
            value = filter.value\n

        Store these values in a dict with:
             * key = Class.__name__
             * values = (attribute, op, value)
        """

        self._filter_dict = {str(filter): (filter.attribute,  filter.op, filter.value) for filter in self._stats_filter_system.filters}

    def _check_rule(self, cs: ContestStats):
        """Check the contest stat against ther filters saved in the filter dict.

        If any result is False, return false as this stat does not pass all
        the filters.

        Notes:\n
                    * False means do NOT pass

        Args:
            cs (ContestStat): The contest stat for which we might filter out

        Returns:
            bool: True if passed all filters else False
        """
        keep = True
        for _, filter_data in self._filter_dict.items():
            attribute, op, value = filter_data
            attribute_value = getattr(cs, attribute)
            if value == attribute_value:
                # print(f"{attribute_name} : {cs_value} == {attribute_value} {True}")
                continue
            elif op == 0:
                # If value is greater than, keep it.
                # print(f"{attribute_name} : {cs_value} > {attribute_value} {cs_value > attribute_value}")
                keep = value > attribute_value
            else:
                # If value is less than, keep it
                # print(f"{attribute_name} : {cs_value} < {attribute_value} {cs_value < attribute_value}")
                keep = value < attribute_value
            if not keep:
                return keep
        return keep
