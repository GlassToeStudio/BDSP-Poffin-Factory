import make_poffins.berry.berry_factory as b
from make_poffins.berry.berry_factory import single_recipe
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker

cooker = PoffinCooker()
test_poffin1 = cooker.cook(single_recipe)  # noqa ES501
test_poffin2 = cooker.cook(single_recipe)  # noqa ES501


def test_poffin_name():
    value = "super mild poffin"
    assert test_poffin1.name == value, f"Should be {value}"


def test_poffin_berry_flavor_values():
    value = [148, 0, 0, 28, 0]
    assert test_poffin1.flavor_values == value, f"Should be {value}"


def test_poffin_smoothness():
    value = 30
    assert test_poffin1.smoothness == value, f"Should be {value}"


def test_poffin_str():
    value = "148 super mild poffin   30 [148,   0,   0,  28,   0]"
    assert str(test_poffin1).__contains__(value), "Should be True"


def test_poffin_main_flavor():
    value = "Spicy"
    assert test_poffin1.main_flavor == value, f"Should be {value}"


def test_poffin_id():
    value = True
    assert test_poffin1.__id__ == test_poffin2.__id__, f"Should be {value}"


def test_poffin_eq():
    value = True
    assert test_poffin1 == test_poffin2, f"Should be {value}"


def test_poffin_hash():
    value = True
    assert len([test_poffin1, test_poffin2]) != len(set([test_poffin1, test_poffin2])), f"Should be {value}"  # noqa ES501


def print_poffin():
    print(repr(test_poffin1))
    print(str(test_poffin1))


if __name__ == "__main__":
    print_poffin()
