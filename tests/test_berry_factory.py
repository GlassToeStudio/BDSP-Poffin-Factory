import make_poffins.berry.berry_factory as b
from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_factory import every_berry
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker


def test_berry_name():
    value = len(set(b.every_berry))
    assert len(b.every_berry) != value, f"Should be True"
