from make_poffins.berry import berry
from make_poffins.berry.berry_factory import (every_berry, lansat_berry,
                                              starf_berry)

ganlon_berry = berry.Berry("Ganlon", [0, 30, 10, 30, 0])
n_ganlon_berry = berry.Berry("Fake2", [0, 30, 10, 30, 0])


def test_berry_name():
    value = "ganlon"
    assert ganlon_berry.name == value, f"Should be {value}"


def test_berry_flavor_values():
    value = [0, 30, 10, 30, 0]
    assert ganlon_berry.flavor_values == value, f"Should be {value}"


def test_berry_smoothness():
    value = 40
    assert ganlon_berry.smoothness == value, f"Should be {value}"


def test_berry_str():
    value1 = "\tganlon Dry      40 [  0,  30,  10,  30,   0] [-30, 20, -20, 30, 0]"
    value2 = "\tganlon Dry      40 [  0,  30,  10,  30,   0]"
    assert str(ganlon_berry) == value1 or str(ganlon_berry) == value2, f"Should be {True}"  # noqa ES501


def test_berry_main_flavor():
    value = "Dry"
    assert ganlon_berry.main_flavor == value, f"Should be {value}"


def test_berry__get_smoothness__():
    value = 255
    assert n_ganlon_berry.smoothness == value, f"Should be {value}"


def test_berry_id():
    value = True
    assert ganlon_berry.__id__ == n_ganlon_berry.__id__, f"Should be {value}"


def test_berry_eq():
    value = True
    assert ganlon_berry == n_ganlon_berry, f"Should be {value}"


def test_berry_hash():
    value = True
    assert len([ganlon_berry, n_ganlon_berry]) != len(set([ganlon_berry, n_ganlon_berry])), f"Should be {value}"  # noqa ES501


def print_all_berries():
    _ = [(print('repr :', repr(b)), print('str  :', b))for b in every_berry]


def print_berry_names():
    _ = [print(b.name) for b in every_berry]


def pint_set_berry_names():
    _ = [print(b.name) for b in frozenset(every_berry)]


def what_is_like_starf():
    starf = starf_berry
    ans = [b.name for b in frozenset(every_berry) if b == starf]
    print(ans)


if __name__ == "__main__":
    print_all_berries()
    print()
    print_berry_names()
    print()
    pint_set_berry_names()
    print()
    what_is_like_starf()
    print(starf_berry, lansat_berry)
