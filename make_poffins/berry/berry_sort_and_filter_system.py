from make_poffins.berry.berry import Berry
from make_poffins.berry.interface_berry_filter import IBerryFilterInterface
from make_poffins.berry.interface_berry_sort import IBerrySortInterface

# pylint: disable=too-few-public-methods


class BerrySortAndFilterSystem:
    """Takes a list of IBerrySortInterface and IBerryFilterInterface rules and
    applies them to a list of berries.
    """

    def __init__(self, filters: list[IBerrySortInterface | IBerryFilterInterface]):
        self._sort_filters = filters

    def get_Sorted_and_filtered_berries(self, berries: list[Berry]) -> list[Berry]:
        """Return filtered and sorted berries based on the passed in rules

        Args:
            berries (list[Berry]): unfiltered, unsorted berries

        Returns:
            list[Berry]: filtered, sorted berries
        """
        for sort_filter in self._sort_filters:
            berries = sort_filter.execute(berries)
        return berries


if __name__ == "__main__":
    pass
