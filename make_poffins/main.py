
from functools import cache

import make_poffins.berry_factory as berry_factory
from make_poffins.berry import Berry
from make_poffins.berry_sorter import BerrySorter
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker
from make_poffins.poffin_factory import PoffinFactory
from make_poffins.recipe_record import RecipeRecord

FLAVORS = ["Spicy", "Dry", "Sweet", "Bitter", "Sour"]


def get_best(bests: list[RecipeRecord], flavor: str) -> RecipeRecord:
    best_flavor = bests[flavor]
    best_flavor = sorted(best_flavor, key=lambda x: (-x.num_can_eat, -x.poffin.smoothness, sum(x.total_values), x.poffin.level), reverse=True)  # noqa ES501

    with open(f"_{flavor}_output1.txt", "w", encoding='utf-8') as f:
        print(best_flavor, file=f)

    returns = []
    if len(best_flavor) > 0:
        returns = best_flavor[0]
    return returns


@cache
def find_best_recipe(cook_time: float) -> set[RecipeRecord]:
    best_recipes = set()
    # for f in FLAVORS:
    #     best_recipes[f] = []

    bs = BerrySorter(berry_factory.every_berry)
    bs.sort_all(True)
    berries = bs.get_sorted_berries()

    for recipe in berry_factory.berry_combinations_4(berries):
        poffin = cook_poffin(recipe, cook_time)

        # if poffin.level >= 100 and poffin.__num_flavors__() >= 3:
        # if (math.ceil(255 / poffin.smoothness) * poffin.level) < 255:  # noqa ES501
        #     continue

        this_recipe = RecipeRecord(poffin)  # noqa ES501
        best_recipes.add(this_recipe)

    return best_recipes


@cache
def cook_poffin(recipe: frozenset[Berry], cook_time: float) -> Poffin:
    cooker = PoffinCooker()
    cooker.cook(recipe, cook_time, 0, 0)
    poffin = cooker.complete()
    return poffin


@cache
def get_best_by_eating(poffin_combos: list[tuple[Poffin]]) -> list[ContestStats]:  # noqa ES501
    all_stats = []
    for poffin_combo in poffin_combos:
        # if len(poffin_combo) != len(set(poffin_combo)):
        #     continue
        current_stat = ContestStats()
        current_stat.feed_poffins(poffin_combo)
        if current_stat.rank > 2 or current_stat.poffins_eaten > 10:
            continue
        all_stats.append(current_stat)

    results = sorted(all_stats, key=lambda x: (-x.num_perfect_values, -x.sheen, x.poffins_eaten))  # noqa ES501
    print("total results:", len(results))
    return results[:5]


def main():
    cooker = PoffinCooker()
    pf = PoffinFactory(cooker, berry_factory)
    poffins = pf.poffin_list
    poffins = pf.get_poffins_with_n_flavors_greater_than_min_value_at_min_level(poffins, 3, 30, 100)  # noqa ES501
    print("Poffins len:", len(poffins))
    combos = berry_factory.berry_combinations_3(poffins)
    results = get_best_by_eating(combos)

    print("Done eating, where is the data?!")
    answer = ""
    for r in results:
        answer += f"{str(r)}\n"

    print("Saving to file and print to terminal")
    with open("new_best_recipe_all.txt", "w", encoding='utf-8') as out_file:
        print(answer, file=out_file)

    print(repr(results))


if __name__ == "__main__":
    main()
