import pytest
from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import (
    RemoveBerriesWith_AnyFlavorValue_LessThan,
    RemoveBerriesWith_Rarity_GreaterThan, RemoveBerriesWith_Rarity_LessThan,
    RemoveBerriesWith_Smoothness_LessThan)
from make_poffins.berry.berry_sort_and_filter_system import \
    BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import (
    IBerrySorter, SortBerriesBy_Main_Flavor,
    SortBerriesBy_Main_Flavor_To_Smoothness_Ratio, SortBerriesBy_Name,
    SortBerriesBy_Rarity, SortBerriesBy_Smoothness,
    SortBerriesBy_Weakened_Main_Flavor)


def test_IBerrySortInterface_instantiation():
    with pytest.raises(TypeError):
        _ = IBerrySorter()


def test_IBerrySortInterface_inheritance():
    _ = SortBerriesBy_Name()
    assert isinstance(_, IBerrySorter)


def test_SortOnBerry_Name_members():
    x = SortBerriesBy_Name()
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
    x = SortBerriesBy_Name()
    with pytest.raises(TypeError):
        y = x.execute()
    y = x.execute(berry_library.every_berry)
    assert y[0].name == "aguav"
    assert y[-1].name == 'yache'
