from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import (
    RemoveBerriesWith_AnyFlavorValue_LessThan,
    RemoveBerriesWith_Rarity_GreaterThan, RemoveBerriesWith_Rarity_LessThan,
    RemoveBerriesWith_Smoothness_LessThan)
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (
    SortOnBerry__Weakened_Main_Flavor, SortOnBerry_Main_Flavor,
    SortOnBerry_Main_Flavor_To_Smoothness_Ratio, SortOnBerry_Name,
    SortOnBerry_Rarity, SortOnBerry_Smoothness)

berry_factory = BerryFactory(None)


def test_SortOnBerry_Name():
    berry_sorters = [
        SortOnBerry_Name()
    ]

    berry_sorter = BerrySortAndFilterSystem(berry_sorters)
    berries = berry_sorter.get_filtered_and_sorted_berries(berry_factory.filtered_berries)
    assert berries[0].name == "aguav"
    assert berries[-1].name == 'yache'


def test_SortOnBerry_Attrs():
    berry_sorters = [
        SortOnBerry_Main_Flavor(),
        SortOnBerry_Smoothness(),
        SortOnBerry__Weakened_Main_Flavor()
        # _SortOnBerry_Attrs((('main_flavor', False), ('smoothness', False),  ('_weakened_main_flavor_value', False)))
    ]

    berry_sorter = BerrySortAndFilterSystem(berry_sorters)
    berries = berry_sorter.get_filtered_and_sorted_berries(berry_factory.filtered_berries)
    assert berries[0].name == "wepear" and berries[-1].rarity == 15


def test_just_sort_on_name_class():
    x = SortOnBerry_Name()
    berries = x.execute(berry_factory.filtered_berries)
    assert berries[0].name == "aguav" and berries[-1].name == 'yache'


def test_SortOnBerry_MainFlavorToSmoothnessRatio():
    x = SortOnBerry_Main_Flavor_To_Smoothness_Ratio()
    berries = x.execute(berry_factory.filtered_berries)
    assert berries[0].main_flavor_value/berries[0].smoothness >= berries[-1].main_flavor_value/berries[-1].smoothness


def test_FilterBerriesBy_AnyFlavorValue_LessThan():
    berry_sorters = [
        RemoveBerriesWith_Rarity_LessThan(5),
        RemoveBerriesWith_Rarity_GreaterThan(9)
    ]
    berry_sorter = BerrySortAndFilterSystem(berry_sorters)
    berries = berry_sorter.get_filtered_and_sorted_berries(berry_library.every_berry)

    value = 33
    assert len(berries) == value, "Should be 30"


if __name__ == "__main__":
    berries = berry_library.every_berry
    x = RemoveBerriesWith_Rarity_LessThan(4)
    berries = x.execute(berries)
    berry_sorters = [
        SortOnBerry_Rarity(),
        SortOnBerry_Name(),
    ]
    for x in reversed(berry_sorters):
        berries = x.execute(berries)
    _ = [print(b) for b in berries]
    print()
