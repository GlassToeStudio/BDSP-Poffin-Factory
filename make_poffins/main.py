import time
from functools import cache
from typing import Callable

import make_poffins.berry_factory as berry_factory
from make_poffins import poffin_factory
from make_poffins.berry import Berry
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker
from make_poffins.poffin_factory import PoffinFactory


@cache
def get_best_by_eating(_poffin_combos: list[tuple[Poffin]], _min_rank: int = 1, _max_eaten: int = 10) -> list[ContestStats]:
    all_stats = []
    for poffin_combo in _poffin_combos:
        current_stat = ContestStats()
        current_stat.feed_poffins(poffin_combo)
        if current_stat.rank > _min_rank or current_stat.poffins_eaten > _max_eaten:
            continue
        all_stats.append(current_stat)

    results = sorted(all_stats, key=lambda x: (-x.num_perfect_values, -x.sheen, x.poffins_eaten))
    num_to_send = 10
    print("Total results:", len(results), "\nSending top {num_to_send}!")
    return results[:num_to_send]


def main(_berry_combinations: tuple[Berry, ...], _poffin_permutations: Callable, _min_flavors: int = 3, _min_value: int = 30, _min_level: int = 100, _min_rank: int = 1, _max_eaten: int = 10):
    pf = PoffinFactory(PoffinCooker(), _berry_combinations)

    poffins = pf.get_poffins_with_n_flavors_greater_than_min_value_at_min_level(pf.poffin_list, _min_flavors, _min_value, _min_level)
    print("Poffins len:", len(poffins))

    results = get_best_by_eating(_poffin_permutations(poffins), _min_rank, _max_eaten)
    print("Done eating, where is the data?!")

    answer = "".join(f"{str(r)}\n" for r in results)

    print("Saving to file and print to terminal")
    timestamp = time.strftime("%d-%b-%Y %I-%M %p", time.localtime())
    with open(f"poffin_results_{timestamp}.txt", "w", encoding="utf-8") as out_file:
        print(answer, file=out_file)

    print(repr(results))


if __name__ == "__main__":
    berry_combinations = berry_factory.berry_combinations_4(berry_factory.every_berry)
    min_flavors = 3
    min_value = 30
    min_level = 100
    min_rank = 1
    max_eaten = 7
    poffin_permutations = poffin_factory.poffin_permutations_3
    main(berry_combinations, poffin_permutations, min_flavors, min_value, min_level, min_rank, max_eaten)
