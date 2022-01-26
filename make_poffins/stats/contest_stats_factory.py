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
        self.rule_dict = {}
        self._get_attr_name_from_Ifilter()

        # Only generated when get_filtered_and_sorted_contest_stats() is called.
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

        if self._filtered_contest_stats is None:

            print("None met the criteria")
            return None

        print(f"Returning {len(self._filtered_contest_stats)} Filtered Poffins")
        return self._filtered_contest_stats

    @calculate_time
    @cache
    def _generate_contest_stats(self) -> list[ContestStats]:
        running_count = 0
        self._contest_stats = []
        for poffin_combo in self._poffin_combos:
            running_count = stat_counter(running_count, 100000)

            current_stat = ContestStats(poffin_combo)

            # Test out new filter:
            if not self._check_rule(current_stat):
                continue

            # current_stat.apply_poffins(poffin_combo)

            # print("Sent", current_stat.poffins_eaten)
            # returned_current_stat = self._stats_filter_system.get_sorted_and_filtered_contest_stats([current_stat])

            # if returned_current_stat and len(returned_current_stat) > 0:
            # returned_current_stat = returned_current_stat[0]

            # print(f"Returned: eaten {str(returned_current_stat.poffins_eaten)}")
            # print(str(returned_current_stat))

            # else:
            # print("Stat did not meet criteria")
            # continue

            # TODO: This is cheating since we have a sorting/filtering system...
            # but why wait and do it later to numerous stats when we can just do
            # do it now and save some time ¯\_(ツ)_/¯

            # if current_stat.rank > self._min_rank or current_stat.poffins_eaten > self._max_eaten:
            # continue

            self._contest_stats.append(current_stat)

            # print(f"\tFound {len(self._contest_stats)} results so far!")
            if len(self._contest_stats) >= 10E6:  # TODO: Maybe not hard code this 🤔

                print("\t10000 records found! Exiting!")
                break

        self._contest_stats = sorted(self._contest_stats, key=lambda x: (x.rarity, x.unique_berries, -x.poffins_eaten))
        return self._contest_stats

    def _get_attr_name_from_Ifilter(self):
        """Loop through the filters and parse their Class.__name__ to extract the
        following values:

        Ex:
            FilterContestStatsBy_Rarity_LT
             - The passed in value: value - from the Class instance.\n
                * class_instance.value
             - The comparison operateor: >, < - from the last two characters of the Class name
                * GT or LT
             - The attribute name: 'name' from the 21:-3 character of the Class name
                * 'rarity'

        Info:
            given_value = i.value\n
            to_parse = i.__class__.__name__\n
            comp = to_parse[-2:]\n
            attribute_name = to_parse[21:-3].lower()\n

        Store these values in a dict with:
             * key = Class.__name__
             * values = (attribute name, compariosn, instance.value)
        """
        for i in self._stats_filter_system.filters:
            self.rule_dict[str(i)] = (str(i)[21:-3].lower(),  str(i)[-2:], i._value)

    def _check_rule(self, cs):
        """Check the contest stat against ther rules saved in the rile dict.

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
        for _, values in self.rule_dict.items():
            attribute_name, comp, cs_value = values
            attribute_value = getattr(cs, attribute_name)
            if cs_value == attribute_value:
                # print(f"{attribute_name} : {cs_value} == {attribute_value} {True}")
                continue
            elif comp == "LT":
                # If my value is greater than, keep it.
                # print(f"{attribute_name} : {cs_value} > {attribute_value} {cs_value > attribute_value}")
                keep = cs_value > attribute_value
            else:
                # If my value is less than, keep it
                # print(f"{attribute_name} : {cs_value} < {attribute_value} {cs_value < attribute_value}")
                keep = cs_value < attribute_value
            if not keep:
                return keep
        return keep

    @calculate_time
    def get_filtered_and_sorted_contest_stats(self):
        return self.filtered_contest_stats
