from make_poffins.berry import berry_library
from make_poffins.poffin.poffin import Poffin

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
    petaya_apicot_custap_colbur_poffin
]
