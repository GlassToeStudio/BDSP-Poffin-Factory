import time
from functools import cache

from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_sort_and_filter_system import *
from make_poffins.berry.interface_berry_filter import *
from make_poffins.berry.interface_berry_sort import *
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin.interface_poffin_filter import *
from make_poffins.poffin.interface_poffin_sort import *
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_sort_and_filter_system import *


@cache
def eat_and_rank_poffins(_poffin_combos: list[tuple[Poffin]], _top_x=10, _min_rank: int = 1, _max_eaten: int = 10, print_file=None) -> list[ContestStats]:
    # TODO: This should have a home
    all_stats = []

    for poffin_combo in _poffin_combos:
        current_stat = ContestStats()
        current_stat.feed_poffins(poffin_combo)
        if current_stat.rank > _min_rank or current_stat.poffins_eaten > _max_eaten:
            continue
        all_stats.append(current_stat)
        # results = sorted(all_stats, key=lambda x: (x.rarity, x.unique_berries, -x.poffins_eaten))

        print(str(current_stat), file=print_file)
        if len(all_stats) >= (_top_x*20):
            break

    results = sorted(all_stats, key=lambda x: (x.unique_berries, x.rarity, x.poffins_eaten))
    if results:
        meh = '\n'*20
        print(f"{meh}{str(results[0])}", file=print_file)
        print(f"Total results: {len(results)}\nSending top {_top_x}!")
        return results[:_top_x]
    return None


def main():
    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"make_poffins/results/poffin_results_{timestamp}.txt", "w", encoding="utf-8") as print_file:

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
        berry_sorters = [
            FilterBerriessBy_RarityGreaterThan(no_berries_rarer_than),
            SortOnBerry_Attrs((('main_flavor', False), ('smoothness', False),  ('__weakened_main_flavor_value__', False))),
        ]
        berry_sorter = BerrySortAndFilterSystem(berry_sorters)
        berry_factory = BerryFactory(berry_sorter)
        berry_combinations = berry_factory.berry_combinations_4()

        # Poffins
        poffin_sorters = [
            FilterPoffinsBy_Level(min_level),
            FilterPoffinsBy_NumberOfFlavors(min_flavors),
            SortOnPoffins_LevelToSmoothnessRatioSum(),
            FilterPoffinsBy_MaxNSimilar(max_similar),
            FilterPoffinsBy_AnyFlavorValueLessThan(min_value)
        ]
        poffin_sorter = PoffinSortAndFilterSystem(poffin_sorters)
        poffin_factory = PoffinFactory(PoffinCooker(cook_time), berry_combinations, poffin_sorter)
        poffin_permutations = poffin_factory.poffin_permutations_4()

        results = eat_and_rank_poffins(poffin_permutations, top_x, min_rank, max_eaten, print_file)

        print("Lets see the results!\n\n\n")
        if len(results) > 0:
            for r in results:
                print(r)
            print('\n'*10)
            print(str(results[0]))
            print(repr(results[0]))


if __name__ == "__main__":
    main()
