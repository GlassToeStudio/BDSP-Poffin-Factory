from make_poffins.berry import berry_library


def test_berry_name():
    value = len(set(berry_library.every_berry))
    assert len(berry_library.every_berry) != value, "Should be True"
