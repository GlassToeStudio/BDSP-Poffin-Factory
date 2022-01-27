from make_poffins.poffin.interface_poffin_filter import IPoffinFilterInterface
from make_poffins.poffin.interface_poffin_sort import IPoffinSortInterface
from make_poffins.poffin.poffin import Poffin

# pylint: disable=too-few-public-methods


class PoffinSortAndFilterSystem:
    def __init__(self, _filters: list[IPoffinSortInterface | IPoffinFilterInterface]):
        self.__sort_filters__ = _filters

    def get_filtered_and_sorted_poffins(self, poffins: list[Poffin]) -> list[Poffin]:
        for sort_filter in self.__sort_filters__:
            if not poffins:
                return None
            poffins = sort_filter.execute(poffins)
        return poffins


if __name__ == "__main__":
    pass
