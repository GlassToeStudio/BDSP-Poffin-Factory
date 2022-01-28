import math
from itertools import combinations

from make_poffins.berry import berry_library
from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.constants import TOTAL_BERRIES, calculate_time


class BerryFactory:
    """Factory to create combinations of differnt berries.

            - Sort berries
            - Filter berries
            - combinate? berries

    Attrs:
        * berries
        * filtered_berries

    Functions:
            get_berry_cmbionations_2
            get_berry_cmbionations_3
            get_berry_cmbionations_4

    """

    def __init__(self, berry_filter_system: BerrySortAndFilterSystem = None, berries: list[Berry] = None):
        """Factory to create combinations of differnt berries.

                - Sort berries
                - Filter berries
                - combinate? berries

        Attrs:
            * berries
            * filtered_berries

        Functions:
                get_berry_cmbionations_2
                get_berry_cmbionations_3
                get_berry_cmbionations_4
        Args:
            berry_filter_system (BerrySortAndFilterSystem, optional): To sort and filter berries. Defaults to None.
            berries (list[Berry], optional): The list of berries. Defaults to None - but will be berry_library.every_berry if None supplied/
        """

        self._berries = berries
        self._filtered_berries = None
        self._berry_filter_system = berry_filter_system
        self._every_berry = berry_library.every_berry
        print("\nSetting Up BerryFactory...")

    @property
    def berries(self):
        """Most likely using all 65 berries unless class initialized with its own list.

        Returns:\n
            1. The list of berries supplied upon inintalization, if any.\n
            2. The list of every berry from the berry library\n
            3. The list of berries if they where somehow set through a field you shouldnt touch.\n
        """

        if self._berries is None:
            self._berries = self._every_berry  # NOTE: Using an outside reference here! :D
            print(f"Returning {len(self._berries)}, Every Berry!")
        else:
            print(f"Returning {len(self._berries)} berries.")
        return self._berries

    @property
    def filtered_berries(self):
        """The list of berries filtered according to the rules found in the berry sort and filter system.\n

        Notes:\n
            - When first called, the list of berries is sorted an filterd. Once sorted and filtered the list is cached and returned as needed.\n

            - If there is no berry sort and filter system, the list of every berry from the berry library is returned, unsorted.\n

        Returns:
            [type]: List of berries, possibly sorted.
        """
        print("Trying to Get Filtered Berries.")

        if self._berry_filter_system is None:
            print(f"Returning {len(self._every_berry)}, Every Berry!")  # NOTE: Using an outside reference here! :D
            return self._every_berry  # NOTE: Using an outside reference here! :D

        if self._filtered_berries is None:
            self._filtered_berries = self._berry_filter_system.get_filtered_and_sorted_berries(self.berries)

        print(f"Returning {len(self._filtered_berries)} Filtered Berries")
        return self._filtered_berries

    @calculate_time
    def _get_berry_combinatiions_n(self, n: int, berries: list[Berry] = None) -> tuple[Berry, ...]:  # noqa ES501
        """Every combination of n berries

        Args:
            berries (list[Berry], optional): Defaults to self.filtered_berries\n
            which in turn defaults to berry_library.every_berry

        Returns:
            tuple[Berry, ...]: Every combination of n berries
        """

        global TOTAL_BERRIES

        if berries is None:
            berries = self.filtered_berries
        print(f"Combinating {len(berries)} Filtered Berries")

        c = math.factorial(len(berries)) / (math.factorial(n) * math.factorial(len(berries) - n))
        TOTAL_BERRIES[0] = c
        print(f"There are {c} combinations! Wow")
        return combinations(berries, n)

    def get_berry_combinations_2(self, berries: list[Berry] = None) -> tuple[Berry, Berry]:
        """Every combination of 2 berries

        Args:
            berries (list[Berry], optional): Defaults to self.filtered_berries\n
            which in turn defaults to berry_library.every_berry

        Returns:
            tuple[Berry, Berry]: Every combination of 2 berries
        """
        return self._get_berry_combinatiions_n(2, berries)

    def get_berry_combinations_3(self, berries: list[Berry] = None) -> tuple[Berry, Berry, Berry]:  # noqa ES501
        """Every combination of 3 berries

        Args:
            berries (list[Berry], optional): Defaults to self.filtered_berries\n
            which in turn defaults to berry_library.every_berry

        Returns:
            tuple[Berry, Berry, Berry]: Every combination of 3 berries
        """
        return self._get_berry_combinatiions_n(3, berries)

    def get_berry_combinations_4(self, berries: list[Berry] = None) -> tuple[Berry, Berry, Berry, Berry]:  # noqa ES501
        """Every combination of 4 berries

        Args:
            berries (list[Berry], optional): Defaults to self.filtered_berries\n
            which in turn defaults to berry_library.every_berry

        Returns:
            tuple[Berry, Berry, Berry, Berry]: Every combination of 4 berries
        """
        return self._get_berry_combinatiions_n(4, berries)


if __name__ == "__main__":
    print("BerryFactory")
