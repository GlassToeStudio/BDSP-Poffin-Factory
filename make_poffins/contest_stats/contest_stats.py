
from make_poffins.berry import berry_library
from make_poffins.constants import BOLD, FLAVOR_COLORS, RESET, bad_red, outline
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory


class ContestStats:
    """Container to hold contest stats
        * Coolness -> Spicy
        * Beauty -> Dry
        * Cuteness -> Sweet
        * Cleverness -> Bitter
        * Tougnness -> Sour
        * Total sheen

    Has method to apply multiple poffins repeatedly.
    """
    __slots__ = [
        'poffins', 'coolness', 'beauty', 'cuteness', 'cleverness',
        'toughness', 'sheen', 'rank', 'rarity', 'poffins_eaten',
        'unique_berries', 'num_perfect_values', '_all_values', '_yield'
    ]

    def __init__(self, poffins: list[Poffin] = None):
        """Container to hold contest stats
            * Coolness -> Spicy
            * Beauty -> Dry
            * Cuteness -> Sweet
            * Cleverness -> Bitter
            * Tougnness -> Sour
            * Total sheen

        Has method to apply multiple poffins repeatedly.
        """
        self.poffins = None
        """The poffins used"""

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

        # Values by which we can sort and filter
        self.rank = 5
        """The ranking for the given poffin combo.

            Notes:\n
                    * 1 - Everything is maxed\n
                    * 2 - All categories maxed but still have some sheen\n
                    * 3 - Did not meet criteria for 1 or 2, this is not good\n
        """
        self.rarity = 0
        """The total rarity of all the berry rarities used in these poffins"""
        self.poffins_eaten = 0
        """Total poffins eaten"""
        self.unique_berries = 0
        """Number of different berriess used to make these poffins"""
        self.num_perfect_values = 0
        """The number of contest stats that are 255 - Not Sheen"""

        self._all_values = None
        """Convenient list of all 5 contest values - Not Sheen"""
        self._yield = 0
        """The total poffins created from these beries\n
            Used to determine if we will need to eat more poffins than are porudced from cooking once.
        """

        if poffins:
            self.apply_poffins(poffins)

    def apply_poffins(self, poffins: list[Poffin]):
        """Simulate feeding poffins one at a time and checking
        each of the 5 contest values and sheen. Keep feeiding
        until sheen is 255.

        Args:
            poffins (list[Poffin]): The poffins to 'eat'

        Notes:\n
            * These values are set once here:
                * self.poffins
                * self.rarity
                * self.unique_berries
        """

        # these are set once
        self.poffins = poffins
        self.rarity = sum(x.rarity for x in self.poffins)
        self.unique_berries = self._get_unique_berries(poffins)

        while True:
            for p in poffins:
                self._apply_poffin(p)
                # Sheen is maxed, cant eat anymore: Rank is 2 => All categories maxed.
                if self.sheen >= 255 or self.num_perfect_values == 5:
                    self.rank = self._rank_combo()
                    self._yield = len(self.poffins) * \
                        len(self.poffins[0].berries)
                    return

    def _apply_poffin(self, p: Poffin) -> None:
        if self.sheen >= 255:
            print("\t\t ** Do we even enter this?")
            return

        self.poffins_eaten += 1
        self.sheen = self._add_value(self.sheen, p.smoothness)
        self.coolness = self._add_value(self.coolness, p.flavor_values[0])
        self.beauty = self._add_value(self.beauty, p.flavor_values[1])
        self.cuteness = self._add_value(self.cuteness, p.flavor_values[2])
        self.cleverness = self._add_value(self.cleverness, p.flavor_values[3])  # noqa ES501
        self.toughness = self._add_value(self.toughness, p.flavor_values[4])

        self._all_values = [self.coolness, self.beauty, self.cuteness, self.cleverness, self.toughness]  # noqa ES501
        self.num_perfect_values = sum(
            [1 for x in self._all_values if x >= 255])

    def _rank_combo(self) -> int:
        """Return a rank of this 4-poffin combo.

                1 - everything is maxed\n
                2 - all categories maxed but still have some sheen\n
                3 - did not might criteria for 1 or 2, this is no good\n

        Returns:
            int: ranking
        """

        contest_values = self.num_perfect_values
        sheen_value = 10 if self.sheen >= 255 else 0
        total = contest_values + sheen_value

        if total == 15:
            return 1
        if total == 5:
            return 2
        return 3

    @classmethod
    def _get_unique_berries(cls, poffins):
        total_berries = set()
        for p in poffins:
            for berry in p.berries:
                total_berries.add(berry)
        return len(total_berries)

    @classmethod
    def _add_value(cls, current_value, additional_value):
        # NOTE: Interneal max 115 for additonal value - Controlled in poffin cooker
        return min(255, current_value + additional_value)

    def __repr__(self) -> str:
        amt = 36
        formated_poffin_string = '\n'.join(map(repr, self.poffins))
        return (
f"\t{formated_poffin_string}                                                          \n"  # noqa ES501
f"\t{BOLD}{outline}{'-' * amt}{RESET}{FLAVOR_COLORS['Dry']}      ---------------  {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| ******   Contest Stats    ****** |{RESET}{FLAVOR_COLORS['Dry']}     \\####|▓▓▓██|####/{RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}{'-' * amt}{RESET}{FLAVOR_COLORS['Dry']}      \\###|█▓▓▓█|###/ {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {FLAVOR_COLORS['Spicy']}{'(Spicy)':<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Spicy']}{'Coolness':<14}{RESET}:{bad_red if self.coolness < 255 else FLAVOR_COLORS['Bitter']}{self.coolness:>4} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Dry']}       `##|██▓▓▓|##'   {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {FLAVOR_COLORS['Dry']}{'(Dry)':<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Dry']}{'Beauty':<14}{RESET}:{bad_red if self.beauty < 255 else FLAVOR_COLORS['Bitter']}{self.beauty:>4} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Sour']}            ({FLAVOR_COLORS['Spicy']}O{FLAVOR_COLORS['Sour']})        {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {FLAVOR_COLORS['Sweet']}{'(Sweet)':<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Sweet']}{'Cuteness':<14}{RESET}:{bad_red if self.cuteness < 255 else FLAVOR_COLORS['Bitter']}{self.cuteness:>4} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Sour']}         .-'''''-.     {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {FLAVOR_COLORS['Bitter']}{'(Bitter)':<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Bitter']}{'Cleverness':<14}{RESET}:{bad_red if self.cleverness < 255 else FLAVOR_COLORS['Bitter']}{self.cleverness:>4} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Sour']}       .'  {FLAVOR_COLORS['Spicy']}* * *{FLAVOR_COLORS['Sour']}  `.   {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {FLAVOR_COLORS['Sour']}{'(Sour)':<8}{RESET} ->  {BOLD}{FLAVOR_COLORS['Sour']}{'Toughness':<14}{RESET}:{bad_red if self.toughness < 255 else FLAVOR_COLORS['Bitter']}{self.toughness:>4} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Sour']}      :  {FLAVOR_COLORS['Spicy']}*       *{FLAVOR_COLORS['Sour']}  :  {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}{'-' * amt}{RESET}{FLAVOR_COLORS['Sour']}     : ~ PO F F IN ~ : {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {RESET}{BOLD}Eaten{RESET}{bad_red if self.poffins_eaten > self._yield else RESET}{self.poffins_eaten:>6}{RESET}  {BOLD}{'Sheen':<14}{RESET}:{BOLD if self.sheen >= 255 else RESET}{self.sheen:>4}{RESET} {BOLD}{outline}|{RESET}{FLAVOR_COLORS['Sour']}     : ~ A W A R D ~ : {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}{'-' * amt}{RESET}{FLAVOR_COLORS['Sour']}      :  {FLAVOR_COLORS['Spicy']}*       *{FLAVOR_COLORS['Sour']}  :  {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}| {RESET}{BOLD}Rank{RESET} :{FLAVOR_COLORS['Bitter'] if self.rank == 1 else FLAVOR_COLORS['Spicy'] if self.rank == 2 else bad_red} {self.rank:<2}{RESET}{BOLD}    {'R/U':<6}{RESET}  {self.rarity:>5} : {self.unique_berries}{BOLD:<6}{outline}|{RESET}{FLAVOR_COLORS['Sour']}       `.  {FLAVOR_COLORS['Spicy']}* * *{FLAVOR_COLORS['Sour']}  .'   {RESET}   \n"  # noqa ES501
f"\t{BOLD}{outline}{'-' * amt}{RESET}{FLAVOR_COLORS['Sour']}         `-.....-'     {RESET}   \n"  # noqa ES501
f"{BOLD}{outline}{'-' * 75}{RESET}\n")  # noqa ES501

    def __str__(self) -> str:
        formated_poffin_string = '\n'.join(map(str, self.poffins))

        # \n"
        return (f"Rank: {self.rank} Poffins eaten: {self.poffins_eaten} Rarity: {self.rarity:<3} Unique Berries: {self.unique_berries}")
        # f"\t{self.coolness}, {self.beauty}, {self.cuteness}, {self.cleverness}, {self.toughness} : {self.sheen}"  # noqa ES501
        # f"{formated_poffin_string}\n")


def main():
    """
    Level: 148 - Super Mild Poffin   Smoothness: 30
        [148, 0, 0, 28, 0]
        Main Flavor: Spicy
        All Flavors: Spicy - Bitter
        Second strongest flavor value: 28
    """

    recipes = (
        [berry_library.petaya_berry, berry_library.enigma_berry,
            berry_library.liechi_berry, berry_library.custap_berry],
        [berry_library.apicot_berry, berry_library.micle_berry,
            berry_library.ganlon_berry, berry_library.jaboca_berry],
        [berry_library.apicot_berry, berry_library.custap_berry,
            berry_library.lansat_berry, berry_library.salac_berry],
        [berry_library.petaya_berry, berry_library.enigma_berry,
            berry_library.ganlon_berry, berry_library.jaboca_berry],
        [berry_library.apicot_berry, berry_library.custap_berry,
            berry_library.salac_berry, berry_library.rowap_berry]
    )
    cooker = PoffinCooker()
    stats = ContestStats()
    pf = PoffinFactory(cooker, recipes)
    poffins = pf.generate_custom_poffin_list_from_recipes(recipes)

    t = set()
    for i in range(len(poffins)):
        for j in poffins[i].berries:
            print(j)
            t.add(j)
    print()
    for _ in t:
        print(_)
    assert len(t) == 11, f"{len(t)} {len(poffins) * 4}"
    stats.apply_poffins(poffins)

    print(stats)
    print(repr(stats))


if __name__ == "__main__":
    main()
