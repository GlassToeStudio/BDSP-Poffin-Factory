import math
import multiprocessing as mp
import threading as mt
from itertools import combinations, permutations, starmap

from make_poffins.berry.berry import Berry
from make_poffins.constants import (TOTAL_BERRIES, TOTAL_POFFINS,
                                    calculate_time, start_up)
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem


class PoffinFactory():
    def __init__(self, cooker: PoffinCooker, berry_combinations: tuple[Berry, ...] = None, poffin_filter_system: PoffinSortAndFilterSystem = None):  # noqa ES501
        self._cooker = cooker
        self._berry_combinations = berry_combinations
        self._poffin_filter_system = poffin_filter_system
        self._poffins = []
        self._filtered_poffin_list = []
        self.num_berries = int(TOTAL_BERRIES[0])
        print("\nSetting Up PoffinFactory")

    @property
    def poffins(self) -> list[Poffin]:
        """List of all possible poffins from the given list of berries

        Note:
            Will not include foul poffins!

        Returns:
            list[Poffin]: Unsorted or Filtered Poffin List
        """
        if not self._poffins:
            # self._poffins = self._generate_poffin_list_serial()
            self._poffins = self._generate_poffin_list_map()
        print(f"Returning {None if not self._poffins else len(self._poffins)} Cooked Poffins")
        return self._poffins

    @property
    def filtered_poffins(self) -> list[Poffin]:
        """List of poffins filtered and sorted to the passed in rules/

        Returns:
            list[Poffin]: Filtered and Sorted Poffin List
        """
        if not self._filtered_poffin_list:
            self._filtered_poffin_list = self._poffin_filter_system.get_filtered_and_sorted_poffins(self.poffins)
        print(f"Returning {None if not self._filtered_poffin_list else len(self._filtered_poffin_list)} Filtered Poffins")
        return self._filtered_poffin_list

    @calculate_time
    def _generate_poffin_list_serial(self) -> list[Poffin]:  # noqa ES501
        print("Cooking Poffins")
        for recipe in self._berry_combinations:
            p = self._cooker.cook(recipe)
            if p.name == "foul poffin":
                continue
            self._poffins.append(p)
        return self._poffins

    @calculate_time
    def _generate_poffin_list_map(self) -> list[Poffin]:  # noqa ES501
        pool = mp.Pool()
        chunk_size = int(TOTAL_BERRIES[0]//mp.cpu_count())
        print(f"Cooking Poffins map")
        r = pool.map_async(self._mapped_cook, self._berry_combinations, chunksize=chunk_size)
        print()
        while not r.ready():
            print(f"{start_up(1)} * Complete: {100*((TOTAL_BERRIES[0] - (r._number_left*chunk_size)) / TOTAL_BERRIES[0]):6.2f}%")
            r.wait(timeout=1)
        self._poffins = [x for x in r.get() if x is not None]
        print(f"{start_up(1)} * Complete: {100*((TOTAL_BERRIES[0] - (r._number_left*chunk_size)) / TOTAL_BERRIES[0]):6.2f}%")
        return self._poffins

    def _mapped_cook(self, recipe):
        p = self._cooker.cook(recipe)
        if p.name != "foul poffin":
            return p

    @calculate_time
    def _get_poffin_permutations_n(self, n: int, poffins: list[Poffin] = None) -> tuple[Poffin, ...]:  # noqa ES501
        """Every combination of n poffins"""

        global TOTAL_POFFINS

        if poffins is None:
            poffins = self.filtered_poffins
        print(f"Permutating {len(poffins)} Filtered Poffins")

        c = math.factorial(len(poffins)) / (math.factorial(len(poffins)-n))
        TOTAL_POFFINS[0] = c
        print(f"There are {c} permutations! Wow")
        return permutations(poffins, n)

    def get_poffin_permutations_2(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin]:
        """Every combination of 2 poffins"""
        return self._get_poffin_permutations_n(2, poffins)

    def get_poffin_permutations_3(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 3 poffins"""
        return self._get_poffin_permutations_n(3, poffins)

    def get_poffin_permutations_4(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 4 poffins"""
        return self._get_poffin_permutations_n(4, poffins)

    def get_poffin_permutations_5(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 5 poffins"""
        return self._get_poffin_permutations_n(5, poffins)

    def get_poffin_permutations_10(self, poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 10 poffins"""
        return self._get_poffin_permutations_n(10, poffins=None)

    def generate_custom_poffin_list_from_recipes(self, recipes) -> list[Poffin]:  # noqa ES501
        self._poffins = [self._cooker.cook(recipe) for recipe in recipes] 
        return self.filtered_poffins

    @staticmethod
    def generate_poffin_combinations_r(poffins: list[Poffin], r: int = 5) -> list[Poffin]:
        Cn_r = math.factorial(len(poffins)) / (math.factorial(r) * math.factorial(len(poffins) - r))
        TOTAL_POFFINS[0] = Cn_r
        print(f"There are {Cn_r} combinations! Wow")
        return combinations(poffins, r)

    @staticmethod
    def generate_poffin_permutations_r(poffins: list[Poffin], r: int = 5) -> list[Poffin]:
        Pn_r = math.factorial(len(poffins)) / (math.factorial(len(poffins)-r))
        TOTAL_POFFINS[0] = Pn_r
        print(f"There are {Pn_r} permutations! Wow")
        return permutations(poffins, r)

    @staticmethod
    def get_python_style_poffin_declaration_string(poffin: Poffin) -> str:
        """test_poffin = Poffin([148, 0, 0, 28, 0], 30, [berry_factory.spelon_berry, berry_factory.liechi_berry, berry_factory.petaya_berry, berry_factory.enigma_berry])"""  # noqa ES501
        poffin_name = "".join([f"{poffin.berries[_].name}_" for _ in range(4)])[:-1]  # noqa ES501
        berry_names = "".join([f"berry_factory.{poffin.berries[_].name}_berry, " for _ in range(4)])[:-2]  # noqa ES501
        return f"{poffin_name}_poffin = Poffin({poffin.flavor_values}, {poffin.smoothness}, [{berry_names}])"  # noqa ES501

    @staticmethod
    def get_python_style_poffin_list_string(poffin: Poffin) -> str:
        """test_poffin = Poffin([148, 0, 0, 28, 0], 30, [berry_factory.spelon_berry, berry_factory.liechi_berry, berry_factory.petaya_berry, berry_factory.enigma_berry])"""  # noqa ES501
        poffin_name = "".join([f"{poffin.berries[_].name}_" for _ in range(4)])[:-1]  # noqa ES501
        return f"{poffin_name}_poffin,"


if __name__ == "__main__":
    print("Starting up...")
    print("Done...")
