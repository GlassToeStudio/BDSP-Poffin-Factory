import multiprocessing as mp
from tqdm import tqdm  # pip install tqdm

from make_poffins.constants import (TOTAL_POFFINS, calculate_time)
from make_poffins.contest_stats.contest_stats import ContestStats
from make_poffins.contest_stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.poffin.poffin import Poffin

# This worker function must be at the top level of the module to be pickled


def _worker_task(args):
    """
    Processes a single poffin combo against a set of filters.
    Returns the ContestStats object if it passes, otherwise None.
    """
    poffin_combo, filter_dict = args
    stat = ContestStats(poffin_combo)

    # This logic is moved from _passes_all_filters for use in the parallel worker
    for _, filter_data in filter_dict.items():
        attribute, op, value = filter_data
        attribute_value = getattr(stat, attribute)

        # op 0 is 'less than', op 1 is 'greater than'
        # The filter keeps values that are NOT less than (i.e., >=) or NOT greater than (i.e., <=)
        if op == 0 and (attribute_value < value):
            return None  # Failed 'less than' filter
        if op == 1 and (attribute_value > value):
            return None  # Failed 'greater than' filter

    return stat


class ContestStatsFactory():
    def __init__(self, poffin_combos: list[tuple[Poffin]], stats_filter_system: ContestStatsSortAndFilterSystem):
        self._poffin_combos = poffin_combos
        self._stats_filter_system = stats_filter_system
        self._filter_dict = {}
        self._filtered_sorted_contest_stats = []
        self.num_poffins = int(TOTAL_POFFINS[0]) if TOTAL_POFFINS[0] > 0 else len(
            self._poffin_combos)

        if self._stats_filter_system.filters:
            self._construct_filter_dict()
        print("\nSetting Up StatsFactory\n")

    @property
    def filtered_sorted_contest_stats(self) -> list[ContestStats]:
        """
        Generates, filters, and sorts contest stats in a single, efficient pipeline.
        """
        if not self._filtered_sorted_contest_stats:
            # 1. Generate and filter stats in parallel
            filtered_stats = self._generate_and_filter_stats_parallel()

            # 2. Sort the filtered results
            print(f"Sorting {len(filtered_stats)} Contest Stats...")
            self._filtered_sorted_contest_stats = self._stats_filter_system.get_filtered_and_sorted_contest_stats(
                filtered_stats)

        print(
            f"Returning {0 if not self._filtered_sorted_contest_stats else len(self._filtered_sorted_contest_stats)} sorted Contest Stats")
        return self._filtered_sorted_contest_stats

    @calculate_time
    def _generate_and_filter_stats_parallel(self) -> list[ContestStats]:
        """
        Uses a multiprocessing Pool and tqdm for efficient processing with a progress bar.
        """
        cores = mp.cpu_count() - 1
        args_iterator = ((combo, self._filter_dict)
                         for combo in self._poffin_combos)

        print(f"Starting parallel processing on {cores} cores...")

        with mp.Pool(processes=cores) as pool:
            # Use imap_unordered to process the tasks and get a progress bar with tqdm
            # The list() call forces the iterator to be consumed, running all tasks.
            results = list(tqdm(pool.imap_unordered(
                _worker_task, args_iterator), total=self.num_poffins, desc="Calculating Stats"))

        # Filter out the None values from workers that didn't pass the filter
        return [stat for stat in results if stat is not None]

    def _construct_filter_dict(self):
        """
        Construct a filter dictionary from the data provided by the available filters.
        """
        self._filter_dict = {str(filter): (filter.attribute,  filter.op, filter.value)
                             for filter in self._stats_filter_system.filters}
