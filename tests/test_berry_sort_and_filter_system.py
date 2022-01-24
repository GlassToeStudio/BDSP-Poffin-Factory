from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.interface_berry_sort import (
    SortOnBerry_Attrs, SortOnBerry_MainFlavorToSmoothnessRatio,
    SortOnBerry_Name)

berry_factory = BerryFactory(None)


def test_SortOnBerry_Name():
    berry_sorters = [
        SortOnBerry_Name()
    ]

    berry_sorter = BerrySortAndFilterSystem(berry_sorters)
    berries = berry_sorter.get_Sorted_and_filtered_berries(berry_factory.filtered_berries)
    assert berries[0].name == "aguav" and berries[-1].name == 'yache'


def test_SortOnBerry_Attrs():
    berry_sorters = [
        SortOnBerry_Attrs((('main_flavor', False), ('smoothness', False),  ('__weakened_main_flavor_value__', False)))
    ]

    berry_sorter = BerrySortAndFilterSystem(berry_sorters)
    berries = berry_sorter.get_Sorted_and_filtered_berries(berry_factory.filtered_berries)
    assert berries[0].name == "wepear" and berries[-1].rarity == 15


def test_just_sort_on_name_class():
    x = SortOnBerry_Name()
    berries = x.execute(berry_factory.filtered_berries)
    assert berries[0].name == "aguav" and berries[-1].name == 'yache'


def test_SortOnBerry_MainFlavorToSmoothnessRatio():
    x = SortOnBerry_MainFlavorToSmoothnessRatio()
    berries = x.execute(berry_factory.filtered_berries)
    assert berries[0].main_flavor_value/berries[0].smoothness >= berries[-1].main_flavor_value/berries[-1].smoothness
