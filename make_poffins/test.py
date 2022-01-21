from itertools import combinations, product

import make_poffins.berry_factory as b
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import Poffin
from make_poffins.poffin_maker import cook_poffin


def test_cook(recipe, t):
    n_poffin = cook_poffin(frozenset(recipe), t)
    return n_poffin


def test_equality(poffin1, poffin2):
    return poffin1 == poffin2


def test_set(poffin_list):
    print(len(poffin_list), len(set(poffin_list)))


def test_product():
    data = [
        ['A', 'B', 'C'],
        [1, 3],
        ['a', 'b', 'c'],
        [4, 5, 6],
        ['!', '@', '#', '$']
    ]

    product_data = [p for p in product(*data)]

    for p in product_data:
        print(p)


if __name__ == "__main__":
    # test_product()
    # test_poffin1 = test_cook([b.spelon_berry, b.liechi_berry, b.petaya_berry, b.enigma_berry], 40)
    # test_poffin2 = test_cook([b.spelon_berry, b.petaya_berry, b.enigma_berry, b.jaboca_berry], 40)
    # print(test_poffin1)
    # print(test_poffin2)
    # print(test_equality(test_poffin1, test_poffin2))
    # test_set([test_poffin1, test_poffin2])
    poffins = []
    recipe1 = [b.spelon_berry, b.petaya_berry, b.enigma_berry, b.jaboca_berry]
    recipe2 = [b.pamtre_berry, b.apicot_berry, b.micle_berry, b.rowap_berry]
    recipe3 = [b.salac_berry, b.lansat_berry, b.custap_berry, b.rowap_berry]
    recipe4 = [b.durin_berry, b.ganlon_berry, b.micle_berry, b.jaboca_berry]
    recipe5 = [b.belue_berry, b.salac_berry, b.lansat_berry, b.rowap_berry]
    recipes = [recipe1, recipe2, recipe3, recipe4, recipe5]
    for recipe in recipes:
        poffins.append(test_cook(recipe, 40))
    # print(poffins)
    stats = ContestStats()
    stats.feed_poffins(poffins)
    print(stats)

    # recipe = [b.rowap_berry, b.payapa_berry, b.kebia_berry, b.belue_berry]
    # test_cook(recipe, 40)
"""

Spicy: 117 * 3 (self.sheen=105, [351, 81, 0, 216, 0]) - 35 - 3
        - spelon         35
        - petaya         40
        - enigma         60
        - jaboca         60


Dry: 117 * 3 (self.sheen=105, [0, 351, 81, 0, 216]) - 35 - 3
        - pamtre         35
        - apicot         40
        - micle          60
        - rowap          60


Sweet: 102 * 3 (self.sheen=117, [126, 0, 306, 0, 261]) - 39 - 3
        - salac          40
        - lansat         50
        - custap         60
        - rowap          60


Bitter: 117 * 3 (self.sheen=105, [0, 216, 0, 351, 81]) - 35 - 3
        - durin          35
        - ganlon         40
        - micle          60
        - jaboca         60


Sour: 117 * 3 (self.sheen=99, [171, 0, 171, 0, 351]) - 33 - 3
        - belue          35
        - salac          40
        - lansat         50
        - rowap          60
"""
