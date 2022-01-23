from abc import ABCMeta, abstractmethod

from make_poffins.berry.berry import Berry


class IBerryFilterInterface(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self.value = value

    @abstractmethod
    def execute(self, berries: list[Berry]) -> list[Berry]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class FilterBerriesBy_MainFlavorValue(IBerryFilterInterface):
    """Filter out any berries < the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor_value >= self.value]


class FilterBerriesBy_Flavor(IBerryFilterInterface):
    """Filter out any berries that is not of the given flavor.

    Args:
        Flavor (str): The flavor berries to keep

    Returns:
        list[Berry]: List of berries that are the given flavor
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor.lower() == self.value.lower()]


class FilterBerryiesBy_NumberOfFlavorsLessThan(IBerryFilterInterface):
    """Filter out any berries with total number of flavors  < the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Berry]: List of berries with flavors >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.num_flavors >= self.value]


class FilterBerriesBy_AnyFlavorValueLessThan(IBerryFilterInterface):
    """Filter out any berries any flavor value  < the passed in value.

    Args:
        Level (int): The minimum flavor value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

        min = 10\n
        max = 40\n
        https://progameguides.com/pokemon/complete-poffin-recipe-guide-for-pokemon-brilliant-diamond-and-shining-pearl/

    Returns:
        list[Berry]: List of berries with all flavor values >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        assert 10 < self.value < 40
        temp_list = berries.copy()
        for b in temp_list:
            for i in range(5):
                if 0 < b.flavor_values[i] < self.value:
                    berries.remove(b)
                    break
        return berries


class FilterBerriesBy_AnyFlavorValueGreaterThan(IBerryFilterInterface):
    """Filter out any berries any flavor value > the passed in value.

    Args:
        Level (int): The minimum flavor value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

        min = 10\n
        max = 40\n
        https://progameguides.com/pokemon/complete-poffin-recipe-guide-for-pokemon-brilliant-diamond-and-shining-pearl/

    Returns:
        list[Berry]: List of berries with all flavor values <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        assert 10 < self.value < 40
        temp_list = berries.copy()
        for b in temp_list:
            for i in range(5):
                if 0 < self.value < b.flavor_values[i]:
                    berries.remove(b)
                    break
        return berries


class FilterBerriesBy_SmoothnessLessThan(IBerryFilterInterface):
    """Filter out any berries with a smoothnes less than the given value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

        min = 20\n
        max = 60\n
        https://progameguides.com/pokemon/complete-poffin-recipe-guide-for-pokemon-brilliant-diamond-and-shining-pearl/

    Returns:
        list[Berry]: berries with smoothness >= value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.smoothness >= self.value]


class FilterBerriessBy_SmoothnessGreaterThan(IBerryFilterInterface):
    """Filter out any berries with a smoothnes greater than the given value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

        min = 20\n
        max = 60\n
        https://progameguides.com/pokemon/complete-poffin-recipe-guide-for-pokemon-brilliant-diamond-and-shining-pearl/

    Returns:
        list[Berry]: berries with smoothness <= value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.smoothness <= self.value]


class FilterBerriessBy_RarityLessThan(IBerryFilterInterface):
    """Filter out any berries with a rarity less than the given value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

    RARITY_TABLE = { smoothness : rarity
        20: 1,
        25: 3,
        30: 5,
        35: 7,
        40: 9,
        50: 11,
        60: 15,
        255: 255  # For those berries that do not exist.
    }

    Returns:
        list[Berry]: berries with smoothness >= value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        assert 1 < self.value < 15
        return [b for b in berries if b.rarity >= self.value]


class FilterBerriessBy_RarityGreaterThan(IBerryFilterInterface):
    """Filter out any berries with a rarity greater than the given value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

    RARITY_TABLE = { smoothness : rarity
        20: 1,
        25: 3,
        30: 5,
        35: 7,
        40: 9,
        50: 11,
        60: 15,
        255: 255  # For those berries that do not exist.
    }

    Returns:
        list[Berry]: berries with smoothness <= value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        assert 1 < self.value < 15
        return [b for b in berries if b.rarity <= self.value]
