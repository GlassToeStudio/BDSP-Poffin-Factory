from abc import ABCMeta, abstractmethod

from make_poffins.poffin.poffin import Poffin


class IPoffinFilterInterface(metaclass=ABCMeta):

    def __init__(self, value: int | str):
        self.value = value

    @abstractmethod
    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class FilterPoffinsBy_Level(IPoffinFilterInterface):
    """Filter out any poffins < the passed in value.

    Args:
        Level (int): The minimum level poffin to keep

    Returns:
        list[Poffin]: List of poffins with a level >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.level >= self.value]


class FilterPoffinsBy_Flavor(IPoffinFilterInterface):
    """Filter out any poffins that is not of the given flavor.

    Args:
        Flavor (str): The flavor poffins to keep

    Returns:
        list[Poffin]: List of poffins that are the given flavor
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.main_flavor.lower() == self.value.lower()]


class FilterPoffinsBy_NumberOfFlavors(IPoffinFilterInterface):
    """Filter out any poffins with total number of flavors  < the passed in value.

    Args:
        Level (int): The minimum amount of flavors

    Returns:
        list[Poffin]: List of poffins with flavors >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        return [p for p in poffins if p.num_flavors >= self.value]


class FilterPoffins_ByRarity(IPoffinFilterInterface):
    """Filter out any berries with a rarity less than the given value

    Notes:
        THIS WILL NOT LEAVE MANY BERRIES!

        min = 4\n
        max = 60\n


    Returns:
        list[Berry]: berries with smoothness >= value
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        assert 1 < self.value < 15
        return [p for p in poffins if p.rarity >= self.value]


class FilterPoffinsBy_AnyFlavorValueLessThan(IPoffinFilterInterface):
    """Filter out any poffins any flavor value  < the passed in value.

    Args:
        Level (int): The minimum flavor value

    Returns:
        list[Poffin]: List of poffins with all flavor values >= the passed in value.
    """

    def execute(self, poffins: list[Poffin]) -> list[Poffin]:
        temp_list = poffins.copy()
        for p in temp_list:
            for i in range(5):
                if 0 < p.flavor_values[i] < self.value:
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
                if not dict_similar_poffin_count[hahsable_poffin_values] == self.value:
                    filtered_poffins.append(similar_poffin)
                    dict_similar_poffin_count[hahsable_poffin_values] += 1
            else:
                filtered_poffins.append(similar_poffin)
                dict_similar_poffin_count[hahsable_poffin_values] = 1

        return filtered_poffins
