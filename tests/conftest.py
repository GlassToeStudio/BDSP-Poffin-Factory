import pytest
from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import \
    RemoveBerriesWith_Smoothness_LessThan
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (SortOnBerry_Main_Flavor,
                                                     SortOnBerry_Name,
                                                     SortOnBerry_Rarity)


@pytest.fixture(scope="session")
def bf():
    """Returns a berry factory with every berry sorted by main flavor, rarirty"""
    berry_filters_sorters = [
        SortOnBerry_Name(),
        SortOnBerry_Name()
        # SortOnBerry_Rarity()
    ]
    for _ in berry_library.tiny_list:
        print(str(_))
    berry_filtering_sorting_system = BerrySortAndFilterSystem(berry_filters_sorters)
    berry_factory = BerryFactory(berry_filtering_sorting_system, berry_library.tiny_list)
    # berry_combinations = berry_factory.get_berry_combinations_4()
    return berry_factory
