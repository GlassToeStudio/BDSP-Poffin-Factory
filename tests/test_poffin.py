import make_poffins.berry_factory as b
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker

cooker = PoffinCooker()
cooker.cook([b.spelon_berry, b.liechi_berry, b.petaya_berry, b.enigma_berry], 40, 0, 0)  # noqa ES501
test_poffin1 = cooker.complete()

cooker = PoffinCooker()
cooker.cook([b.spelon_berry, b.liechi_berry, b.petaya_berry, b.enigma_berry], 40, 0, 0)  # noqa ES501
test_poffin2 = cooker.complete()


def test_poffin_name():
    value = "super mild poffin"
    assert test_poffin1.name == value, f"Should be {value}"


def test_berry_flavor_values():
    value = [148, 0, 0, 28, 0]
    assert test_poffin1.flavor_values == value, f"Should be {value}"


def test_berry_smoothness():
    value = 30
    assert test_poffin1.smoothness == value, f"Should be {value}"


def test_berry_str():
    value = "148 super mild poffin  30 - Flavors [148, 0, 0, 28, 0]"
    assert str(test_poffin1).__contains__(value), "Should be True"


def test_berry_main_flavor():
    value = "Spicy"
    assert test_poffin1.main_flavor == value, f"Should be {value}"


def test_berry_id():
    value = True
    assert test_poffin1.__id__ == test_poffin2.__id__, f"Should be {value}"


def test_berry_eq():
    value = True
    assert test_poffin1 == test_poffin2, f"Should be {value}"


def test_berry_hash():
    value = True
    assert len([test_poffin1, test_poffin2]) != len(set([test_poffin1, test_poffin2])), f"Should be {value}"  # noqa ES501


def print_poffin():
    print(repr(test_poffin1))
    print(str(test_poffin1))


if __name__ == "__main__":
    print_poffin()
