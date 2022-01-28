import multiprocessing as mp
from functools import cache

from make_poffins.constants import (TOTAL_POFFINS, calculate_time, chunks,
                                    stat_counter)
from make_poffins.contest_stats.contest_stats import ContestStats
from make_poffins.contest_stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.poffin.poffin import Poffin


class ContestStatsFactory():
    def __init__(self, poffin_combos: list[tuple[Poffin]], stats_filter_system: ContestStatsSortAndFilterSystem):
        # passed in
        self._poffin_combos = poffin_combos
        self._stats_filter_system = stats_filter_system
        self._filter_dict = {}
        self._filtered_contest_stats = []
        self._filtered_sorted_contest_stats = []
        self.num_poffins = int(TOTAL_POFFINS[0])
        self.running_count = 0
        if self._stats_filter_system.filters:
            self._construct_filter_dict()
        print("\nSetting Up StatsFactory\n")

    @property
    def filtered_contest_stats(self) -> list[ContestStats]:
        """List of filtered contest stats from the given list of poffins

        Note:\n
                * Contest stats are filtered upon creation.
                * Internal cutoff @ 10E6 records
                * Internal min rank @ 1
                * Internal max eaten @ 20

        Returns:
            list[ContestStats]: Unfiltered and Unsorted Contest Stats List
        """

        if not self._filtered_contest_stats:
            self._filtered_contest_stats = self._generate_contest_stats_parallel()

        return self._filtered_contest_stats

    @property
    def filtered_sorted_contest_stats(self) -> list[ContestStats]:
        """List of filtered and sorted contest stats from the given list of poffins

        Note:\n
                * Internal cutoff @ 10E6 records

        Returns:
            list[ContestStats]: Filtered and Sorted Contest Stats List
        """

        if not self._filtered_sorted_contest_stats:
            self._filtered_sorted_contest_stats = self._stats_filter_system.get_filtered_and_sorted_contest_stats(self.filtered_contest_stats)
        print(f"Returning {0 if not self._filtered_sorted_contest_stats else len(self._filtered_sorted_contest_stats)} sorted Contest Stats")
        return self._filtered_sorted_contest_stats

    @calculate_time
    def _generate_contest_stats_serial(self) -> list[ContestStats]:

        for poffin_combo in self._poffin_combos:
            current_stat = ContestStats(poffin_combo)
            #self.running_count = stat_counter(self.running_count, self.num_poffins, 1, 5000)
            if self._passes_all_filters(current_stat):
                self._filtered_contest_stats.append(current_stat)

            if len(self._filtered_contest_stats) >= 10E6 or self.running_count >= 10E6:  # NOTE: Maybe not hard code this 🤔
                #self.running_count = stat_counter(self.running_count, self.num_poffins, 1, 1)
                return self._filtered_contest_stats

        #self.running_count += stat_counter(self.running_count, self.num_poffins, 1, 1)
        return self._filtered_contest_stats

    @calculate_time
    def _generate_contest_stats_parallel(self) -> list[ContestStats]:
        processed_list = mp.Manager().list()
        processes = []
        chunk_size = int(self.num_poffins//mp.cpu_count())

        for i, poffin_chunk in enumerate(chunks(self._poffin_combos, chunk_size)):
            if i % chunk_size == 0:
                p = mp.Process(target=self._parallel_task, args=(poffin_chunk, processed_list))
                processes.append(p)
                p.start()

        for process in processes:
            process.join()

        self._filtered_contest_stats = processed_list
        return self._filtered_contest_stats

    def _parallel_task(self, poffin_chunks, shared_list):
        for poffin_combo in poffin_chunks:
            current_stat = ContestStats(poffin_combo)
            if self._passes_all_filters(current_stat):
                shared_list.append(current_stat)

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

    def _passes_all_filters(self, cs: ContestStats):
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
            if value != attribute_value:
                if op == 0:
                    keep = attribute_value > value  # If attribute > value, Keep it.
                else:
                    keep = attribute_value < value  # If attribute < value, Keep it.
            if not keep:
                return keep
        return keep
