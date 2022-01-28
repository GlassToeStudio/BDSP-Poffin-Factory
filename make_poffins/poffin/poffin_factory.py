import math
import multiprocessing as mp
import queue
from itertools import combinations, permutations

from make_poffins.berry.berry import Berry
from make_poffins.constants import (TOTAL_BERRIES, TOTAL_POFFINS,
                                    calculate_time, chunks)
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
            self._poffins = self._generate_poffin_list_serial()
            # self._poffins = self._generate_poffin_list_parallel() TODO: Not using this, its slower.. for some reason and I think there is a bug.
        print(f"Returning {len(self._poffins)} Cooked Poffins")
        return self._poffins

    @property
    def filtered_poffins(self) -> list[Poffin]:
        """List of poffins filtered and sorted to the passed in rules/

        Returns:
            list[Poffin]: Filtered and Sorted Poffin List
        """
        if not self._filtered_poffin_list:
            self._filtered_poffin_list = self._poffin_filter_system.get_filtered_and_sorted_poffins(self.poffins)
        print(f"Returning {len(self._filtered_poffin_list)} Filtered Poffins")
        return self._filtered_poffin_list

    @calculate_time
    def _generate_poffin_list_serial(self) -> list[Poffin]:  # noqa ES501
        print("Cooking Poffins", self.num_berries, mp.cpu_count())
        for recipe in self._berry_combinations:
            p = self._cooker.cook(recipe)
            if p.name == "foul poffin":
                continue
            self._poffins.append(p)
        return self._poffins

    @calculate_time
    def _generate_poffin_list_parallel(self) -> list[Poffin]:  # noqa ES501
        processed_list = mp.Manager().list()
        processes = []
        chunk_size = int(self.num_berries//(mp.cpu_count()))
        for i, berry_chunk in enumerate(chunks(self._berry_combinations, chunk_size)):
            if i % chunk_size == 0:
                p = mp.Process(target=self._parallel_task, args=(berry_chunk, processed_list))
                processes.append(p)
                p.start()

        for p in processes:
            p.join()

        self._poffins = processed_list
        return self._poffins

    def _parallel_task(self, berry_chunks, shared_list):
        for recipe in berry_chunks:
            p = self._cooker.cook(recipe)
            if p.name == "foul poffin":
                continue
            shared_list.append(p)

    @calculate_time
    def _get_poffin_permutations_n(self, n: int, poffins: list[Poffin] = None) -> tuple[Poffin, ...]:  # noqa ES501
        """Every combination of n poffins"""

        global TOTAL_POFFINS

        if poffins is None:
            poffins = self.filtered_poffins
        print(f"Permutating {len(poffins)} Filtered Berries")

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
        return [self._cooker.cook(recipe) for recipe in recipes]  # noqa ES501

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
