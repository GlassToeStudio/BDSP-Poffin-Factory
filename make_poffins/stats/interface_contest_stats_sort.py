from abc import ABCMeta, abstractmethod
from operator import attrgetter

from make_poffins.stats.contest_stats import ContestStats


class IContestStatsSortInterface(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self.value = value
        """Check criteria against this value"""
        self.reverse = reverse
        """Rverse the order of the list if True

        Note:\n
                * default: False
                * by defualt sorters are sorted by best to worst.
        """

    @abstractmethod
    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class SortOnContestStats_Attrs(IContestStatsSortInterface):
    """Sort contst stats by multiple values in ascending (False) or descenidng (True) order.

    Format = (('attr', Reversed?), ('name', False))

    Notes;\n
            * H: means Higher is better so supply True to the second argument
                - (("coolness", True), )
            * L: means Lower is better so supply False to the second argument
                - (("rarity", False), )
            *  : means neither is better - False for ascending, True for descending
                - (("rarity", False), )
    Attr:
        *  0 | int : coolness           * H\n
        *  1 | int : beauty             * H\n
        *  2 | int : cuteness           * H\n
        *  3 | int : cleverness         * H\n
        *  4 | int : toughness          * H\n
        *  5 | int : sheen              * H\n
        *  6 | int : poffins_eaten      * L\n
        *  7 | int : num_perfect_values * H\n
        *  8 | int : unique_berries     * L\n
        *  9 | int : rarity             * L\n
        * 10 | int : rank               * L\n

    https://docs.python.org/3/howto/sorting.html

    Returns:
        list[ContestStats]: sorted list of contet stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        for key, reverse in reversed(self._value):
            contest_stats.sort(key=attrgetter(key), reverse=reverse)
        return contest_stats


class SortOnContestStats_Coolness(IContestStatsSortInterface):
    """Sort contest_stats by the value of their coolness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.coolness, reverse=not self.reverse)


class SortOnContestStats_Beauty(IContestStatsSortInterface):
    """Sort contest_stats by the value of their beauty, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.beauty, reverse=not self.reverse)


class SortOnContestStats_Cuteness(IContestStatsSortInterface):
    """Sort contest_stats by the value of their cuteness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.cuteness, reverse=not self.reverse)


class SortOnContestStats_Cleverness(IContestStatsSortInterface):
    """Sort contest_stats by the value of their cleverness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.cleverness, reverse=not self.reverse)


class SortOnContestStats_Toughness(IContestStatsSortInterface):
    """Sort contest_stats by the value of their toughness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.toughness, reverse=not self.reverse)


class SortOnContestStats_Sheen(IContestStatsSortInterface):
    """Sort contest_stats by the value of their sheen, descending.

        Notes:\n
            * List reteruned in descending order by default
                - 255, 254, ..., 2, 1
            * Higher is not always better
            * Lower is not always better

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.toughness, reverse=not self.reverse)


class SortOnContestStats_PoffinsEaten(IContestStatsSortInterface):
    """Sort contest_stats by the value of their poffins eaten, ascending.

            * Lower is better.
            * List in Ascending Order
    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.poffins_eaten, reverse=self.reverse)


class SortOnContestStats_NumPerfectValues(IContestStatsSortInterface):
    """Sort contest_stats by their number of perfect values (value of 255), descending.

            * Higher is better.
            * List in Descending Order
    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.num_perfect_values, reverse=not self.reverse)


class SortOnContestStats_NumUniqueBerries(IContestStatsSortInterface):
    """Sort contest_stats by their number of unique berries used, ascending.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.unique_berries, reverse=self.reverse)


class SortOnContestStats_Rarity(IContestStatsSortInterface):
    """Sort contest_stats by the rarity of the berries used, asceding.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.rarity, reverse=self.reverse)


class SortOnContestStats_Rank(IContestStatsSortInterface):
    """Sort contest_stats by their rank, ascending.

            * Lower is better.
            * List in Descending Order

        Notes:\n
                * 1 - Everything is maxed\n
                * 2 - All categories maxed but still have some sheen\n
                * 3 - Did not meet criteria for 1 or 2, this is not good\n

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return sorted(contest_stats, key=lambda x: x.rank, reverse=self.reverse)
