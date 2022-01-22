from itertools import combinations

from make_poffins import berry_factory
from make_poffins.berry import Berry

petaya_berry = Berry("Petaya", [30, 0, 0, 30, 10])
"""Spicy (25)  -- [10, 0, 0, 0, 0]"""
enigma_berry = Berry("Enigma", [40, 10, 0, 0, 0])
"""Dry (25)  -- [0, 10, 0, 0, 0]"""
tanga_berry = Berry("Tanga", [20, 0, 0, 0, 10])
"""Sweet (25)  -- [0, 0, 10, 0, 0]"""
spelon_berry = Berry("Spelon", [30, 10, 0, 0, 0])
"""Bitter (25)  -- [0, 0, 0, 10, 0]"""
liechi_berry = Berry("Liechi", [30, 10, 30, 0, 0])
"""Sour (25)  -- [0, 0, 0, 0, 10]"""
lansat_berry = Berry("Lansat", [30, 10, 30, 10, 30])
"""Spicy (20)  -- [10, 0, 10, 10, 10] - same as starf"""
starf_berry = Berry("Starf", [30, 10, 30, 10, 30])
"""Spicy (20)  -- [10, 10, 0, 10, 10] - same as lansat"""
figy_berry = Berry("Figy", [15, 0, 0, 0, 0])
"""Spicy (20)  -- [10, 10, 10, 0, 10]"""
chople_berry = Berry("Chople", [15, 0, 0, 10, 0])
"""Spicy (20)  -- [10, 10, 10, 10, 0]"""
occa_berry = Berry("Occa", [15, 0, 10, 0, 0])
"""Dry (20)  -- [0, 10, 10, 10, 10]"""
babiri_berry = Berry("Babiri", [25, 10, 0, 0, 0])
"""Spicy (25)  -- [15, 0, 0, 0, 0]"""
cheri_berry = Berry("Cheri", [10, 0, 0, 0, 0])
"""Dry (25)  -- [0, 15, 0, 0, 0]"""
rindo_berry = Berry("Rindo", [10, 0, 0, 15, 0])
"""Sweet (25)  -- [0, 0, 15, 0, 0]"""
pinap_berry = Berry("Pinap", [10, 0, 0, 0, 10])
"""Bitter (25)  -- [0, 0, 0, 15, 0]"""
nomel_berry = Berry("Nomel", [10, 0, 0, 0, 20])
"""Sour (25)  -- [0, 0, 0, 0, 15]"""
belue_berry = Berry("Belue", [10, 0, 0, 0, 30])
"""Spicy (20)  -- [10, 10, 0, 0, 0]"""
rowap_berry = Berry("Rowap", [10, 0, 0, 0, 40])
"""Dry (20)  -- [0, 10, 10, 0, 0]"""
pomeg_berry = Berry("Pomeg", [10, 0, 10, 10, 0])
"""Sweet (20)  -- [0, 0, 10, 10, 0]"""
qualot_berry = Berry("Qualot", [10, 0, 10, 0, 10])
"""Bitter (20)  -- [0, 0, 0, 10, 10]"""
leppa_berry = Berry("Leppa", [10, 0, 10, 10, 10])
"""Spicy (20)  -- [10, 0, 0, 0, 10]"""
shuca_berry = Berry("Shuca", [10, 0, 15, 0, 0])
"""Spicy (20)  -- [10, 0, 10, 10, 0]"""
tamato_berry = Berry("Tamato", [20, 10, 0, 0, 0])
"""Dry (20)  -- [0, 10, 0, 10, 10]"""
rawst_berry = Berry("Rawst", [0, 0, 0, 10, 0])
"""Spicy (20)  -- [10, 0, 10, 0, 10]"""
aguav_berry = Berry("Aguav", [0, 0, 0, 15, 0])
"""Spicy (20)  -- [10, 10, 0, 10, 0]"""
aspear_berry = Berry("Aspear", [0, 0, 0, 0, 10])
"""Dry (20)  -- [0, 10, 10, 0, 10]"""
wepear_berry = Berry("Wepear", [0, 0, 0, 10, 10])
"""Spicy (30)  -- [20, 10, 0, 0, 0]"""
rabuta_berry = Berry("Rabuta", [0, 0, 0, 20, 10])
"""Dry (30)  -- [0, 20, 10, 0, 0]"""
durin_berry = Berry("Durin", [0, 0, 0, 30, 10])
"""Sweet (30)  -- [0, 0, 20, 10, 0]"""
jaboca_berry = Berry("Jaboca", [0, 0, 0, 40, 10])
"""Bitter (30)  -- [0, 0, 0, 20, 10]"""
iapapa_berry = Berry("Iapapa", [0, 0, 0, 0, 15])
"""Sour (30)  -- [10, 0, 0, 0, 20]"""
colbur_berry = Berry("Colbur", [0, 0, 0, 10, 20])
"""Spicy (35)  -- [30, 10, 0, 0, 0]"""
pecha_berry = Berry("Pecha", [0, 0, 10, 0, 0])
"""Dry (35)  -- [0, 30, 10, 0, 0]"""
nanab_berry = Berry("Nanab", [0, 0, 10, 10, 0])
"""Sweet (35)  -- [0, 0, 30, 10, 0]"""
haban_berry = Berry("Haban", [0, 0, 10, 20, 0])
"""Bitter (35)  -- [0, 0, 0, 30, 10]"""
payapa_berry = Berry("Payapa", [0, 0, 10, 0, 15])
"""Sour (35)  -- [10, 0, 0, 0, 30]"""
mago_berry = Berry("Mago", [0, 0, 15, 0, 0])
"""Spicy (30)  -- [15, 0, 10, 0, 0]"""
wacan_berry = Berry("Wacan", [0, 0, 15, 0, 10])
"""Dry (30)  -- [0, 15, 0, 10, 0]"""
magost_berry = Berry("Magost", [0, 0, 20, 10, 0])
"""Sweet (30)  -- [0, 0, 15, 0, 10]"""
roseli_berry = Berry("Roseli", [0, 0, 25, 10, 0])
"""Bitter (30)  -- [10, 0, 0, 15, 0]"""
watmel_berry = Berry("Watmel", [0, 0, 30, 10, 0])
"""Sour (30)  -- [0, 10, 0, 0, 15]"""
salac_berry = Berry("Salac", [0, 0, 30, 10, 30])
"""Spicy (30)  -- [15, 0, 0, 10, 0]"""
custap_berry = Berry("Custap", [0, 0, 40, 10, 0])
"""Dry (30)  -- [0, 15, 0, 0, 10]"""
razz_berry = Berry("Razz", [10, 10, 0, 0, 0])
"""Sweet (30)  -- [10, 0, 15, 0, 0]"""
hondew_berry = Berry("Hondew", [10, 10, 0, 10, 0])
"""Bitter (30)  -- [0, 10, 0, 15, 0]"""
oran_berry = Berry("Oran", [10, 10, 0, 10, 10])
"""Sour (30)  -- [0, 0, 10, 0, 15]"""
lum_berry = Berry("Lum", [10, 10, 10, 10, 0])
"""Spicy (35)  -- [20, 0, 0, 0, 10]"""
persim_berry = Berry("Persim", [10, 10, 10, 0, 10])
"""Dry (35)  -- [10, 20, 0, 0, 0]"""
chesto_berry = Berry("Chesto", [0, 10, 0, 0, 0])
"""Sweet (35)  -- [0, 10, 20, 0, 0]"""
coba_berry = Berry("Coba", [0, 10, 0, 15, 0])
"""Bitter (35)  -- [0, 0, 10, 20, 0]"""
kelpsy_berry = Berry("Kelpsy", [0, 10, 0, 10, 10])
"""Sour (35)  -- [0, 0, 0, 10, 20]"""
yache_berry = Berry("Yache", [0, 10, 0, 0, 15])
"""Spicy (35)  -- [25, 10, 0, 0, 0]"""
bluk_berry = Berry("Bluk", [0, 10, 10, 0, 0])
"""Dry (35)  -- [0, 25, 10, 0, 0]"""
grepa_berry = Berry("Grepa", [0, 10, 10, 0, 10])
"""Spicy (40)  -- [30, 10, 30, 0, 0]"""
sitrus_berry = Berry("Sitrus", [0, 10, 10, 10, 10])
"""Dry (40)  -- [0, 30, 10, 30, 0]"""
kasib_berry = Berry("Kasib", [0, 10, 20, 0, 0])
"""Sweet (40)  -- [0, 0, 30, 10, 30]"""
charti_berry = Berry("Charti", [10, 20, 0, 0, 0])
"""Spicy (40)  -- [30, 0, 0, 30, 10]"""
wiki_berry = Berry("Wiki", [0, 15, 0, 0, 0])
"""Dry (40)  -- [10, 30, 0, 0, 30]"""
passho_berry = Berry("Passho", [0, 15, 0, 10, 0])
"""Spicy (50)  -- [30, 10, 30, 10, 30]"""
kebia_berry = Berry("Kebia", [0, 15, 0, 0, 10])
"""Spicy (50)  -- [30, 10, 30, 10, 30]"""
cornn_berry = Berry("Cornn", [0, 20, 10, 0, 0])
"""Spicy (60)  -- [40, 10, 0, 0, 0]"""
apicot_berry = Berry("Apicot", [10, 30, 0, 0, 30])
"""Dry (60)  -- [0, 40, 10, 0, 0]"""
chilan_berry = Berry("Chilan", [0, 25, 10, 0, 0])
"""Sweet (60)  -- [0, 0, 40, 10, 0]"""
pamtre_berry = Berry("Pamtre", [0, 30, 10, 0, 0])
"""Bitter (60)  -- [0, 0, 0, 40, 10]"""
ganlon_berry = Berry("Ganlon", [0, 30, 10, 30, 0])
"""Sour (60)  -- [10, 0, 0, 0, 40]"""
micle_berry = Berry("Micle", [0, 40, 10, 0, 0])
"""Sweet (35)  -- [0, 0, 25, 10, 0]"""

every_berry = [
    cheri_berry,
    chesto_berry,
    pecha_berry,
    rawst_berry,
    aspear_berry,
    leppa_berry,
    oran_berry,
    persim_berry,
    lum_berry,
    sitrus_berry,
    figy_berry,
    wiki_berry,
    mago_berry,
    aguav_berry,
    iapapa_berry,
    razz_berry,
    bluk_berry,
    nanab_berry,
    wepear_berry,
    pinap_berry,
    pomeg_berry,
    kelpsy_berry,
    qualot_berry,
    hondew_berry,
    grepa_berry,
    tamato_berry,
    cornn_berry,
    magost_berry,
    rabuta_berry,
    nomel_berry,
    spelon_berry,
    pamtre_berry,
    watmel_berry,
    durin_berry,
    belue_berry,
    occa_berry,
    passho_berry,
    wacan_berry,
    rindo_berry,
    yache_berry,
    chople_berry,
    kebia_berry,
    shuca_berry,
    coba_berry,
    payapa_berry,
    tanga_berry,
    charti_berry,
    kasib_berry,
    haban_berry,
    colbur_berry,
    babiri_berry,
    chilan_berry,
    liechi_berry,
    ganlon_berry,
    salac_berry,
    petaya_berry,
    apicot_berry,
    lansat_berry,
    starf_berry,
    enigma_berry,
    micle_berry,
    custap_berry,
    jaboca_berry,
    rowap_berry,
    roseli_berry,
]
"""List of all 64 berries"""

tiny_list = [
    petaya_berry,
    enigma_berry,
    tanga_berry,
    apicot_berry,
    micle_berry,
    charti_berry,
    liechi_berry,
    custap_berry,
    lansat_berry,
    ganlon_berry,
    jaboca_berry,
    petaya_berry,
    salac_berry,
    rowap_berry,
    colbur_berry
]
"""Three of each, theoretically best, berries -  Spicy, Dry, Sweet, Bitter, Sour"""  # noqa ES501

nano_list = [
    petaya_berry,
    enigma_berry,
    apicot_berry,
    liechi_berry,
    custap_berry,
    ganlon_berry,
]
"""Only 6 berries! Om My!"""

single_recipe = [spelon_berry, liechi_berry, petaya_berry, enigma_berry]
"""Four berries to be used as a single test recipe\n

Poffin:

    148 super mild poffin   30 [148,   0,   0,  28,   0]\n
            spelon Spicy    35 [ 30,  10,   0,   0,   0]\n
            liechi Spicy    40 [ 30,  10,  30,   0,   0]\n
            petaya Spicy    40 [ 30,   0,   0,  30,  10]\n
            enigma Spicy    60 [ 40,  10,   0,   0,   0]\n
"""


def __berry_combinatiions_n__(n: int, berries: list[Berry] = None) -> tuple[Berry, ...]:  # noqa ES501
    """Every combination of n berries"""
    if berries is None:
        berries = every_berry
    return combinations(berries, n)


def berry_combinations_2(berries: list[Berry] = None) -> tuple[Berry, Berry]:
    """Every combination of 2 berries"""
    return __berry_combinatiions_n__(2, berries)


def berry_combinations_3(berries: list[Berry] = None) -> tuple[Berry, Berry, Berry]:  # noqa ES501
    """Every combination of 3 berries"""
    return __berry_combinatiions_n__(3, berries)


def berry_combinations_4(berries: list[Berry] = None) -> tuple[Berry, Berry, Berry, Berry]:  # noqa ES501
    """Every combination of 4 berries"""
    return __berry_combinatiions_n__(4, berries)


def berry_combinations_5(berries: list[Berry] = None) -> tuple[Berry, Berry, Berry, Berry]:  # noqa ES501
    """Every combination of 4 berries"""
    return __berry_combinatiions_n__(5, berries)


if __name__ == "__main__":
    for x in dir(berry_factory):
        print(x)
