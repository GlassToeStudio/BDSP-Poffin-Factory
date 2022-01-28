from abc import ABCMeta, abstractmethod

from make_poffins.poffin.poffin import Poffin


class IPoffinFilterInterface(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self._value = value

    @abstractmethod
    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class FilterPoffinsBy_Flavor(IPoffinFilterInterface):
    """Filter out any poffins that is not of the given flavor.

    Args:
        Flavor (str): The flavor poffins to keep

    Notes:\n
            * "Spicy"\n
            * "Dry"\n
            * "Bitter"\n
            * "Sweet"\n
            * "Sour"\n

    Returns:
        list[Poffin]: List of poffins that are the given flavor
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.main_flavor.lower() == self._value.lower()]


class FilterPoffinsBy_Level_LessThan(IPoffinFilterInterface):
    """Filter out any poffins < the passed in value.

    Args:
        Level (int): The minimum level poffin to keep

    Returns:
        list[Poffin]: List of poffins with a level >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.level >= self._value]


class FilterPoffinsBy_Level_GreaterThan(IPoffinFilterInterface):
    """Filter out any poffins > the passed in value.

    Args:
        Level (int): The maximum level poffin to keep

    Returns:
        list[Poffin]: List of poffins with a level <= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.level <= self._value]


class FilterPoffinsBy_SecondLevel_LessThan(IPoffinFilterInterface):
    """Filter out any poffins < the passed in value.

    Args:
        Level (int): The minimum level poffin to keep

    Returns:
        list[Poffin]: List of poffins with a level >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.second_level >= self._value]


class FilterPoffinsBy_SecondLevel_GreaterThan(IPoffinFilterInterface):
    """Filter out any poffins > the passed in value.

    Args:
        Level (int): The maximum level poffin to keep

    Returns:
        list[Poffin]: List of poffins with a level <= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.second_level <= self._value]


class FilterPoffinsBy_NumberOfFlavors_LessThan(IPoffinFilterInterface):
    """Filter out any poffins with total number of flavors  < the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Notes:\n
            * 1 - 5 flavors

    Returns:
        list[Poffin]: List of poffins with number of flavors >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert 0 < self._value <= 5
        return [p for p in poffins if p.num_flavors >= self._value]


class FilterPoffinsBy_NumberOfFlavors_GreaterThan(IPoffinFilterInterface):
    """Filter out any poffins with total number of flavors  > the passed in value.

    Args:
        Level (int): The maximum amount of flavors

    Notes:\n
            * 0 - 4 flavors

    Returns:
        list[Poffin]: List of poffins with flavors <= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert 0 <= self._value < 5
        return [p for p in poffins if p.num_flavors <= self._value]


class FilterPoffinsBy_Name(IPoffinFilterInterface):
    """Filter out any poffins that do not have the same name as the passed in value.

    Args:
        name (str): The name of the poffins to keep.

    Notes:\n
            * "mild poffin"\n
            * "rich poffin"\n
            * "overripe poffin"\n
            * "super mild poffin"\n
            * "foul poffin" - Typically arent generated.\n

    Returns:
        list[Poffin]: Lisf of poffins with the same name as the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert self._value in ["foul poffin", "mild poffin", "rich poffin", "overripe poffin", "super mild poffin"]
        return super().execute(poffins)


class FilterPoffinsBy_Rarity_LessThan(IPoffinFilterInterface):
    """Filter out any berries with a rarity less than the given value

    Notes:\n
            * min = 7\n
            * max = 60\n

        THIS WILL NOT LEAVE MANY BERRIES!\n

    Returns:
        list[Berry]: berries with rarity >= value
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert 6 < self._value <= 60
        return [p for p in poffins if p.rarity >= self._value]


class FilterPoffinsBy_Rarity_GreaterThan(IPoffinFilterInterface):
    """Filter out any berries with a rarity greater than the given value

    Notes:\n
            * min = 4\n
            * max = 45\n

        THIS WILL NOT LEAVE MANY BERRIES!\n

    Returns:
        list[Berry]: berries with rarity <= value
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert 4 <= self._value < 46
        return [p for p in poffins if p.rarity <= self._value]


class FilterPoffinsBy_AnyFlavorValueLessThan(IPoffinFilterInterface):
    """Filter out any poffins with any flavor value  < the passed in value.

    Args:
        Level (int): The minimum flavor value

    Returns:
        list[Poffin]: List of poffins with all flavor values >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        temp_list = poffins.copy()
        for p in temp_list:
            for i in range(5):
                if 0 < p.flavor_values[i] < self._value:
                    poffins.remove(p)
                    break
        return poffins


class FilterPoffinsBy_MaxNSimilar(IPoffinFilterInterface):
    """Keep uo to x amount of poffins that happen to have the exact same
    values for each flavor.

    Args:
        max_num (int): The max number of poffins similar to one another.

    Returns:
        list[Poffin]: List of poffins with up to x similar flavor valued-poffins.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        dict_similar_poffin_count = {}
        filtered_poffins = []
        for similar_poffin in poffins:
            hahsable_poffin_values = tuple(similar_poffin.flavor_values)
            if hahsable_poffin_values in dict_similar_poffin_count:
                if not dict_similar_poffin_count[hahsable_poffin_values] == self._value:
                    filtered_poffins.append(similar_poffin)
                    dict_similar_poffin_count[hahsable_poffin_values] += 1
            else:
                filtered_poffins.append(similar_poffin)
                dict_similar_poffin_count[hahsable_poffin_values] = 1

        return filtered_poffins


class FilterPoffinsBy__id__(IPoffinFilterInterface):
    """Filter out any poffins whose __id__ does not equal the passed in value.


    Returns:
        list[Poffin]: berries.__id__ == value
    """

    def execute(self, berries: list[Poffin]) -> list[Poffin]:
        return [b for b in berries if b.__id__ == self._value]
