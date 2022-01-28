from make_poffins.berry import berry_library
from make_poffins.berry.berry_factory import BerryFactory


def test_berry_list(bf: BerryFactory):
    value = len(bf.berries)
    assert len(berry_library.tiny_list) == value, "Should be True"
    assert bf.berries[0].name == "petaya"


def test_berry_filtered_list(bf: BerryFactory):
    value = len(bf.filtered_berries)
    assert len(berry_library.tiny_list) == value, "Should be True"


def test_all_combinations_4(bf: BerryFactory):
    value = 1365
    assert len(list(bf.get_berry_combinations_4())) == value, "Should be True"


def test_all_combinations_3(bf: BerryFactory):
    value = 455
    assert len(list(bf.get_berry_combinations_3())) == value, "Should be True"


def test_all_combinations_2(bf: BerryFactory):
    value = 105
    assert len(list(bf.get_berry_combinations_2())) == value, "Should be True"
