import random

from make_poffins.berry import berry_library
from make_poffins.constants import FLAVORS
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_library import (bitter_poffins, dry_poffins,
                                                sour_poffins, spicy_poffins,
                                                sweet_poffins)

# Bitter
petaya_enigma_micle_custap_poffin = Poffin([28, 0, 13, 43, 0], 42, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.micle_berry, berry_library.custap_berry])
petaya_enigma_custap_ganlon_poffin = Poffin([40, 0, 0, 85, 0], 37, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.custap_berry, berry_library.ganlon_berry])

# Dry
petaya_enigma_apicot_micle_poffin = Poffin([0, 100, 0, 0, 0], 37, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.apicot_berry, berry_library.micle_berry])
petaya_enigma_apicot_ganlon_poffin = Poffin([12, 87, 0, 27, 0], 32, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.apicot_berry, berry_library.ganlon_berry])

# Sour
petaya_apicot_custap_salac_poffin = Poffin([12, 0, 27, 0, 42], 32, [berry_library.petaya_berry, berry_library.apicot_berry, berry_library.custap_berry, berry_library.salac_berry])
petaya_apicot_custap_colbur_poffin = Poffin([10, 0, 0, 0, 25], 30, [berry_library.petaya_berry, berry_library.apicot_berry, berry_library.custap_berry, berry_library.colbur_berry])

# Spicy
petaya_enigma_tanga_apicot_poffin = Poffin([85, 55, 0, 0, 0], 30, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.tanga_berry, berry_library.apicot_berry])
petaya_enigma_tanga_charti_poffin = Poffin([102, 42, 0, 12, 0], 29, [berry_library.petaya_berry, berry_library.enigma_berry, berry_library.tanga_berry, berry_library.charti_berry])

# Sweet
petaya_micle_liechi_custap_poffin = Poffin([12, 0, 57, 42, 0], 37, [berry_library.petaya_berry, berry_library.micle_berry, berry_library.liechi_berry, berry_library.custap_berry])
petaya_micle_custap_lansat_poffin = Poffin([12, 0, 42, 12, 0], 39, [berry_library.petaya_berry, berry_library.micle_berry, berry_library.custap_berry, berry_library.lansat_berry])

poffin_list = [
    # Spicy
    petaya_enigma_tanga_apicot_poffin,
    petaya_enigma_tanga_charti_poffin,
    # Dry
    petaya_enigma_apicot_micle_poffin,
    petaya_enigma_apicot_ganlon_poffin,
    # Sweet
    petaya_micle_liechi_custap_poffin,
    petaya_micle_custap_lansat_poffin,
    # Bitter
    petaya_enigma_micle_custap_poffin,
    petaya_enigma_custap_ganlon_poffin,
    # Sour
    petaya_apicot_custap_salac_poffin,
    petaya_apicot_custap_colbur_poffin,
    # Spicy
    petaya_enigma_tanga_apicot_poffin,
    petaya_enigma_tanga_charti_poffin,
    # Dry
    petaya_enigma_apicot_micle_poffin,
    petaya_enigma_apicot_ganlon_poffin,
    # Sweet
    petaya_micle_liechi_custap_poffin,
    petaya_micle_custap_lansat_poffin,
    # Bitter
    petaya_enigma_micle_custap_poffin,
    petaya_enigma_custap_ganlon_poffin,
    # Sour
    petaya_apicot_custap_salac_poffin,
    petaya_apicot_custap_colbur_poffin,
    # Spicy
    petaya_enigma_tanga_apicot_poffin,
    petaya_enigma_tanga_charti_poffin,
    # Dry
    petaya_enigma_apicot_micle_poffin,
    petaya_enigma_apicot_ganlon_poffin,
    # Sweet
    petaya_micle_liechi_custap_poffin,
    petaya_micle_custap_lansat_poffin,
    # Bitter
    petaya_enigma_micle_custap_poffin,
    petaya_enigma_custap_ganlon_poffin,
    # Sour
    petaya_apicot_custap_salac_poffin,
    petaya_apicot_custap_colbur_poffin
]

spicy_poffin_list = spicy_poffins.spicy_poffins_list
dry_poffin_list = dry_poffins.dry_poffins_list
sweet_poffin_list = sweet_poffins.sweet_poffins_list
bitter_poffin_list = bitter_poffins.bitter_poffins_list
sour_poffin_list = sour_poffins.sour_poffins_list

poffin_list_dict = {
    'spicy': spicy_poffin_list,
    'dry': dry_poffin_list,
    'sweet': sweet_poffin_list,
    'bitter': bitter_poffin_list,
    'sour': sour_poffin_list
}
FLAVORS


def get_random_poffin(flavor):
    l = poffin_list_dict[flavor.lower()]
    n = len(l)
    r = random.randrange(len(l))
    return l[r]


def generate_random_poffin_list_n_of_each(n: int, flavors: list[str]) -> list[Poffin]:
    """Return a list of n poffins of each given flavor.

    Args:
        n (int): Number of each poffin flavor
        flavors (list[str]): List of flavors

    Returns:
        list[Poffin]: List of poffins with n of each flavor
    """
    return_list = []
    for _ in range(n):
        for f in flavors:
            return_list.append(get_random_poffin(f))
    return return_list


def generate_random_poffin_list_n_total_of_random(n: int) -> list[Poffin]:
    """Retrun a list of size n containing random flavored poffins.

    Args:
        n (int): size of return list

    Returns:
        list[Poffin]: list of random poffins of size n
    """
    return_list = []
    for _ in range(n):
        f = random.randrange(len(FLAVORS))
        return_list.append(get_random_poffin(f))
    return return_list
