import time
from functools import cache

from make_poffins.berry import berry_factory
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import poffin_factory
from make_poffins.poffin.interface_poffin_filter import (
    FilterPoffinsBy_AnyFlavorValueLessThan, FilterPoffinsBy_Level,
    FilterPoffinsBy_MaxNSimilar, FilterPoffinsBy_NumberOfFlavors)
from make_poffins.poffin.interface_poffin_sort import \
    SortOnPoffinLevelToSmoothnessRatioSum
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem


@cache
def get_best_by_eating(_poffin_combos: list[tuple[Poffin]], _top_x=10, _min_rank: int = 1, _max_eaten: int = 10, print_file=None) -> list[ContestStats]:
    all_stats = []

    for poffin_combo in _poffin_combos:
        current_stat = ContestStats()
        current_stat.feed_poffins(poffin_combo)
        if current_stat.rank > _min_rank or current_stat.poffins_eaten > _max_eaten:
            continue
        all_stats.append(current_stat)
        # results = sorted(all_stats, key=lambda x: (x.rarity, x.unique_berries, -x.poffins_eaten))

        print(str(current_stat), file=print_file)
        if len(all_stats) >= _top_x:
            break

    results = sorted(all_stats, key=lambda x: (x.rarity, x.unique_berries, -x.poffins_eaten))
    print(f"Total results: {len(results)}\nSending top {_top_x}!")
    return results[:_top_x]


def main():
    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:

        berry_combinations = berry_factory.berry_combinations_4(berry_factory.every_berry)
        poffin_permutations = poffin_factory.poffin_permutations_4

        min_level = 100
        min_flavors = 3
        max_similar = 4
        min_value = 30

        min_rank = 1
        max_eaten = 8
        cook_time = 40
        top_x = 30

        p_factory = PoffinFactory(PoffinCooker(cook_time), berry_combinations)

        sorters = [
            FilterPoffinsBy_Level(min_level),
            FilterPoffinsBy_NumberOfFlavors(min_flavors),
            SortOnPoffinLevelToSmoothnessRatioSum(),
            FilterPoffinsBy_MaxNSimilar(max_similar),
            FilterPoffinsBy_AnyFlavorValueLessThan(min_value)
        ]
        poffin_sorter = PoffinSortAndFilterSystem(sorters)
        poffins = poffin_sorter.get_Sorted_and_filtered_poffins(p_factory.poffin_list)

        print("Poffins len:", len(poffins))

        results = get_best_by_eating(poffin_permutations(poffins), top_x, min_rank, max_eaten, print_file)

        print("Done eating!")
        for r in results:
            print(r)
        print('\n'*10)
        print(str(results[0]))
        print(repr(results[0]))


if __name__ == "__main__":
    main()
