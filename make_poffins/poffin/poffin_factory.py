from itertools import permutations

from make_poffins.berry.berry import Berry
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker

from poffin.poffin_sort_and_filter_system import PoffinSortAndFilterSystem


def __poffin_permutations_n__(n: int, poffins: list[Poffin]) -> tuple[Poffin, ...]:  # noqa ES501
    """Every combination of n poffins"""
    return permutations(poffins, n)


def poffin_permutations_2(poffins: list[Poffin]) -> tuple[Poffin, Poffin]:
    """Every combination of 2 poffins"""
    return __poffin_permutations_n__(2, poffins)


def poffin_permutations_3(poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin]:  # noqa ES501
    """Every combination of 3 poffins"""
    return __poffin_permutations_n__(3, poffins)


def poffin_permutations_4(poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
    """Every combination of 4 poffins"""
    return __poffin_permutations_n__(4, poffins)


def poffin_permutations_5(poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
    """Every combination of 5 poffins"""
    return __poffin_permutations_n__(5, poffins)


def poffin_permutations_10(poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
    """Every combination of 10 poffins"""
    return __poffin_permutations_n__(10, poffins)


class PoffinFactory():
    def __init__(self, cooker: PoffinCooker, berry_combinations: tuple[Berry, ...]):  # noqa ES501
        self.__poffins__ = None
        self.__cooker__ = cooker
        self.__berry_combinations__ = berry_combinations

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
        for recipe in self.__berry_combinations__:
            p = self.__cooker__.cook(recipe)
            if p.name == "foul poffin":
                continue
            self.__poffins__.append(p)

    def generate_custom_poffin_list_from_recipes(self, recipes):  # noqa ES501
        return [self.__cooker__.cook(recipe) for recipe in recipes]  # noqa ES501

    # Sorters
    def get_poffins_with_n_flavors_greater_than_min_value_at_min_level(self, o_poffins: list[Poffin], num_flavors: int = 3, min_value: int = 30, min_level: int = 100) -> list[Poffin]:  # noqa ES501
        poffin_sorter = PoffinSortAndFilterSystem()
        poffins = poffin_sorter.filter_poffins_by_level(o_poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501
        poffins = poffin_sorter.filter_similar_poffins_to_four(poffins)
        poffins = poffin_sorter.filter_if_any_value_less_than(poffins, min_value)  # noqa ES501
        print(len(poffins))
        self.__poffins__ = poffins
        return poffins

    def get_poffins_by_flavor_with_n_flavors_greater_than_min_value_at_min_level(self, o_poffins: list[Poffin], flavor: str, num_flavors: int = 3, min_value: int = 30, min_level: int = 100) -> list[Poffin]:  # noqa ES501
        poffin_sorter = PoffinSortAndFilterSystem()
        poffins = poffin_sorter.filter_poffins_by_flavor(o_poffins, flavor)
        poffins = poffin_sorter.filter_poffins_by_level(poffins, min_level)
        poffins = poffin_sorter.filter_by_num_flavors(poffins, num_flavors)
        poffins = poffin_sorter.sort_on_sum_of_main_flavor_smoothness_ratios(poffins)  # noqa ES501

        poffins = poffin_sorter.filter_similar_poffins_to_four(poffins)
        poffins = poffin_sorter.filter_if_any_value_less_than(poffins, min_value)  # noqa ES501
        print(len(poffins))
        self.__poffins__ = poffins
        return poffins


if __name__ == "__main__":
    print("Starting up...")
    print("Done...")
