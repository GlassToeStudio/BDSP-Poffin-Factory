from timeit import default_timer as timer

from gts_colors.colors import (BOLD, ITALIC, N_BOLD, N_ITALIC, RESET, RGB_BLUE,
                               RGB_DARK_VIOLET, RGB_GREEN, RGB_ORANGE, RGB_RED,
                               RGB_VIOLET, RGB_YELLOW, color_256)

italic = ITALIC
n_bold = N_BOLD
n_italic = N_ITALIC

# Weakened by:
# Spicy |  Sour  |  Bitter | Sweet  | Dry\n
# Dry   |  Spicy |  Sour   | Bitter | Sweet
FLAVORS = ["Spicy", "Dry", "Sweet", "Bitter", "Sour"]
"""List of all 5 flavors in order of preference - Spicy, Dry, Sweet, Bitter, Sour"""  # noqa ES501
FLAVOR_COLORS = {"Spicy": color_256(208), "Dry": color_256(39), "Sweet": color_256(163), "Bitter": color_256(40), "Sour": color_256(226)}  # noqa ES501
"""Dictionary of ascii color codes for each of the 5 flavors: {"Flavor" : Color}"""  # noqa ES501
FLAVOR_PREFERENCE = {"Spicy": 5, "Dry": 4, "Sweet": 3, "Bitter": 2, "Sour": 1}
"""Lookup table to find a given flavor's (Spicy, Dry, Sweet, Bitter, Sour) preference"""  # noqa ES501
SMOOTHNESS_TABLE = {
    20: ["leppa", "oran", "persim", "lum", "sitrus", "razz", "bluk", "nanab", "wepear", "pinap", "pomeg", "kelpsy", "qualot", "hondew", "grepa"],  # noqa ES501
    25: ["cheri", "chesto", "pecha", "rawst", "aspear", "figy", "wiki", "mago", "aguav", "iapapa"],  # noqa ES501
    30: ["tamato", "cornn", "magost", "rabuta", "nomel", "occa", "passho", "wacan", "rindo", "yache", "chople", "kebia", "shuca", "coba", "payapa"],  # noqa ES501
    35: ["spelon", "pamtre", "watmel", "durin", "belue", "tanga", "charti", "kasib", "haban", "colbur", "babiri", "chilan", "roseli"],  # noqa ES501
    40: ["liechi", "ganlon", "salac", "petaya", "apicot"],
    50: ["lansat", "starf"],  # Exactly the same berry, just different name
    60: ["enigma", "micle", "custap", "jaboca", "rowap"],
}
"""Lookup table to find the inherent smoothness of a berry by giving its name"""  # noqa ES501

RARITY_TABLE = {
    20: 1,
    25: 3,
    30: 5,
    35: 7,
    40: 9,
    50: 11,
    60: 15,
    255: 255  # For those berries that do not exist.
}

outline = color_256(168)
"""A pinkish color for an outline"""
bad_red = color_256(196)
"""A red"""
super_mild_poffin = f'{f"{BOLD}{RGB_RED}SU{RGB_ORANGE}PER {RGB_YELLOW}MI{RGB_GREEN}LD {RGB_BLUE}PO{RGB_DARK_VIOLET}FF{RGB_VIOLET}IN{RESET}":<28}'  # noqa ES501
"""The word "Super Mild Poffin" but in rainbow colors"""
mild_poffin = f'{f"{BOLD}{color_256(11) }MILD POFFIN{RESET}":<28}'
"""The word "Mild Poffin" but in gold"""
rich_poffin = f'{f"{BOLD}{color_256(247)}RICH POFFIN{RESET}":<28}'
"""The word "Rich Poffin" but in light grey."""
overripe_poffin = f'{f"{BOLD}{color_256(242)}OVERRIPE POFFIN{RESET}":<28}'
"""The word Overripe Poffin but in dark grey"""
foul_poffin = f'{f"{BOLD}{color_256(237)}FOUL POFFIN{RESET}":<28}'
"""The word Foul Poffin but in black"""


def sort_flavors(flavors_list: list[str]) -> list[tuple[int, str]]:
    """Sort the list of flavors names by preference

    Ex:
        [(30, 'Spicy'), (30, 'Sweet'), (30, 'Sour'), (10, 'Dry'), (10, 'Bitter')]  # noqa ES501
    """

    return sorted(flavors_list, key=lambda x: (x[0], FLAVOR_PREFERENCE[x[1]]), reverse=True)  # noqa ES501


def subtract_weakening_flavors(values: list[int]) -> list[int]:
    return [values[i] - values[(i+1) % 5] for i in range(5)]  # noqa ES501


def calculate_time(func):
    def time_it(*args, **kwargs):
        begin = timer()
        r = func(*args, **kwargs)
        end = timer()
        print(f"\t{BOLD}{color_256(34)}Total time taken in : {color_256(179)}{func.__name__}, {color_256(151)}{(end - begin):.6f}{color_256(34)} seconds{RESET}")
        return r
    return time_it


TOTAL_POFFINS = [0]
"""Update this in poffin factory to keeo track of the total permutations of poffins"""


def stat_counter(stat_count: int, per_iteration: int = 10000):
    if stat_count % per_iteration == 0:
        print(f" * {BOLD}Checked {outline}{stat_count:>9}{RESET}{BOLD} stats so far out of {outline}{TOTAL_POFFINS[0]:.0f}{RESET}"
              f"\t{color_256(82)}{10*stat_count/TOTAL_POFFINS[0]:.2f}{RESET}%")
    return stat_count + 1
