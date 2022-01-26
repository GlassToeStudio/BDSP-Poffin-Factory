from abc import ABCMeta, abstractmethod

from make_poffins.stats.contest_stats import ContestStats


class IContestStatsFilterInterface(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self._value = value
        """The value by which we are comparing"""

    @abstractmethod
    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class FilterContestStatsBy_Rank_LT(IContestStatsFilterInterface):
    """Filter out any stats with a rank < the given value

        Notes:\n
                * 1 - Everything is maxed\n
                * 2 - All categories maxed but still have some sheen\n
                * 3 - Did not meet criteria for 1 or 2, this is not good\n

        Returns:
            list[ContestStats]: List of contest_stats with rank >= the given value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        self.value = min(self.value, 3)
        return [cs for cs in contest_stats if cs.rank >= self.value]


class FilterContestStatsBy_Rank_GT(IContestStatsFilterInterface):
    """Filter out any stats with a rank > the given value

        Notes:\n
                * 1 - Everything is maxed\n
                * 2 - All categories maxed but still have some sheen\n
                * 3 - Did not meet criteria for 1 or 2, this is not good\n

        Returns:
            list[ContestStats]: List of contest_stats with rank <= the given value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        self.value = max(self.value, 1)
        return [cs for cs in contest_stats if cs.rank <= self.value]


class FilterContestStatsBy_Rarity_LT(IContestStatsFilterInterface):
    """Filter out any contest stats with a rarity less than the given value

    Notes:\n
            * min =  7 x num poffins\n
            * max = 60 x num poffins\n

        THIS WILL NOT LEAVE MANY BERRIES!\n

    Returns:
        list[ContestStat]: contest stats with rarity <= value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        num_poffins = len(contest_stats[0].poffins)
        assert ((7*num_poffins)-1) < self._value <= ((60*num_poffins))
        return [cs for cs in contest_stats if cs.rarity >= self._value]


class FilterContestStatsBy_Rarity_GT(IContestStatsFilterInterface):
    """Filter out any contest stats with a rarity greater than the given value

    Notes:\nk
            * min =  4 x num poffins
            * max = 45 x num poffins

        THIS WILL NOT LEAVE MANY BERRIES!\n

    Returns:
        list[ContestStat]: contest stats with rarity <= value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        num_poffins = len(contest_stats[0].poffins)
        assert (4*num_poffins) <= self._value < ((45*num_poffins)+1)
        return [cs for cs in contest_stats if cs.rarity <= self._value]


class FilterContestStatsBy_Poffins_Eaten_LT(IContestStatsFilterInterface):
    """Filter out any contest stats with poffins eaten less than the given value

    Notes:\n
            * Not a usefule filter imo
            * 5 poffin combos : 10 poffins eaten great
            * 5 poffin combos : 10 poffins eaten ok
            * 3 poffin combos : 9 poffins eaten great
            * 3 poffin combos : 12 poffins eaten ok
            * etc

    Returns:
        list[ContestStat]: contest stats with poffins eaten >= value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return [cs for cs in contest_stats if cs.poffins_eaten >= self._value]


class FilterContestStatsBy_Poffins_Eaten_GT(IContestStatsFilterInterface):
    """Filter out any contest stats with poffins eaten greater than the given value

    Notes:\n
            * No magic value but
            * 5 poffin combos : 10 poffins eaten great
            * 5 poffin combos : 10 poffins eaten ok
            * 3 poffin combos : 9 poffins eaten great
            * 3 poffin combos : 12 poffins eaten ok
            * etc

    Returns:
        list[ContestStat]: contest stats with poffins eaten <= value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return [cs for cs in contest_stats if cs.poffins_eaten <= self._value]


class FilterContestStatsBy_Num_Perfect_values_GT(IContestStatsFilterInterface):
    """Filter out any contest stats with more than the given amount of perfect values.

    Notes:\n
            * 1 - 5

    Returns:
        list[ContestStat]: contest stats with n perfect values > value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return [cs for cs in contest_stats if cs.num_perfect_values <= self._value]


class FilterContestStatsBy_Num_Perfect_values_LT(IContestStatsFilterInterface):
    """Filter out any contest stats with less than the given amount of perfect values

    Notes:\n
            * 1 - 5

    Returns:
        list[ContestStat]: contest stats with n perfect values < value
    """

    def execute(self, contest_stats: list[ContestStats]) -> list[ContestStats]:
        return [cs for cs in contest_stats if cs.num_perfect_values >= self._value]
