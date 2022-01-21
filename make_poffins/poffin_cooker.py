import math

from make_poffins.berry import Berry
from make_poffins.constants import subtract_weakening_flavors
from make_poffins.poffin import Poffin


class PoffinCooker:
    """Give it some berries and it will cook a poffin in time = t"""

    def __init__(self):
        self.__values__ = [0] * 5
        """Starting with the berry values [0, 10, 10, 0, 0] and resulting in, for example, [0, 0, 0, 8, 8]"""  # noqa ES501
        self.__smoothness__ = 0
        """Smoothness is the value added to sheen"""
        self.__poffin__ = None
        """The resulting poffin"""
        self.__negative_values__ = None
        """Number of values that are negative"""

    def __sum_over_all_berries__(self, berries: list[Berry]) -> None:
        """For each of the 5 flavors, sum the value for each berry.

        Args:
            berries (list[Berry]): list of all berries in recipe
        """

        for i in range(5):
            for berry in berries:
                self.__values__[i] += berry.flavor_values[i]

    def __subtract_weakening_flavors__(self) -> None:
        """Each flavor has a corresponding flavor that weakens it.
        Subtract all the weaken factors from each flavor.
        """

        self.__values__ = subtract_weakening_flavors(self.__values__)

    def __decrease_by_negative_flavors__(self) -> None:
        """Once subtracted, count the number of negative values and
        subract 1 from every value for each negative value.
        """

        for i in range(5):
            self.__values__[i] -= self.__count_negative_values__()

    def __multiply_by_cooking_time_bonus__(self, cook_time: float) -> None:
        """Multiply the remaining values by a bonus for cooking time.

            bonus = 60.0 / cook_time
        Args:
            cook_time (float): Time it takes to cook a poffin
        """

        bonus = 60.0 / cook_time
        for i in range(5):
            self.__values__[i] = math.floor(self.__values__[i] * bonus)

    def __subtract_spills_and_burns__(self, spills: int, burns: int) -> None:
        """Reduce each value by the number of spills and the number of burns.

        Args:
            spills (int): Number of spills
            burns (int): Number of burns
        """

        self.__values__ = [self.__values__[i] - (spills + burns) for i in range(5)]

    def __set_negatives_to_zero__(self) -> None:
        """Set any negative value to 0"""

        self.__values__ = [x if x > 0 else 0 for x in self.__values__]

    def __calc_smoothness__(self, berries: list[Berry]) -> None:
        """Calculate the smoothness of the poffin.

        smoothness_p = ⌊Σⁿ(smoothness_b) / n⌋ - n

        -9 for having 6 max level friends help cook.

        (there can be 6 total friends so is it [friends * 1.5]?)

        Args:
            berries (list[Berry]): list of all berries in recipe
        """

        n = len(berries)
        berry_smoothness = sum(x.smoothness for x in berries)
        self.__smoothness__ = math.floor((berry_smoothness / n) - n)

    def __adjust_affection__(self):
        """I dont know how this works"""
        self.__smoothness__ -= 9

    def __count_negative_values__(self) -> int:
        """Return the number of negative values.

        Will check to see if this is already calculated.
        If so, return the value
        else calculate and store the value and return it.

        Returns:
            int: total number of negative values
        """

        if self.__negative_values__ is None:
            self.__negative_values__ = sum(1 for x in self.__values__ if x < 0)
        return self.__negative_values__

    def cook(self, berries: list[Berry], cook_time: float, spills: int, burns: int) -> None:  # noqa ES501
        """Cook the poffin.

        Args:
            berries (list[Berry]): Berries to use in the recipe
            cook_time (float): Time it takes to cook
            spills (int): Number of spills
            burns (int): Number of burns
        """

        self.__sum_over_all_berries__(berries)
        self.__subtract_weakening_flavors__()
        self.__decrease_by_negative_flavors__()
        self.__multiply_by_cooking_time_bonus__(cook_time)
        self.__subtract_spills_and_burns__(spills, burns)
        self.__set_negatives_to_zero__()
        self.__calc_smoothness__(berries)
        self.__adjust_affection__()
        self.__poffin__ = Poffin(self.__values__, self.__smoothness__, berries)

    def complete(self) -> Poffin:
        """Return the poffin.

        Returns:
            Poffin: Poffin
        """
        return self.__poffin__
