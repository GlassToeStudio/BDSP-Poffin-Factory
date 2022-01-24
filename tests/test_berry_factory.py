import make_poffins.berry.berry_factory as b
from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker

berry_factory = BerryFactory(None)


def test_berry_name():
    value = len(set(berry_factory.every_berry))
    assert len(berry_factory.every_berry) != value, f"Should be True"
