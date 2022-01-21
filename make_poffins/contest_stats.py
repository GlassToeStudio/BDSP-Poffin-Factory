import make_poffins.berry_factory as b
from make_poffins.constants import BOLD, FLAVOR_COLORS, RESET, bad_red, outline
from make_poffins.poffin import Poffin
from make_poffins.poffin_cooker import PoffinCooker


class ContestStats:
    def __init__(self):
        self.poffins = None
        self.coolness = 0
        """Coolness -> Spicy"""
        self.beauty = 0
        """Beauty -> Dry"""
        self.cuteness = 0
        """Cuteness -> Sweet"""
        self.cleverness = 0
        """Cleverness -> Bitter"""
        self.toughness = 0
        """Tougnness -> Sour"""
        self.sheen = 0
        """Total sheen"""
        self.poffins_eaten = 0
        """Total poffins eaten"""
        self.rank = -1
        """The ranking for the given poffin combo"""
        self.__all_values = None
        """Convenient list of all contest values"""

    def feed_poffins(self, poffins: list[Poffin]):
        self.poffins = poffins
        # print(poffins)
        while True:
            for p in poffins:
                self.feed(p)
                if self.sheen >= 255 or self.__rank_combo__() == 2:
                    self.rank = self.__rank_combo__()
                    return

    def feed(self, p: Poffin) -> None:
        if self.sheen >= 255:
            return

        self.poffins_eaten += 1
        self.sheen = self.__add_value__(self.sheen, p.smoothness)
        self.coolness = self.__add_value__(self.coolness, p.flavor_values[0])
        self.beauty = self.__add_value__(self.beauty, p.flavor_values[1])
        self.cuteness = self.__add_value__(self.cuteness, p.flavor_values[2])
        self.cleverness = self.__add_value__(self.cleverness, p.flavor_values[3])  # noqa ES501
        self.toughness = self.__add_value__(self.toughness, p.flavor_values[4])
        self.__all_values = [self.coolness, self.beauty, self.cuteness, self.cleverness, self.toughness]  # noqa ES501

    @staticmethod
    def __add_value__(current_value, additional_value):
        if current_value + additional_value >= 255:
            return 255
        return current_value + additional_value

    def __rank_combo__(self) -> int:
        """Return a rank of this 4-poffin combo.

        1 - everything is maxed
        2 - all categories maxed but still have some sheen
        3 - did not might criteria for 1 or 2, this is no good

        Returns:
            int: ranking
        """

        contest_values = sum(1 for x in self.__all_values if x >= 255)
        sheen_value = 10 if self.sheen >= 255 else 0
        total = contest_values + sheen_value
        if total == 15:
            return 1
        if total == 5:
            return 2
        return 3

    def __repr__(self) -> str:
        amt = 36
        formated_poffin_string = '\n'.join(map(repr, self.poffins))
        return (
            f"{formated_poffin_string}\n"
            f"{BOLD}{outline}{'-'* amt}{RESET}\n"
            f"{BOLD}{outline}| ******   Contest Stats    ****** |{RESET}\n"
            f"{BOLD}{outline}{'-'* amt}{RESET}\n"
            f"{BOLD}{outline}| {FLAVOR_COLORS['Spicy' ]}{'(Spicy)'  :<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Spicy' ]}{'Coolness'  :<14}{RESET}:{bad_red if self.coolness   < 255 else FLAVOR_COLORS['Bitter']}{self.coolness  :>4} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}| {FLAVOR_COLORS['Dry'   ]}{'(Dry)'    :<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Dry'   ]}{'Beauty'    :<14}{RESET}:{bad_red if self.beauty     < 255 else FLAVOR_COLORS['Bitter']}{self.beauty    :>4} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}| {FLAVOR_COLORS['Sweet' ]}{'(Sweet)'  :<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Sweet' ]}{'Cuteness'  :<14}{RESET}:{bad_red if self.cuteness   < 255 else FLAVOR_COLORS['Bitter']}{self.cuteness  :>4} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}| {FLAVOR_COLORS['Bitter']}{'(Bitter)' :<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Bitter']}{'Cleverness':<14}{RESET}:{bad_red if self.cleverness < 255 else FLAVOR_COLORS['Bitter']}{self.cleverness:>4} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}| {FLAVOR_COLORS['Sour'  ]}{'(Sour)'   :<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Sour'  ]}{'Toughness' :<14}{RESET}:{bad_red if self.toughness  < 255 else FLAVOR_COLORS['Bitter']}{self.toughness :>4} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}{'-'* amt}{RESET}\n"
            f"{BOLD}{outline}| {RESET}{BOLD}Eaten{RESET}{self.poffins_eaten:>6}  {BOLD}{'Sheen':<14}{RESET}:{BOLD if self.sheen >= 255 else RESET}{self.sheen:>4}{RESET} {BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}{'-'* amt}{RESET}\n"
            f"{BOLD}{outline}| {RESET}{BOLD}Rank{RESET} :{FLAVOR_COLORS['Bitter'] if self.rank == 1 else FLAVOR_COLORS['Spicy'] if self.rank == 2 else bad_red} {self.rank}{RESET:<29}{BOLD}{outline}|{RESET}\n"  # noqa ES501
            f"{BOLD}{outline}{'-'* amt}{RESET}\n")

    def __str__(self) -> str:
        formated_poffin_string = '\n'.join(map(str, self.poffins))
        return (f"Rank: {self.rank} Poffins eaten: {self.poffins_eaten}\n"
                f"\t{self.coolness}, {self.beauty}, {self.cuteness}, {self.cleverness}, {self.toughness} : {self.sheen}\n"  # noqa ES501
                f"\n{formated_poffin_string}\n")


def main():
    """
    Level: 148 - Super Mild Poffin   Smoothness: 30
        [148, 0, 0, 28, 0]
        Main Flavor: Spicy
        All Flavors: Spicy - Bitter
        Second strongest flavor value: 28
    """
    def cook_poffin(recipe, t):
        cooker = PoffinCooker()
        cooker.cook(recipe, t, 0, 0)
        poffin = cooker.complete()
        return poffin

    recipes = [
        [b.spelon_berry, b.petaya_berry, b.enigma_berry, b.jaboca_berry],
        [b.pamtre_berry, b.apicot_berry, b.micle_berry, b.rowap_berry],
        [b.salac_berry, b.lansat_berry, b.custap_berry, b.rowap_berry],
        [b.durin_berry, b.ganlon_berry, b.micle_berry, b.jaboca_berry],
        [b.belue_berry, b.salac_berry, b.lansat_berry, b.rowap_berry]
    ]
    poffins = []
    for recipe in recipes:
        poffins.append(cook_poffin(recipe, 40))

    stats = ContestStats()
    stats.feed_poffins(frozenset(poffins))
    print(stats)
    print(repr(stats))


if __name__ == "__main__":
    main()
