
from copy import deepcopy

from make_poffins import berry_factory
from make_poffins.berry import Berry
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker
from make_poffins.poffin_sorter import PoffinSorter


class PoffinFactory():
    def __init__(self, cooker: PoffinCooker, berryfactory: berry_factory):
        self.__poffins__ = None
        self.__cooker__ = cooker
        self.__berry_factory__ = berryfactory

    @property
    def poffin_list(self):
        """List of all possible poffins from the given list of berries

            Note:
                Will not include foul poffins!
        """
        if self.__poffins__ is None:
            self.__generate_poffin_list__()
        return self.__poffins__

    @classmethod
    def get_python_style_poffin_declaration_string(cls, poffin: Poffin) -> str:
        """test_poffin = Poffin([148, 0, 0, 28, 0], 30, [berry_factory.spelon_berry, berry_factory.liechi_berry, berry_factory.petaya_berry, berry_factory.enigma_berry])"""  # noqa ES501
        poffin_name = "".join([f"{poffin.berries[_].name}_" for _ in range(4)])[:-1]  # noqa ES501
        berry_names = "".join([f"berry_factory.{poffin.berries[_].name}_berry, " for _ in range(4)])[:-2]  # noqa ES501
        return f"{poffin_name}_poffin = Poffin({poffin.flavor_values}, {poffin.smoothness}, [{berry_names}])"  # noqa ES501

    @classmethod
    def get_python_style_poffin_list_string(cls, poffin: Poffin) -> str:
        """test_poffin = Poffin([148, 0, 0, 28, 0], 30, [berry_factory.spelon_berry, berry_factory.liechi_berry, berry_factory.petaya_berry, berry_factory.enigma_berry])"""  # noqa ES501
        poffin_name = "".join([f"{poffin.berries[_].name}_" for _ in range(4)])[:-1]  # noqa ES501
        return f"{poffin_name}_poffin,"

    def __generate_poffin_list__(self):  # noqa ES501
        self.__poffins__ = []
        berries = self.__berry_factory__.every_berry
        for recipe in self.__berry_factory__.berry_combinations_4(berries):
            p = self.__cooker__.cook(recipe)
            if p.name == "foul poffin":
                continue
            self.__poffins__.append(p)

    def generate_custom_poffin_list_from_recipes(self, recipes):  # noqa ES501
        return [self.__cooker__.cook(recipe) for recipe in recipes]  # noqa ES501

    def get_poffins_with_n_flavors_greater_than_min_value_at_min_level(self, o_poffins: list[Poffin], num_flavors: int = 3, min_value: int = 30, min_level: int = 100) -> list[Poffin]:  # noqa ES501
        poffin_sorter = PoffinSorter()
        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, "spicy")
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        spicy_poffins_list = poffins.copy()

        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, "dry")
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        dry_poffins_list = poffins.copy()

        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, "sweet")
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        sweet_poffins_list = poffins.copy()

        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, "bitter")
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        bitter_poffins_list = poffins.copy()

        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, "sour")
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        sour_poffins_list = poffins.copy()

        poffins = [*spicy_poffins_list, *dry_poffins_list, *sweet_poffins_list, *bitter_poffins_list, *sour_poffins_list]  # noqa ES501

        poffins = poffin_sorter.filter_similar_poffins_to_four(poffins)

        poffins = poffin_sorter.filter_if_any_value_less_than(poffins, min_value)
        print(len(poffins))
        return poffins

    def get_poffins_by_flavor_with_n_flavors_greater_than_min_value_at_min_level(self, o_poffins: list[Poffin], flavor: str, num_flavors: int = 3, min_value: int = 30, min_level: int = 100) -> list[Poffin]:  # noqa ES501
        poffin_sorter = PoffinSorter()
        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, flavor)
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501

        poffins = poffin_sorter.filter_similar_poffins_to_four(poffins)
        poffins = poffin_sorter.filter_if_any_value_less_than(poffins, min_value)
        print(len(poffins))
        return poffins


def test_generate_poffin_string():
    cooker = PoffinCooker()
    pf = PoffinFactory(cooker, berry_factory)
    recipes = [[pf.__berry_factory__.every_berry[0], pf.__berry_factory__.every_berry[1], pf.__berry_factory__.every_berry[2], pf.__berry_factory__.every_berry[3]]]  # noqa ES501
    poffins = [pf.__cooker__.cook(recipe) for recipe in recipes]
    _ = [print(pf.get_python_style_poffin_declaration_string(poffin)) for poffin in poffins]


def different_poffin_files():
    spicy_file = open("make_poffins/poffin_data/spicy_poffins.py", 'w+', encoding='utf-8')  # noqa ES501
    dry_file = open("make_poffins/poffin_data/dry_poffins.py", 'w+', encoding='utf-8')  # noqa ES501
    sweet_file = open("make_poffins/poffin_data/sweet_poffins.py", 'w+', encoding='utf-8')  # noqa ES501
    bitter_file = open("make_poffins/poffin_data/bitter_poffins.py", 'w+', encoding='utf-8')  # noqa ES501
    sour_file = open("make_poffins/poffin_data/sour_poffins.py", 'w+', encoding='utf-8')  # noqa ES501

    temp_dict = {"Spicy": spicy_file, "Dry": dry_file, "Sweet": sweet_file, "Bitter": bitter_file, "Sour": sour_file}  # noqa ES501

    cooker = PoffinCooker()
    pe = PoffinFactory(cooker, berry_factory)
    berr_list = pe.__berry_factory__.tiny_list
    for recipe in pe.__berry_factory__.berry_combinations_4(berr_list):
        p = pe.__cooker__.cook(recipe)  # noqa ES501
        print(pe.get_python_style_poffin_declaration_string(p), file=temp_dict[p.main_flavor])  # noqa ES501

    for recipe in pe.__berry_factory__.berry_combinations_4(berr_list):
        p = pe.__cooker__.cook(recipe)
        print(pe.get_python_style_poffin_list_string(p), file=temp_dict[p.main_flavor])  # noqa ES501

    spicy_file.close()
    dry_file.close()
    sweet_file.close()
    bitter_file.close()
    sour_file.close()
    print("Done making poffin list")


GLOBAL_SEEN = set()
GLOBAL_REMAINING_POFFINS = []


def __shift_values__(poffin: Poffin):
    u = poffin.flavor_values.copy()
    v = u.copy()
    v.append(v.pop(0))
    x = v.copy()
    x.append(x.pop(0))
    y = x.copy()
    y.append(y.pop(0))
    z = y.copy()
    z.append(z.pop(0))
    u = tuple(u)
    v = tuple(v)
    x = tuple(x)
    y = tuple(y)
    z = tuple(z)

    if u not in GLOBAL_SEEN and v not in GLOBAL_SEEN and x not in GLOBAL_SEEN and y not in GLOBAL_SEEN and z not in GLOBAL_SEEN:  # noqa ES501
        GLOBAL_REMAINING_POFFINS.append(poffin)
    GLOBAL_SEEN.add(u)
    GLOBAL_SEEN.add(v)
    GLOBAL_SEEN.add(x)
    GLOBAL_SEEN.add(y)
    GLOBAL_SEEN.add(z)


def test_shift():
    every_poffin = set()
    temp_dict = {"Spicy": set(), "Dry": set(), "Sweet": set(), "Bitter": set(), "Sour": set()}  # noqa ES501
    cooker = PoffinCooker()
    pf = PoffinFactory(cooker, berry_factory)
    berry_list = pf.__berry_factory__.every_berry
    for i, recipe in enumerate(pf.__berry_factory__.berry_combinations_4(berry_list)):
        p = pf.__cooker__.cook(recipe)  # noqa ES501
        every_poffin.add(p)
        temp_dict[p.main_flavor].add(p)
        __shift_values__(p)
    print(len(GLOBAL_REMAINING_POFFINS), len(every_poffin), i)


def test_make_poffins_dict_and_list_and_show_lengths():
    temp_dict = {"Spicy": set(), "Dry": set(), "Sweet": set(), "Bitter": set(), "Sour": set()}
    every_poffin = []
    cooker = PoffinCooker()
    pf = PoffinFactory(cooker, berry_factory)
    berry_list = pf.__berry_factory__.nano_list
    for recipe in pf.__berry_factory__.berry_combinations_4(berry_list):
        p = pf.__cooker__.cook(recipe)  # noqa ES501
        every_poffin.append(p)
        temp_dict[p.main_flavor].add(p)

    for _, p in temp_dict.items():
        print(len(p))
    print(len(every_poffin))


def generate_poffins_files():
    _ = input("WARNING - THIS IS LONG AND WILL OVERWRITE YOUR FILES!\nKEYBOARD INTERUPT NOW OR ELSE")
    with open("make_poffins/poffin_factory.py", 'a+', encoding='utf-8') as poffin_factory_file:  # noqa ES501
        cooker = PoffinCooker()
        pf = PoffinFactory(cooker, berry_factory)
        berr_list = pf.__berry_factory__.every_berry
        for _, recipe in enumerate(pf.__berry_factory__.berry_combinations_4(berr_list)):
            print(pf.get_python_style_poffin_declaration_string(pf.__cooker__.cook(recipe)), file=poffin_factory_file)  # noqa ES501
            count = _
        print(f"Done making poffins: {count}")

        print("all_poffins = [", file=poffin_factory_file)
        for recipe in pf.__berry_factory__.berry_combinations_4(berr_list):
            print(pf.get_python_style_poffin_list_string(pf.__cooker__.cook(recipe)), file=poffin_factory_file)  # noqa ES501
        print("]", file=poffin_factory_file)
        print("Done making poffin list")


if __name__ == "__main__":
    print("Starting up...")
    print()
    test_generate_poffin_string()
    print("Done...")
