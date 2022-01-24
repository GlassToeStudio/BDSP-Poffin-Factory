from abc import ABCMeta, abstractmethod

from make_poffins.berry.berry import Berry


class IBerryFilterInterface(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self.value = value

    @abstractmethod
    def execute(self, berries: list[Berry]) -> list[Berry]:
        """Process the berries according to this filtering rule.

        Args:
            berries (list[Berry]): berries to filter

        Raises:
            NotImplementedError: Part of interface

        Returns:
            list[Berry]: filtered berries
        """
        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__} with a value of {self.value}"


class FilterBerriesBy_AnyFlavorValue_LessThan(IBerryFilterInterface):
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


class FilterBerriesBy_AnyFlavorValue_GreaterThan(IBerryFilterInterface):
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


class FilterBerriesBy_Smoothness_LessThan(IBerryFilterInterface):
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


class FilterBerriessBy_Smoothness_GreaterThan(IBerryFilterInterface):
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


class FilterBerriesBy_MainFlavorValue_LessThan(IBerryFilterInterface):
    """Filter out any berries < the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor_value >= self.value]


class FilterBerriesBy_MainFlavorValue_GreaterThan(IBerryFilterInterface):
    """Filter out any berries > the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor_value <= self.value]


class FilterBerriesBy_MainFlavorName(IBerryFilterInterface):
    """Filter out any berries that is not of the given flavor.

    Args:
        Flavor (str): The flavor berries to keep

    Returns:
        list[Berry]: List of berries that are the given flavor
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor.lower() == self.value.lower()]


class FilterBerryiesBy_NumberOfFlavors_LessThan(IBerryFilterInterface):
    """Filter out any berries with total number of flavors  < the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Berry]: List of berries with flavors >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.num_flavors >= self.value]


class FilterBerryiesBy_NumberOfFlavors_GreaterThan(IBerryFilterInterface):
    """Filter out any berries with total number of flavors > the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Berry]: List of berries with flavors <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.num_flavors <= self.value]


class FilterBerriessBy_Rarity_LessThan(IBerryFilterInterface):
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


class FilterBerriessBy_Rarity_GreaterThan(IBerryFilterInterface):
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
        assert 1 <= self.value <= 15
        return [b for b in berries if b.rarity <= self.value]


class FilterBerriesBy_WeakenedMainFlavorValue_LessThan(IBerryFilterInterface):
    """Filter out any berries < the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor_value >= self.value]


class FilterBerriesBy_WeakenedMainFlavorValue_GreaterThan(IBerryFilterInterface):
    """Filter out any berries > the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor_value <= self.value]


class FilterBerriesBy_WeakenedMainFlavorName(IBerryFilterInterface):
    """Filter out any berries that is not of the given weakened flavor.

    Args:
        Flavor (str): The flavor berries to keep

    Returns:
        list[Berry]: List of berries that are the given flavor
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor.lower() == self.value.lower()]


class FilterBerriessBy__id__(IBerryFilterInterface):
    """Filter out any berries whose __id__ does not equal the passed in value.


    Returns:
        list[Berry]: berries.__id__ == value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.__id__ == self.value]
