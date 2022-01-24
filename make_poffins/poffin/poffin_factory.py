from itertools import permutations

from make_poffins.berry.berry import Berry
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_sort_and_filter_system import \
    PoffinSortAndFilterSystem


class PoffinFactory():
    def __init__(self, cooker: PoffinCooker, berry_combinations: tuple[Berry, ...], poffin_filter_system: PoffinSortAndFilterSystem = None):  # noqa ES501
        self.__cooker__ = cooker
        self.__berry_combinations__ = berry_combinations
        self.__poffin_filter_system__ = poffin_filter_system

        self.__poffins__ = None
        self.__filtered_poffin_list__ = None
        print("\nSetting Up PoffinFactory")

    @property
    def poffins(self) -> list[Poffin]:
        """List of all possible poffins from the given list of berries

        Note:
            Will not include foul poffins!
        Returns:
            list[Poffin]: Unsorted or Filtered Poffin List
        """
        print("Trying to Get the Poffin List", self.__poffins__)
        if self.__poffins__ is None:
            print("Poffin List is Empty")
            self.__poffins__ = self.__generate_poffin_list__()
        print(f"Returning {len(self.__poffins__)} Generated Poffins")
        return self.__poffins__

    @property
    def filtered_poffins(self) -> list[Poffin]:
        """List of poffins filtered and sorted to the passed in rules/

        Returns:
            list[Poffin]: Filtered and Sorted Poffin List
        """
        print("Trying to Get Filtered Poffins")
        if self.__filtered_poffin_list__ is None:
            print("Have to Generate Filtered Poffins")
            self.__filtered_poffin_list__ = self.__poffin_filter_system__.get_Sorted_and_filtered_poffins(self.poffins)
        print(f"Returning {len(self.__filtered_poffin_list__)} Filtered Poffins")
        return self.__filtered_poffin_list__

    def __generate_poffin_list__(self):  # noqa ES501
        print("Generating Poffins")
        self.__poffins__ = []
        for recipe in self.__berry_combinations__:
            p = self.__cooker__.cook(recipe)
            if p.name == "foul poffin":
                continue
            self.__poffins__.append(p)
        return self.__poffins__

    def __poffin_permutations_n__(self, n: int, poffins: list[Poffin] = None) -> tuple[Poffin, ...]:  # noqa ES501
        """Every combination of n poffins"""
        print(f"Calling Permutations N, there are {'0' if poffins is None  else len(poffins)} poffins")
        if poffins is None:
            print("There are no Poffins Here")
            poffins = self.filtered_poffins
        print(f"Permutating {len(poffins)} Filtered Poffins")
        return permutations(poffins, n)

    def poffin_permutations_2(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin]:
        """Every combination of 2 poffins"""
        print(f"Calling Permutations 2, there are {'0' if poffins is None  else len(poffins)} poffins")
        return self.__poffin_permutations_n__(2, poffins)

    def poffin_permutations_3(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 3 poffins"""
        print(f"Calling Permutations 3, there are {'0' if poffins is None  else len(poffins)} poffins")
        return self.__poffin_permutations_n__(3, poffins)

    def poffin_permutations_4(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 4 poffins"""
        print(f"Calling Permutations 4, there are {'0' if poffins is None  else len(poffins)} poffins")
        return self.__poffin_permutations_n__(4, poffins)

    def poffin_permutations_5(self, poffins: list[Poffin] = None) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 5 poffins"""
        print(f"Calling Permutations 5, there are {'0' if poffins is None  else len(poffins)} poffins")
        return self.__poffin_permutations_n__(5, poffins)

    def poffin_permutations_10(self, poffins: list[Poffin]) -> tuple[Poffin, Poffin, Poffin, Poffin, Poffin]:  # noqa ES501
        """Every combination of 10 poffins"""
        print(f"Calling Permutations 10, there are {'0' if poffins is None  else len(poffins)} poffins")
        return self.__poffin_permutations_n__(10, poffins=None)

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

    def generate_custom_poffin_list_from_recipes(self, recipes):  # noqa ES501
        return [self.__cooker__.cook(recipe) for recipe in recipes]  # noqa ES501


if __name__ == "__main__":
    print("Starting up...")
    print("Done...")
