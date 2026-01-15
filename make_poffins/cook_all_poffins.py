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
    SortPoffinsBy_Level, SortPoffinsBy_LevelToSmoothnessRatioSum,
    SortPoffinsBy_NumFlavors, SortPoffinsBy_SecondLevel,
    SortPoffinsBy_Smoothness)


@calculate_time
def main():
    # Berries
    berry_filters_sorters = [
        # RemoveBerriesWith_Rarity_LessThan(1),
        # RemoveBerriesWith_Rarity_GreaterThan(15),
        SortBerriesBy_Rarity(),
        SortBerriesBy_Name()
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system)
    berry_combinations = berry_factory.get_berry_combinations_4()

    # Poffins
    poffin_filters_sorters = [
        RemovePoffinsWith_Level_LessThan(85),
        # RemovePoffinsWith_SecondLevel_LessThan(30),
        RemovePoffinsWith_NumberOfFlavors_LessThan(1),
        RemovePoffinsWith_MaxNSimilar(1),
        SortPoffinsBy_NumFlavors(),
        SortPoffinsBy_Level(),
        SortPoffinsBy_SecondLevel()
    ]
    poffin_filtering_sorting_system = PoffinSortAndFilterSystem(poffin_filters_sorters)
    poffin_factory = PoffinFactory(PoffinCooker(40), berry_combinations, poffin_filtering_sorting_system)
    all_poffins = poffin_factory.generate_custom_poffin_list_from_recipes(berry_combinations)

    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:
        if not all_poffins:
            print("No results")
        else:
            print("Lets see the results!\n\n\n")
            for poffin in all_poffins:
                print(poffin, file=print_file)
            print('\n'*10, file=print_file)
            print(str(all_poffins[0]), file=print_file)
            print(str(all_poffins[0]))
            print(repr(all_poffins[0]))


if __name__ == "__main__":
    main()
