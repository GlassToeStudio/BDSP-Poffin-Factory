import pickle

from make_poffins.berry import berry_library
from make_poffins.constants import FLAVORS
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_library import poffin_library
from make_poffins.stats.contest_stats_factory import ContestStatsFactory
from make_poffins.stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.stats.interface_contest_stats_sort import (
    SortOnContestStats_PoffinsEaten, SortOnContestStats_Rarity)


def test_pickle_berry():
    berry = berry_library.aguav_berry
    pickled_berry = pickle.dumps(berry)


def test_pickle_poffin():
    poffin = poffin_library.petaya_apicot_custap_colbur_poffin
    pickled_poffin = pickle.dumps(poffin)


def test_pickle_contests_stats():
    poffin_list = poffin_library.generate_random_poffin_list_n_of_each(5, FLAVORS)
    poffin_combos = PoffinFactory.generate_poffin_combinations_r(poffin_list, 3)

    sorters = [
        SortOnContestStats_Rarity(),
        SortOnContestStats_PoffinsEaten(),
    ]
    sorting_system = ContestStatsSortAndFilterSystem(sorters)
    stat_factory = ContestStatsFactory(poffin_combos, sorting_system)
    final_stats = stat_factory.filtered_sorted_contest_stats

    #_ = [print(str(p)) for p in final_stats]


if __name__ == '__main__':
    test_pickle_contests_stats()
