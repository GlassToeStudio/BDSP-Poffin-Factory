from copy import deepcopy
from itertools import product

from make_poffins.berry.berry_sorter import BerrySorter
from make_poffins.contest_stats import ContestStats
from make_poffins.poffin import poffin
from make_poffins.poffin.poffin import Poffin, berry_factory
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from poffin.interface_poffin_filter import (FilterPoffinsBy_Level,
                                            FilterPoffinsBy_MaxNSimilar)
from poffin.interface_poffin_sort import (SortOnPoffins_MainFlavorValue,
                                          SortOnPoffins_Smoothness)
from poffin.poffin_sort_and_filter_system import PoffinSortAndFilterSystem


def test_cook(recipe, t):
    cooker = PoffinCooker()
    cooker.cook(frozenset(recipe), 40, 0, 0)
    return cooker.complete()


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


def test_sort():
    bs = BerrySorter(berry_factory.every_berry)
    bs.sort_all(True)
    bs.print_berries()
    bs = BerrySorter(berry_factory.every_berry)
    bs.sort_all(False)
    bs.print_berries()


def test_set_frozenset():
    x = set([1, 2, 3, 4, 5, 6, 6, 7])
    y = frozenset([1, 2, 3, 4, 5, 6, 6, 7])
    print(x, y)
    w = [(x, x, x, x) for x in berry_factory.every_berry]
    z = set([(x, x, x, x) for x in berry_factory.every_berry])
    print(w[0], str(list(z)[0]))


if __name__ == "__main__":
    p1 = Poffin([148, 0, 0, 28, 0], 30, berry_factory.single_recipe)
    p2 = Poffin([148, 0, 0, 28, 0], 33, berry_factory.single_recipe)
    p3 = Poffin([35, 0, 0, 28, 0], 20, berry_factory.single_recipe)
    p4 = Poffin([168, 0, 0, 28, 0], 40, [berry_factory.ganlon_berry, berry_factory.liechi_berry, berry_factory.micle_berry, berry_factory.tamato_berry])
    print(*p1.berries)
    print(*p4.berries)
    _poffins = [p1, p2, p3, p4]
    s = set([*p1.berries, *p2.berries, *p3.berries, *p4.berries])
    print(len(s))
    print(*s)
# sorting
sort_class1 = SortOnPoffins_Smoothness()
filter_class1 = FilterPoffinsBy_Level(148)
filter_class2 = FilterPoffinsBy_MaxNSimilar(1)
sort_class2 = SortOnPoffins_MainFlavorValue()

sort_filters = [sort_class1, filter_class1, filter_class2, sort_class2]
poffin_sorter_filterer = PoffinSortAndFilterSystem(sort_filters)
_poffins = poffin_sorter_filterer.get_Sorted_and_filtered_poffins(_poffins)
_ = [print(p) for p in _poffins]
print(sort_class1)


# test_product()
# test_poffin1 = test_cook([b.spelon_berry, b.liechi_berry, b.petaya_berry, b.enigma_berry], 40)
# test_poffin2 = test_cook([b.spelon_berry, b.petaya_berry, b.enigma_berry, b.jaboca_berry], 40)
# print(test_poffin1)
# print(test_poffin2)
# print(test_equality(test_poffin1, test_poffin2))
# test_set([test_poffin1, test_poffin2])
# poffins = []
# recipe1 = [bf.spelon_berry, bf.petaya_berry, bf.enigma_berry, bf.jaboca_berry]
# recipe2 = [bf.pamtre_berry, bf.apicot_berry, bf.micle_berry, bf.rowap_berry]
# recipe3 = [bf.salac_berry, bf.lansat_berry, bf.custap_berry, bf.rowap_berry]
# recipe4 = [bf.durin_berry, bf.ganlon_berry, bf.micle_berry, bf.jaboca_berry]
# recipe5 = [bf.belue_berry, bf.salac_berry, bf.lansat_berry, bf.rowap_berry]
# recipes = [recipe1, recipe2, recipe3, recipe4, recipe5]
# for recipe in recipes:
#     poffins.append(test_cook(recipe, 40))
# # print(poffins)
# stats = ContestStats()
# stats.feed_poffins(poffins)
# print(stats)

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
