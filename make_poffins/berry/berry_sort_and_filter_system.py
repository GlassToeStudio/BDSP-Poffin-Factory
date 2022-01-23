from make_poffins.berry.berry import Berry
from make_poffins.berry.interface_berry_filter import IBerryFilterInterface
from make_poffins.berry.interface_berry_sort import IBerrySortInterface

# pylint: disable=too-few-public-methods


class BerrySortAndFilterSystem:
    def __init__(self, _filters: list[IBerrySortInterface | IBerryFilterInterface]):
        self.__sort_filters__ = _filters

    def get_Sorted_and_filtered_berries(self, berries: list[Berry]) -> list[Berry]:
        for sort_filter in self.__sort_filters__:
            berries = sort_filter.execute(berries)
        return berries


if __name__ == "__main__":
    pass
