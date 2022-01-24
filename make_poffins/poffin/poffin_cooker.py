"""https://bulbapedia.bulbagarden.net/wiki/Poffin#Cooking"""
import math

from make_poffins.berry.berry import Berry
from make_poffins.constants import subtract_weakening_flavors
from make_poffins.poffin.poffin import Poffin


class PoffinCooker:
    """Give it some berries and it will cook a poffin in time = t"""

    def __init__(self, cook_time: float = 40, spills: int = 0, burns: int = 0):  # noqa ES501
        self.cook_time = cook_time
        self.spills = spills
        self.burns = burns

    @classmethod
    def __sum_over_all_berries__(cls, berries: list[Berry]) -> list[int]:
        """For each of the 5 flavors, sum the value for each berry.

        Args:
            berries (list[Berry]): list of all berries in recipe

        Returns:
            list[int]: summed_berry_values
        """

        summed_berry_values = [0] * 5
        for i in range(5):
            for berry in berries:
                summed_berry_values[i] += berry.flavor_values[i]
        return summed_berry_values

    @classmethod
    def __subtract_weakening_flavors__(cls, poffin_values: list[int]) -> list[int]:  # noqa ES501
        """Each flavor has a corresponding flavor that weakens it.
        Subtract all the weaken factors from each flavor.
        """

        return subtract_weakening_flavors(poffin_values)

    def __decrease_by_negative_flavors__(self, poffin_values: list[int]) -> list[int]:  # noqa ES501
        """Once subtracted, count the number of negative values and
        subract 1 from every value for each negative value.
        """
        negatives = self.__count_negative_values__(poffin_values)
        return [poffin_values[i] - negatives for i in range(5)]  # noqa ES501

    def __multiply_by_cooking_time_bonus__(self, poffin_values: list[int]) -> list[int]:  # noqa ES501
        """Multiply the remaining values by a bonus for cooking time.
        """

        bonus = 60.0 / self.cook_time
        return [math.floor(poffin_values[i] * bonus) for i in range(5)]

    def __subtract_spills_and_burns__(self, poffin_values: list[int]) -> list[int]:  # noqa ES501
        """Reduce each value by the number of spills and the number of burns.

        """
        # TODO: I set the max value to 115 since I think thats all you can get in game.
        return [min(poffin_values[i] - (self.spills + self.burns), 115) for i in range(5)]  # noqa ES501
        #return [min(poffin_values[i] - (self.spills + self.burns), 115) for i in range(5)]  # noqa ES501

    @classmethod
    def __set_negatives_to_zero__(cls, poffin_values: list[int]) -> list[int]:
        """Set any negative value to 0"""

        return [x if x > 0 else 0 for x in poffin_values]

    @classmethod
    def __calc_smoothness__(cls, berries: list[Berry]) -> int:
        """Calculate the smoothness of the poffin.

        smoothness_p = ⌊Σⁿ(smoothness_b) / n⌋ - n

        -9 for having 6 max level friends help cook.

        (there can be 6 total friends so is it [friends * 1.5]?)

        Args:
            berries (list[Berry]): list of all berries in recipe
        """

        n = len(berries)
        berry_smoothness = sum(x.smoothness for x in berries)
        return math.floor((berry_smoothness / n) - n)

    @classmethod
    def __adjust_affection__(cls, smoothness: int):
        """I dont know how this works"""
        return smoothness - 9

    @classmethod
    def __count_negative_values__(cls, poffin_values: list[int]) -> list[int]:
        """Return the number of negative values.

        Returns:
            int: total number of negative values
        """

        return sum(1 for x in poffin_values if x < 0)

    def cook(self, berries: list[Berry]) -> Poffin:  # noqa ES501
        """Cook the poffin.

        Args:
            berries (list[Berry]): Berries to use in the recipe

        Returns:
            Poffin: cooked poffin
        """

        poffin_values = self.__sum_over_all_berries__(berries)
        poffin_values = self.__subtract_weakening_flavors__(poffin_values)
        poffin_values = self.__decrease_by_negative_flavors__(poffin_values)
        poffin_values = self.__multiply_by_cooking_time_bonus__(poffin_values)
        poffin_values = self.__subtract_spills_and_burns__(poffin_values)
        poffin_values = self.__set_negatives_to_zero__(poffin_values)
        smoothness = self.__calc_smoothness__(berries)
        smoothness = self.__adjust_affection__(smoothness)
        return Poffin(poffin_values, smoothness, berries)
