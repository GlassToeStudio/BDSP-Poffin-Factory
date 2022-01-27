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
from make_poffins.poffin.interface_poffin_filter import (
    FilterPoffinsBy_AnyFlavorValueLessThan, FilterPoffinsBy_Level_LessThan,
    FilterPoffinsBy_MaxNSimilar, FilterPoffinsBy_NumberOfFlavors_LessThan)
from make_poffins.poffin.interface_poffin_sort import (
    SortOnPoffins_Attrs, SortOnPoffins_Level,
    SortOnPoffins_LevelToSmoothnessRatioSum)
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
from make_poffins.stats.interface_contest_stats_sort import \
    SortOnContestStats_Rarity


def main():
    # Poffins
    min_level = 100
    min_flavors = 3
    max_similar = 4
    min_value = 20
    # Cooking
    cook_time = 38.5

    # Stats
    max_eaten = 6
    min_rank = 1
    # Internal rank mechanism

    # Berries
    berry_filters_sorters = [
        SortOnBerry_Rarity(),
        SortOnBerry_Name()
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system)
    for _ in berry_factory.filtered_berries:
        print(_)

    _ = input("wait")
    berry_combinations = berry_factory.get_berry_combinations_4()

    # Poffins
    poffin_filters_sorters = [
        FilterPoffinsBy_Level_LessThan(min_level),
        FilterPoffinsBy_NumberOfFlavors_LessThan(min_flavors),
        SortOnPoffins_LevelToSmoothnessRatioSum(),
        FilterPoffinsBy_MaxNSimilar(max_similar),
        FilterPoffinsBy_AnyFlavorValueLessThan(min_value),
        SortOnPoffins_Attrs((("level", True), ("second_level", True), ("rarity", False)))
    ]
    poffin_filtering_sorting_system = PoffinSortAndFilterSystem(poffin_filters_sorters)
    poffin_factory = PoffinFactory(PoffinCooker(cook_time), berry_combinations, poffin_filtering_sorting_system)
    poffin_permutations = poffin_factory.get_poffin_permutations_3()

    # poffin_permutations = PoffinFactory.generate_poffin_combinations(poffin_library.poffin_list, 4)
    # Stats
    contest_stats_filters_sorters = [
        SortOnContestStats_Rarity(),
        # FilterContestStatsBy_Rank_GreaterThan(1),
        # FilterContestStatsBy_PoffinsEaten_GreaterThan(5)
        FilterContestStatsBy_Poffins_Eaten_GT(max_eaten),
        FilterContestStatsBy_Rank_GT(min_rank)
    ]
    contest_stats_filtering_sorting_system = ContestStatsSortAndFilterSystem(contest_stats_filters_sorters)
    contest_stat_factory = ContestStatsFactory(poffin_permutations, contest_stats_filtering_sorting_system)
    final_stats = contest_stat_factory.filtered_contest_stats

    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:
        if final_stats:
            print("Lets see the results!\n\n\n")
            print(str(final_stats[0]), file=print_file)
            for stat in final_stats:
                print(stat)
            print('\n'*10)
            print(str(final_stats[0]))
            print(repr(final_stats[0]))
        else:
            print("No results")


if __name__ == "__main__":
    main()
