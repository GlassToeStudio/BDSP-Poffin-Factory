import time

from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import (
    RemoveBerriesWith_Rarity_GreaterThan, RemoveBerriesWith_Rarity_LessThan,
    RemoveBerriesWith_Smoothness_LessThan)
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (
    SortBerriesBy_Main_Flavor_Value, SortBerriesBy_Name, SortBerriesBy_Rarity,
    SortBerriesBy_Weakened_Main_Flavor_Value)
from make_poffins.constants import calculate_time
from make_poffins.contest_stats.contest_stats_factory import \
    ContestStatsFactory
from make_poffins.contest_stats.contest_stats_filter_interface import (
    RemoveContestStatsWith_PoffinsEaten_GreaterThan,
    RemoveContestStatsWith_Rank_GreaterThan)
from make_poffins.contest_stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.contest_stats.contest_stats_sort_interface import (
    SortContestStatsBy_NumUniqueBerries, SortContestStatsBy_PoffinsEaten,
    SortContestStatsBy_Rank, SortContestStatsBy_Rarity)
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_filter_interface import (
    RemovePoffinsWith_AnyFlavorValueLessThan, RemovePoffinsWith_Level_LessThan,
    RemovePoffinsWith_MaxNSimilar,
    RemovePoffinsWith_NumberOfFlavors_GreaterThan,
    RemovePoffinsWith_NumberOfFlavors_LessThan,
    RemovePoffinsWith_SecondLevel_LessThan)
from make_poffins.poffin.poffin_library import poffin_library
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem
from make_poffins.poffin.poffin_sort_interface import (
    SortPoffinsBy_Level, SortPoffinsBy_LevelToSmoothnessRatioSum)


@calculate_time
def main():
    # Berries
    berry_filters_sorters = [
        RemoveBerriesWith_Rarity_LessThan(3),
        RemoveBerriesWith_Rarity_GreaterThan(11),
        SortBerriesBy_Rarity(),
        SortBerriesBy_Name()
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system)
    berry_combinations = berry_factory.get_berry_combinations_4()

    # Poffins
    poffin_filters_sorters = [
        RemovePoffinsWith_Level_LessThan(100),
        RemovePoffinsWith_SecondLevel_LessThan(40),
        RemovePoffinsWith_NumberOfFlavors_LessThan(1),
        RemovePoffinsWith_MaxNSimilar(1),
        SortPoffinsBy_LevelToSmoothnessRatioSum()
    ]
    poffin_filtering_sorting_system = PoffinSortAndFilterSystem(poffin_filters_sorters)
    poffin_factory = PoffinFactory(PoffinCooker(40), berry_combinations, poffin_filtering_sorting_system)
    poffin_permutations = poffin_factory.get_poffin_permutations_3()

    # Stats
    contest_stats_filters_sorters = [
        RemoveContestStatsWith_PoffinsEaten_GreaterThan(12),
        RemoveContestStatsWith_Rank_GreaterThan(2),
        SortContestStatsBy_Rank(),
        # SortOnContestStats_PoffinsEaten(),
        # SortOnContestStats_NumUniqueBerries(),
        # SortOnContestStats_Rarity(),
    ]
    contest_stats_filtering_sorting_system = ContestStatsSortAndFilterSystem(contest_stats_filters_sorters)
    contest_stat_factory = ContestStatsFactory(poffin_permutations, contest_stats_filtering_sorting_system)
    final_stats = contest_stat_factory.filtered_sorted_contest_stats

    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:
        if not final_stats:
            print("No results")
        else:
            print("Lets see the results!\n\n\n")
            for stat in final_stats:
                print(stat, file=print_file)
            print('\n'*10, file=print_file)
            print(str(final_stats[0]), file=print_file)
            print(str(final_stats[0]))
            print(repr(final_stats[0]))


if __name__ == "__main__":
    main()
