from copy import deepcopy

from make_poffins.poffin import Poffin


class PoffinSorter():
    """A class with functionality to sort poffins on various attributes"""
    @staticmethod
    def sort_on_main_flavor_value(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their main flavor value.

        If value == True, list is in descending order (higher is better)

        If value == False, list is in ascending order (lower is berrer)

        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.level, reverse=value)

    @staticmethod
    def sort_on_smoothness(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)

        If value == False, list is in ascending order (lower is berrer)

        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.smoothness, reverse=value)

    @staticmethod
    def sort_on_sum_of_main_flavor_smoothness_ratios(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)
        If value == False, list is in ascending order (lower is berrer)


        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: (x.level / x.smoothness)+(x.second_level / x.smoothness), reverse=value)  # noqa ES501

    @staticmethod
    def sort_on_main_flavor_smoothness_ratio(poffins: list[Poffin], value: bool = True) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins sorted by their smoothness.

        If value == True, list is in descending order (higher is better)
        If value == False, list is in ascending order (lower is berrer)


        Keyword Args:
            value = True
        """

        return sorted(poffins, key=lambda x: x.level / x.smoothness, reverse=value)  # noqa ES501

    @staticmethod
    def filter_poffins_by_flavor(poffins: list[Poffin], flavor: str) -> list[Poffin]:  # noqa ES501
        """Return the list of only <flavor> poffins."""

        return [p for p in poffins if p.main_flavor.lower() == flavor.lower()]  # noqa ES501

    @staticmethod
    def filter_poffins_by_level(poffins: list[Poffin], level: int) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins with a level >= level"""

        return [p for p in poffins if p.level >= level]  # noqa ES501

    @staticmethod
    def filter_by_num_flavors(poffins: list[Poffin], num_favors: int) -> list[Poffin]:  # noqa ES501
        """Return the list of poffins with a number of flavors  >= num_favors"""  # noqa ES501

        return [p for p in poffins if p.__num_flavors__() >= num_favors]  # noqa ES501

    @staticmethod
    def filter_if_any_value_less_than(poffins: list[Poffin], min_flavor_value: int = 25) -> list[Poffin]:  # noqa ES501
        """Remove any poffin from the list if one of their non-zero flavor values is < min_flavor_value"""  # noqa ES501

        temp_list = deepcopy(poffins)
        for p in temp_list:
            for i in range(5):
                if 0 < p.flavor_values[i] < min_flavor_value:
                    poffins.remove(p)
                    break
        return poffins  # noqa ES501

    @staticmethod
    def filter_similar_poffins_to_four(poffins: list[Poffin]) -> list[Poffin]:
        spicy_value_dict = {}
        looping_list = deepcopy(poffins)
        for sp in looping_list:
            t = tuple(sp.flavor_values)
            if t in spicy_value_dict:
                if spicy_value_dict[t] == 4:
                    poffins.remove(sp)
                    continue
                spicy_value_dict[t] += 1
            else:
                spicy_value_dict[t] = 1
        return poffins
