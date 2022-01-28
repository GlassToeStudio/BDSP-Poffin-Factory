import pytest
from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import (
    FilterBerriesBy_AnyFlavorValue_LessThan,
    FilterBerriesBy_Smoothness_LessThan, FilterBerriessBy_Rarity_GreaterThan,
    FilterBerriessBy_Rarity_LessThan)
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (
    IBerrySorter, SortOnBerry__Weakened_Main_Flavor, SortOnBerry_Main_Flavor,
    SortOnBerry_Main_Flavor_To_Smoothness_Ratio, SortOnBerry_Name,
    SortOnBerry_Rarity, SortOnBerry_Smoothness)


def test_IBerrySortInterface_instantiation():
    with pytest.raises(TypeError):
        _ = IBerrySorter()


def test_IBerrySortInterface_inheritance():
    _ = SortOnBerry_Name()
    assert isinstance(_, IBerrySorter)


def test_SortOnBerry_Name_members():
    x = SortOnBerry_Name()
    assert hasattr(x, '_value')
    assert x._value is None
    assert hasattr(x, '_reverse')
    assert x._reverse is False
    assert hasattr(x, 'value')
    assert x.value == 'name'
    assert hasattr(x, 'reverse')
    assert x.reverse is False
    assert hasattr(x, 'execute')
    assert callable(getattr(x, 'execute'))


def test_SortOnBerry_Name_execute():
    x = SortOnBerry_Name()
    with pytest.raises(TypeError):
        y = x.execute()
    y = x.execute(berry_library.every_berry)
    assert y[0].name == "aguav"
    assert y[-1].name == 'yache'
