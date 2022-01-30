from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import (
    RemoveBerriesWith_Rarity_GreaterThan, RemoveBerriesWith_Rarity_LessThan,
    RemoveBerriesWith_Smoothness_LessThan)
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (
    SortBerriesBy_Main_Flavor, SortBerriesBy_Smoothness,
    SortBerriesBy_Weakened_Main_Flavor_Value)
from make_poffins.contest_stats.contest_stats_factory import \
    ContestStatsFactory
from make_poffins.contest_stats.contest_stats_filter_interface import (
    FilterContestStatsBy_Num_Perfect_values_LT,
    FilterContestStatsBy_Poffins_Eaten_GT,
    FilterContestStatsBy_Poffins_Eaten_LT, FilterContestStatsBy_Rank_GT,
    FilterContestStatsBy_Rank_LT, FilterContestStatsBy_Rarity_GT,
    FilterContestStatsBy_Rarity_LT)
from make_poffins.contest_stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.contest_stats.contest_stats_sort_interface import (
    SortOnContestStats_PoffinsEaten, SortOnContestStats_Rank,
    SortOnContestStats_Rarity)
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_filter_interface import (
    RemovePoffinsWith_AnyFlavorValueLessThan, RemovePoffinsWith_MaxNSimilar,
    RemovePoffinsWith_NumberOfFlavors_LessThan,
    RemovePoffinsWith_Rarity_GreaterThan, RemovePoffinsWith_Level_LessThan,
    RemovePoffinsWith_Flavor_NotEqual)
from make_poffins.poffin.poffin_library import poffin_library
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem
from make_poffins.poffin.poffin_sort_interface import (
    SortPoffinsBy_LevelToSmoothnessRatioSum, SortPoffinsBy_Name)

# noqa F401
berries = berry_library.every_berry
x = RemoveBerriesWith_Rarity_LessThan(8)
berries = x.execute(berries)
x = RemoveBerriesWith_Rarity_GreaterThan(9)
berries = x.execute(berries)


def test_rank_and_eaten_filter():
    poffin_combos = PoffinFactory.generate_poffin_combinations_r(poffin_library.poffin_list, 4)

    sorters = [
        SortOnContestStats_Rarity(),
        SortOnContestStats_PoffinsEaten(),
    ]
    sorting_system = ContestStatsSortAndFilterSystem(sorters)
    stat_factory = ContestStatsFactory(poffin_combos, sorting_system)
    final_stats = stat_factory.filtered_sorted_contest_stats

    #_ = [print(str(p)) for p in final_stats]

    assert 27405 == len(final_stats)


if __name__ == "__main__":
    test_rank_and_eaten_filter()
