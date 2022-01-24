import math
from itertools import combinations

from make_poffins.berry import berry_factory, berry_library
from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem


class BerryFactory:
    def __init__(self, berry_filter_system: BerrySortAndFilterSystem = None, berries: list[Berry] = None):
        self._berry_filter_system = berry_filter_system
        self._berries = berries
        self._filtered_berries = None
        self._every_berry = berry_library.every_berry
        print("\nSetting Up BerryFactory...")

    @property
    def berries(self):
        print("Trying to Get the Berry List", self._berries)

        if self._berries is None:
            print("Berry List is Empty")

            self._berries = self._every_berry  # TODO: Using an outside reference here! :D
            print(f"Returning {len(self._berries)}, Every Berry!")
        else:
            print(f"Returning {len(self._berries)} berries.")
        return self._berries

    @property
    def filtered_berries(self):
        print("Trying to Get Filtered Berries.")

        if self._berry_filter_system is None:
            print("There is No Berry Filter System.")
            print(f"Returning {len(self._berries)}, Every Berry!")
            return self._every_berry

        if self._filtered_berries is None:
            print("Have to Generate Filtered Berries")

            self._filtered_berries = self._berry_filter_system.get_Sorted_and_filtered_berries(self.berries)
        print(f"Returning {len(self._filtered_berries)} Filtered Berries")

        return self._filtered_berries

    def _berry_combinatiions_n(self, n: int, berries: list[Berry] = None) -> tuple[Berry, ...]:  # noqa ES501
        """Every combination of n berries"""
        print(f"Calling Combinations N, there are {'0' if berries is None  else len(berries)} berries")

        if berries is None:
            print("There are no Berries Here")

            berries = self.filtered_berries
        print(f"Combinating {len(berries)} Filtered Berries")

        c = math.factorial(len(berries)) / (math.factorial(n) * math.factorial(len(berries) - n))
        print(f"There are {c} combinations! Wow")

        return combinations(berries, n)

    def berry_combinations_2(self, berries: list[Berry] = None) -> tuple[Berry, Berry]:
        """Every combination of 2 berries

            List of all 65 berries used if no berry list is passed in.
        """
        print(f"Calling Combinations 2, there are {'0' if berries is None  else len(berries)} berries")
        return self._berry_combinatiions_n(2, berries)

    def berry_combinations_3(self, berries: list[Berry] = None) -> tuple[Berry, Berry, Berry]:  # noqa ES501
        """Every combination of 3 berries

            List of all 65 berries used if no berry list is passed in.
        """
        print(f"Calling Combinations 3, there are {'0' if berries is None  else len(berries)} berries")
        return self._berry_combinatiions_n(3, berries)

    def berry_combinations_4(self, berries: list[Berry] = None) -> tuple[Berry, Berry, Berry, Berry]:  # noqa ES501
        """Every combination of 4 berries

            List of all 65 berries used if no berry list is passed in.
        """
        print(f"Calling Combinations 4, there are {'0' if berries is None  else len(berries)} berries")
        return self._berry_combinatiions_n(4, berries)


if __name__ == "__main__":
    for x in dir(berry_factory):
        print(x)
