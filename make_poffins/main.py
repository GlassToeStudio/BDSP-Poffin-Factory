from functools import cache
from itertools import product

import make_poffins.berry_factory as b
from make_poffins.berry import Berry
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
def find_best_recipe(cook_time: float) -> BestRecipe:
    best_recipes = {}
    for f in FLAVORS:
        best_recipes[f] = []

    for recipe in b.berry_combinations_4():
        poffin = cook_poffin(recipe, cook_time)

        if poffin.level >= 100:
            this_recipe = BestRecipe(poffin.main_flavor, poffin.level, poffin, recipe)  # noqa ES501
            best_recipes[poffin.main_flavor].append(this_recipe)

    return best_recipes


@cache
def cook_poffin(recipe: list[Berry], cook_time: float) -> Poffin:
    cooker = PoffinCooker()
    cooker.cook(recipe, cook_time, 0, 0)
    poffin = cooker.complete()
    return poffin


@cache
def get_best_by_eating(poffin_combos: list[Poffin]) -> list[ContestStats]:
    all_stats = []
    for poffin_combo in poffin_combos:
        if len(poffin_combo) != len(set(poffin_combo)):
            continue
        current_stat = ContestStats()
        current_stat.feed_poffins(poffin_combo)
        all_stats.append(current_stat)

    results = sorted(all_stats, key=lambda x: (x.rank, x.poffins_eaten))
    return results[:10]


def main():
    print("Finding best recipes")
    best_recipes = find_best_recipe(40)
    print("Have best recipes")
    filtered_recipes = []
    for _, recipes in best_recipes.items():
        seen = []
        filtering = []
        for recipe in recipes:
            if recipe.poffin.flavor_values in seen or recipe.poffin.smoothness > 40:  # noqa ES501
                continue

            seen.append(recipe.poffin.flavor_values)
            filtering.append(recipe.poffin)

        filtered_recipes.append(filtering)

    print("Filtered the recipes")
    for item in filtered_recipes:
        print(len(item))

    print("Making the combinations of the recipes")
    combos = frozenset(product(*filtered_recipes))
    print("Eating and getting contest stats")
    results = get_best_by_eating(combos)

    print("Done eating, where is the data?!")
    answer = ""
    for recipe in results:
        answer += f"{recipe}\n"

    print("Saving to file and print to terminal")
    with open("_best_recipe_all.txt", "w", encoding='utf-8') as out_file:
        print(answer, file=out_file)
    print(repr(results[0]))


if __name__ == "__main__":
    main()
