import math
from functools import cache
from itertools import product

import make_poffins.berry_factory as bf
from make_poffins.berry import Berry
from make_poffins.berry_sorter import BerrySorter
from make_poffins.best_recipe import BestRecipe
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker

FLAVORS = ["Spicy", "Dry", "Sweet", "Bitter", "Sour"]


def get_best(bests: list[BestRecipe], flavor: str) -> BestRecipe:
    best_flavor = bests[flavor]
    best_flavor = sorted(best_flavor, key=lambda x: (-x.num_can_eat, -x.poffin.smoothness, sum(x.total_values), x.poffin.level), reverse=True)  # noqa ES501

    with open(f"_{flavor}_output1.txt", "w", encoding='utf-8') as f:
        print(best_flavor, file=f)

    returns = []
    if len(best_flavor) > 0:
        returns = best_flavor[0]
    return returns


@cache
def find_best_recipe(cook_time: float) -> set[BestRecipe]:
    best_recipes = set()
    # for f in FLAVORS:
    #     best_recipes[f] = []

    bs = BerrySorter(bf.every_berry)
    bs.sort_all(True)
    berries = bs.get_sorted_berries()

    for recipe in bf.berry_combinations_4(berries):
        poffin = cook_poffin(recipe, cook_time)

        # if poffin.level >= 100 and poffin.__num_flavors__() >= 3:
        # if (math.ceil(255 / poffin.smoothness) * poffin.level) < 255:  # noqa ES501
        #     continue

        this_recipe = BestRecipe(poffin)  # noqa ES501
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
        if current_stat.rank > 3:
            continue
        all_stats.append(current_stat)

    results = sorted(all_stats, key=lambda x: (-x.num_perfect_values, x.sheen, x.poffins_eaten))  # noqa ES501
    print("total results:", len(results))
    return results


def main():
    print("Finding best recipes")
    best_recipes = find_best_recipe(40)

    print("Have best recipes")
    # for _, r in best_recipes.items():
    #     print(str(r), "\n")
    # _ = input("Wait")

    # print(f"Filtering {sum(len(x) for _, x in best_recipes.items())} recipes")  # noqa ES501
    # filtered_recipes = []
    # for _, recipes in best_recipes.items():
    #     temp_filter_holder = []
    #     for recipe in recipes:
    #         if recipe.poffin.smoothness < 30 or recipe.poffin.smoothness > 40:  # or recipe.poffin.smoothness > 40:  # noqa ES501
    #             continue

    #         temp_filter_holder.append(recipe.poffin)

    #     filtered_recipes.append(temp_filter_holder)

    print(f"Filtered the recipes do to {len(best_recipes)}")
    # for item in filtered_recipes:
    #     print(str(item))
    # _ = input("Wait")
    print("Making the combinations of the recipes")
    combos = [(x.poffin) for x in best_recipes]
    combos = bf.berry_combinationss_2(combos)
    print("Eating and getting contest stats")
    results = get_best_by_eating(combos)

    print("Done eating, where is the data?!")
    answer = ""
    for recipe in results:
        answer += f"{recipe}\n"

    print("Saving to file and print to terminal")
    with open("__best_recipe_all.txt", "w", encoding='utf-8') as out_file:
        print(answer, file=out_file)
    print(repr(results[:10]))


if __name__ == "__main__":
    main()
