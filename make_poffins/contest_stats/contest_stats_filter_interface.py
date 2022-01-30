from abc import ABCMeta, abstractmethod


class IContestStatsFilter(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self._value = value

    @property
    @abstractmethod
    def value(self):
        """The value by which we are comparing"""
        raise NotImplementedError

    @property
    @abstractmethod
    def attribute(self):
        """The name of this attribute"""
        raise NotImplementedError

    @property
    @abstractmethod
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class RemoveContestStatsWith_Rank_LessThan(IContestStatsFilter):
    """Filter out any stats with a rank < the given value

        Notes:\n
                * 1 - Everything is maxed\n
                * 2 - All categories maxed but still have some sheen\n
                * 3 - Did not meet criteria for 1 or 2, this is not good\n

        A value less than means "better"

        Returns:
            list[ContestStats]: List of contest_stats with rank >= the given value
    """

    @property
    def value(self):
        """The value by which we are comparing"""
        assert 1 <= self._value <= 3
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "rank"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 0


class RemoveContestStatsWith_Rank_GreaterThan(IContestStatsFilter):
    """Filter out any stats with a rank > the given value

        Notes:\n
                * 1 - Everything is maxed\n
                * 2 - All categories maxed but still have some sheen\n
                * 3 - Did not meet criteria for 1 or 2, this is not good\n

        A value greater than means "worse"        

        Returns:
            list[ContestStats]: List of contest_stats with rank <= the given value
    """

    @property
    def value(self):
        """The value by which we are comparing"""
        assert 1 <= self._value <= 3
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "rank"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 1


class RemoveContestStatsWith_Rarity_LessThan(IContestStatsFilter):
    """Filter out any contest stats with a rarity less than the given value

    Notes:\n
            * min =  7 x num poffins\n
            * max = 60 x num poffins\n


    Returns:
        list[ContestStat]: contest stats with rarity <= value
    """

    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "rarity"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 0


class RemoveContestStatsWith_Rarity_GreaterThan(IContestStatsFilter):
    """Filter out any contest stats with a rarity greater than the given value

    Notes:\n
            * min =  4 x num poffins
            * max = 45 x num poffins

    Returns:
        list[ContestStat]: contest stats with rarity <= value
    """

    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "rarity"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 1


class RemoveContestStatsWith_PoffinsEaten_LessThan(IContestStatsFilter):
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

    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "poffins_eaten"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 0


class RemoveContestStatsWith_PoffinsEaten_GreaterThan(IContestStatsFilter):
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
    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "poffins_eaten"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 1


class RemoveContestStatsWith_NumPerfectValues_LessThan(IContestStatsFilter):
    """Filter out any contest stats with less than the given amount of perfect values

    Notes:\n
            * 1 - 5

    Returns:
        list[ContestStat]: contest stats with n perfect values < value
    """
    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "num_perfect_values"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 0


class RemoveContestStatsWith_NumPerfectValues_GreaterThan(IContestStatsFilter):
    """Filter out any contest stats with more than the given amount of perfect values.

    Notes:\n
            * 1 - 5

    Returns:
        list[ContestStat]: contest stats with n perfect values > value
    """

    @property
    def value(self):
        """The value by which we are comparing"""
        return self._value

    @property
    def attribute(self):
        """The name of this attribute"""
        return "num_perfect_values"

    @property
    def op(self):
        """     * 0 : Less than\n       * 1 : Greater Than"""
        return 1
