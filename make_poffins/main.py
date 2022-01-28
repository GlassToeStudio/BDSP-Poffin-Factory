import time

from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.interface_berry_filter import (
    FilterBerriesBy_Smoothness_LessThan, FilterBerriessBy_Rarity_GreaterThan,
    FilterBerriessBy_Rarity_LessThan)
from make_poffins.berry.interface_berry_sort import (
    SortOnBerry__Weakened_Main_Flavor_Value, SortOnBerry_Main_Flavor_Value,
    SortOnBerry_Name, SortOnBerry_Rarity)
from make_poffins.constants import calculate_time
from make_poffins.poffin.interface_poffin_filter import (
    FilterPoffinsBy_AnyFlavorValueLessThan, FilterPoffinsBy_Level_LessThan,
    FilterPoffinsBy_MaxNSimilar, FilterPoffinsBy_NumberOfFlavors_LessThan)
from make_poffins.poffin.interface_poffin_sort import (
    SortOnPoffins_Level, SortOnPoffins_LevelToSmoothnessRatioSum)
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_library import poffin_library
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem
from make_poffins.stats.contest_stats_factory import ContestStatsFactory
from make_poffins.stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.stats.interface_contest_stats_filter import (
    FilterContestStatsBy_Poffins_Eaten_GT, FilterContestStatsBy_Rank_GT)
from make_poffins.stats.interface_contest_stats_sort import (
    SortOnContestStats_NumUniqueBerries, SortOnContestStats_PoffinsEaten,
    SortOnContestStats_Rarity)


@calculate_time
def main():
    # Berries
    berry_filters_sorters = [
        SortOnBerry_Rarity(),
        SortOnBerry_Name(),
        FilterBerriessBy_Rarity_LessThan(7)
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system)
    berry_combinations = berry_factory.get_berry_combinations_4()

    # Poffins
    poffin_filters_sorters = [
        FilterPoffinsBy_Level_LessThan(100),
        FilterPoffinsBy_NumberOfFlavors_LessThan(3),
        FilterPoffinsBy_MaxNSimilar(4),
        FilterPoffinsBy_AnyFlavorValueLessThan(20),
        SortOnPoffins_LevelToSmoothnessRatioSum()
    ]
    poffin_filtering_sorting_system = PoffinSortAndFilterSystem(poffin_filters_sorters)
    poffin_factory = PoffinFactory(PoffinCooker(38.5), berry_combinations, poffin_filtering_sorting_system)
    poffin_permutations = poffin_factory.get_poffin_permutations_3()

    # Stats
    contest_stats_filters_sorters = [
        FilterContestStatsBy_Poffins_Eaten_GT(9),
        FilterContestStatsBy_Rank_GT(1),
        SortOnContestStats_Rarity(),
        SortOnContestStats_PoffinsEaten(),
        SortOnContestStats_NumUniqueBerries()
    ]
    contest_stats_filtering_sorting_system = ContestStatsSortAndFilterSystem(contest_stats_filters_sorters)
    contest_stat_factory = ContestStatsFactory(poffin_permutations, contest_stats_filtering_sorting_system)
    final_stats = contest_stat_factory.filtered_sorted_contest_stats

    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:
        if final_stats:
            print("Lets see the results!\n\n\n")
            for stat in final_stats:
                print(stat, file=print_file)
            print('\n'*10, file=print_file)
            print(str(final_stats[0]))
            print(str(final_stats[0]), file=print_file)

            # for stat in final_stats[:100]:
            #    print(stat)
            # for stat in final_stats[:10]:
            # print(repr(stat))
        else:
            print("No results")


if __name__ == "__main__":
    main()
