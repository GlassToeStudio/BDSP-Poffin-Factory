from make_poffins.berry import berry_library
from make_poffins.poffin.poffin_cooker import PoffinCooker


def test_cooking():
    cooker = PoffinCooker(cook_time=40, spills=0, friends=6)
    p = cooker.cook(berry_library.single_recipe)
    print(p)


if __name__ == "__main__":
    test_cooking()
