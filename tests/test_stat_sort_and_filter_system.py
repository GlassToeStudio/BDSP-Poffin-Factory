from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.interface_berry_filter import (
    FilterBerriesBy_Smoothness_LessThan, FilterBerriessBy_Rarity_GreaterThan,
    FilterBerriessBy_Rarity_LessThan)
from make_poffins.berry.interface_berry_sort import (
    SortOnBerry__Weakened_Main_Flavor_Value, SortOnBerry_Main_Flavor,
    SortOnBerry_Smoothness)
from make_poffins.poffin.interface_poffin_filter import (
    FilterPoffinsBy_AnyFlavorValueLessThan, FilterPoffinsBy_Flavor,
    FilterPoffinsBy_Level_LessThan, FilterPoffinsBy_MaxNSimilar,
    FilterPoffinsBy_NumberOfFlavors_LessThan,
    FilterPoffinsBy_Rarity_GreaterThan)
from make_poffins.poffin.interface_poffin_sort import (
    SortOnPoffins_Attrs, SortOnPoffins_LevelToSmoothnessRatioSum,
    SortOnPoffins_Name)
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_library import poffin_library
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem
from make_poffins.stats.contest_stats_factory import ContestStatsFactory
from make_poffins.stats.contest_stats_sort_and_filter_system import \
    ContestStatsSortAndFilterSystem
from make_poffins.stats.interface_contest_stats_filter import (
    FilterContestStatsBy_Num_Perfect_values_LT,
    FilterContestStatsBy_Poffins_Eaten_GT,
    FilterContestStatsBy_Poffins_Eaten_LT, FilterContestStatsBy_Rank_GT,
    FilterContestStatsBy_Rank_LT, FilterContestStatsBy_Rarity_GT,
    FilterContestStatsBy_Rarity_LT)
from make_poffins.stats.interface_contest_stats_sort import (
    SortOnContestStats_PoffinsEaten, SortOnContestStats_Rank,
    SortOnContestStats_Rarity)

# noqa F401
berries = berry_library.every_berry
x = FilterBerriessBy_Rarity_LessThan(8)
berries = x.execute(berries)
x = FilterBerriessBy_Rarity_GreaterThan(9)
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

    _ = [print(str(p)) for p in final_stats]

    assert 10 == len(final_stats)


def test_whats_going_on_in_main():
    # Berries
    no_berries_rarer_than = 15
    min_berry_smoothness = 20

    # Poffins
    min_level = 100
    min_flavors = 3
    max_similar = 4
    min_value = 20
    # Cooking
    cook_time = 38.5

    # Stats
    max_eaten = 5
    min_rank = 1
    # Internal rank mechanism
    stop_at_first_n_results = 2000

    # Berries
    berry_filters_sorters = [
        FilterBerriesBy_Smoothness_LessThan(min_berry_smoothness),
        SortOnBerry_Main_Flavor(),
        SortOnBerry_Smoothness(),
        SortOnBerry__Weakened_Main_Flavor_Value()
    ]
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system, berry_library.tiny_list)
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
    #_ = input("Wait")
    poffins = poffin_factory.poffins
    print("length of poffins:", len(poffins))
    #_ = input("Wait")
    filtered_poffins = poffin_factory.filtered_poffins
    print("length of filtered poffins:", len(filtered_poffins))
    # _ = input("Wait")
    poffin_permutations = poffin_factory.get_poffin_permutations_4()

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
    final_stats = contest_stat_factory.filtered_sorted_contest_stats


def test_get_attr_name():
    poffin_combos = PoffinFactory.generate_poffin_combinations_r(poffin_library.poffin_list, 4)

    sorters = [
        FilterContestStatsBy_Rarity_LT(201),
        FilterContestStatsBy_Rank_LT(2),
        FilterContestStatsBy_Rank_GT(2),
        FilterContestStatsBy_Num_Perfect_values_LT(2),
        SortOnContestStats_Rarity(),
        SortOnContestStats_PoffinsEaten()
    ]
    sorting_system = ContestStatsSortAndFilterSystem(sorters)
    stat_factory = ContestStatsFactory(poffin_combos, sorting_system)

    # stat_factory._get_attr_name_from_Ifilter()
    final_stats = stat_factory.filtered_sorted_contest_stats

    _ = [print(str(p)) for p in final_stats]

    assert 10 == len(final_stats)


if __name__ == "__main__":
    test_get_attr_name()
