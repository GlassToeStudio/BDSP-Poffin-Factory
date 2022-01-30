from abc import ABCMeta, abstractmethod

from make_poffins.berry.berry import Berry


class IBerryFilter(metaclass=ABCMeta):
    """Berry Filter Parent Class - abstract - not to be instanced."""

    def __init__(self, value: int | str):
        self._value = value

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
        return f"{self.__class__.__name__} with a value of {self._value}"


class RemoveBerriesWith_AnyFlavorValue_LessThan(IBerryFilter):
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
        assert 10 < self._value < 40
        temp_list = berries.copy()
        for b in temp_list:
            for i in range(5):
                if 0 < b.flavor_values[i] < self._value:
                    berries.remove(b)
                    break
        return berries


class RemoveBerriesWith_AnyFlavorValue_GreaterThan(IBerryFilter):
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
        assert 10 < self._value < 40
        temp_list = berries.copy()
        for b in temp_list:
            for i in range(5):
                if 0 < self._value < b.flavor_values[i]:
                    berries.remove(b)
                    break
        return berries


class RemoveBerriesWith_Smoothness_LessThan(IBerryFilter):
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
        return [b for b in berries if b.smoothness >= self._value]


class RemoveBerriesWith_Smoothness_GreaterThan(IBerryFilter):
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
        return [b for b in berries if b.smoothness <= self._value]


class RemoveBerriesWith_MainFlavorValue_LessThan(IBerryFilter):
    """Filter out any berries < the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor_value >= self._value]


class RemoveBerriesWith_MainFlavorValue_GreaterThan(IBerryFilter):
    """Filter out any berries > the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor_value <= self._value]


class RemoveBerriesWith_MainFlavorName(IBerryFilter):
    """Filter out any berries that is not of the given flavor.

    Args:
        Flavor (str): The flavor berries to keep

    Returns:
        list[Berry]: List of berries that are the given flavor
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.main_flavor.lower() == self._value.lower()]


class RemoveBerriesWith_NumberOfFlavors_LessThan(IBerryFilter):
    """Filter out any berries with total number of flavors  < the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Berry]: List of berries with flavors >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.num_flavors >= self._value]


class RemoveBerriesWith_NumberOfFlavors_GreaterThan(IBerryFilter):
    """Filter out any berries with total number of flavors > the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Berry]: List of berries with flavors <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.num_flavors <= self._value]


class RemoveBerriesWith_Rarity_LessThan(IBerryFilter):
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
        assert 1 <= self._value < 15
        return [b for b in berries if b.rarity >= self._value]


class RemoveBerriesWith_Rarity_GreaterThan(IBerryFilter):
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
        assert 1 < self._value <= 15
        return [b for b in berries if b.rarity <= self._value]


class RemoveBerriesWith_WeakenedMainFlavorValue_LessThan(IBerryFilter):
    """Filter out any berries < the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level >= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor_value >= self._value]


class RemoveBerriesWith_WeakenedMainFlavorValue_GreaterThan(IBerryFilter):
    """Filter out any berries > the passed in value.

    Args:
        Level (int): The minimum level berry to keep

    Returns:
        list[Berry]: List of berries with a level <= the passed in value.
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor_value <= self._value]


class RemoveBerriesWith_WeakenedMainFlavorName(IBerryFilter):
    """Filter out any berries that is not of the given weakened flavor.

    Args:
        Flavor (str): The flavor berries to keep

    Returns:
        list[Berry]: List of berries that are the given flavor
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b._weakened_main_flavor.lower() == self._value.lower()]


class RemoveBerriesWith_id_NotEqual(IBerryFilter):
    """Filter out any berries whose __id__ does not equal the passed in value.


    Returns:
        list[Berry]: berries.__id__ == value
    """

    def execute(self, berries: list[Berry]) -> list[Berry]:
        return [b for b in berries if b.__id__ == self._value]
