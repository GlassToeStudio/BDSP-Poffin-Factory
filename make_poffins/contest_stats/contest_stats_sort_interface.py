from abc import ABCMeta, abstractmethod
from operator import attrgetter

from make_poffins.contest_stats.contest_stats import ContestStats


class IContestStatsSort(metaclass=ABCMeta):
    def __init__(self, value=None, reverse=False):
        self._value = value
        """Check criteria against this value"""
        self._reverse = reverse
        """Rverse the order of the list if True

        Note:\n
                * default: False
                * by defualt sorters are sorted by best to worst.
        """
    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def reverse(self):
        raise NotImplementedError

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        """Process the contest stats according to this sorting rule.

        Args:
            contest stats (list[ContestStats]): contest stats to sort

        Returns:
            list[ContestStats]: sorted contest stats
        """
        contest_stats.sort(key=attrgetter(self.value), reverse=self.reverse)
        return contest_stats

    def __str__(self):
        return self.__class__.__name__


class SortContestStatsBy_Coolness(IContestStatsSort):
    """Sort contest_stats by the value of their coolness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "coolness"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_Beauty(IContestStatsSort):
    """Sort contest_stats by the value of their beauty, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "beauty"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_Cuteness(IContestStatsSort):
    """Sort contest_stats by the value of their cuteness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "cuteness"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_Cleverness(IContestStatsSort):
    """Sort contest_stats by the value of their cleverness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "cleverness"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_Toughness(IContestStatsSort):
    """Sort contest_stats by the value of their toughness, descending.

            * Higher is better.
            * List in Descending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "toughness"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_Sheen(IContestStatsSort):
    """Sort contest_stats by the value of their sheen, descending.

        Notes:\n
            * List reteruned in descending order by default
                - 255, 254, ..., 2, 1
            * Higher is not always better
            * Lower is not always better

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "sheen"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_PoffinsEaten(IContestStatsSort):
    """Sort contest_stats by the value of their poffins eaten, ascending.

            * Lower is better.
            * List in Ascending Order
    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "poffins_eaten"

    @property
    def reverse(self):
        return self._reverse


class SortContestStatsBy_NumPerfectValues(IContestStatsSort):
    """Sort contest_stats by their number of perfect values (value of 255), descending.

            * Higher is better.
            * List in Descending Order
    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "num_perfect_values"

    @property
    def reverse(self):
        return not self._reverse


class SortContestStatsBy_NumUniqueBerries(IContestStatsSort):
    """Sort contest_stats by their number of unique berries used, ascending.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "unique_berries"

    @property
    def reverse(self):
        return self._reverse


class SortContestStatsBy_Rarity(IContestStatsSort):
    """Sort contest_stats by the rarity of the berries used, asceding.

            * Lower is better.
            * List in Ascending Order

    Returns:
        list[ContestStats]: sorted list of contest_stats
    """
    @property
    def value(self):
        return "rarity"

    @property
    def reverse(self):
        return self._reverse


class SortContestStatsBy_Rank(IContestStatsSort):
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
    @property
    def value(self):
        return "rank"

    @property
    def reverse(self):
        return self._reverse
