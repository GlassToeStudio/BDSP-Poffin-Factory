import time

from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.interface_berry_filter import \
    FilterBerriessBy_Rarity_GreaterThan
from make_poffins.berry.interface_berry_sort import SortOnBerry_Attrs
from make_poffins.poffin.interface_poffin_filter import (
    FilterPoffinsBy_AnyFlavorValueLessThan, FilterPoffinsBy_Level_LessThan,
    FilterPoffinsBy_MaxNSimilar, FilterPoffinsBy_NumberOfFlavors_LessThan)
from make_poffins.poffin.interface_poffin_sort import \
    SortOnPoffins_LevelToSmoothnessRatioSum
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem
from make_poffins.stats.contest_stats_factory import ContestStatsFactory
from make_poffins.stats.interface_contest_stats_filter import (
    FilterContestStatsBy_PoffinsEaten_GreaterThan,
    FilterContestStatsBy_Rank_GreaterThan)
from stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem


def main():
    no_berries_rarer_than = 15

    min_level = 50
    min_flavors = 2
    max_similar = 4
    min_value = 20

    min_rank = 1
    max_eaten = 20
    cook_time = 40
    top_x = 20

    # Berries
    berry_filters_sorters = [
        FilterBerriessBy_Rarity_GreaterThan(no_berries_rarer_than),
        SortOnBerry_Attrs((('main_flavor', False), ('smoothness', False),  ('_weakened_main_flavor_value', False))),
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system)
    berry_combinations = berry_factory.get_berry_combinations_4()

    # Poffins
    poffin_filters_sorters = [
        FilterPoffinsBy_Level_LessThan(min_level),
        FilterPoffinsBy_NumberOfFlavors_LessThan(min_flavors),
        SortOnPoffins_LevelToSmoothnessRatioSum(),
        FilterPoffinsBy_MaxNSimilar(max_similar),
        FilterPoffinsBy_AnyFlavorValueLessThan(min_value)
    ]
    poffin_filtering_sorting_system = PoffinSortAndFilterSystem(poffin_filters_sorters)
    poffin_factory = PoffinFactory(PoffinCooker(cook_time), berry_combinations, poffin_filtering_sorting_system)
    poffin_permutations = poffin_factory.get_poffin_permutations_4()

    # Stats
    contest_stats_filters_sorters = [
        FilterContestStatsBy_PoffinsEaten_GreaterThan(max_eaten),
        FilterContestStatsBy_Rank_GreaterThan(min_rank)
    ]
    contest_stats_filtering_sorting_system = ContestStatsSortAndFilterSystem(contest_stats_filters_sorters)
    contest_stat_factory = ContestStatsFactory(poffin_permutations, contest_stats_filtering_sorting_system, top_x, min_rank, max_eaten)
    final_stats = contest_stat_factory.get_filtered_and_sorted_contest_stats()

    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:
        print("Lets see the results!\n\n\n")
        if len(final_stats) > 0:
            print(str(final_stats[0]), file=print_file)
            for stat in final_stats:
                print(stat)
            print('\n'*10)
            print(str(final_stats[0]))
            print(repr(final_stats[0]))


if __name__ == "__main__":
    main()
