from make_poffins.berry.berry import Berry
from make_poffins.berry.berry_factory import every_berry


class BerrySorter():
    def __init__(self, berries: list[Berry]):
        self.berries = berries
        self.berries_lists_sorted = []
        self.berries_sorted = []

        self.berry_dict = {
            "Spicy": [],
            "Dry": [],
            "Sweet": [],
            "Bitter": [],
            "Sour": []
        }

    def __sort__(self, berries: list[Berry], value: bool = True) -> list[Berry]:  # noqa ES501
        return sorted(berries, key=lambda x: (x.main_flavor_value, -x.smoothness), reverse=value)  # noqa ES501

    def __filter__(self) -> list[Berry]:
        for b in self.berries:
            if b.smoothness >= 0:
                self.berry_dict[b.main_flavor].append(b)

    def __make_list_of_list__(self):
        for _, berry_list in self.berry_dict.items():
            self.berries_lists_sorted.append(berry_list)

    def __make_list__(self):
        for _, berry_list in self.berry_dict.items():
            for berry in berry_list:
                self.berries_sorted.append(berry)

    def sort_all(self, value: bool):
        self.__filter__()

        for flavor, berry_list in self.berry_dict.items():
            self.berry_dict[flavor] = self.__sort__(berry_list, value)
        self.__make_list_of_list__()
        self.__make_list__()

    def print_berries(self):
        for berry_list in self.berries_lists_sorted:
            for berry in berry_list:
                print(berry, berry.main_flavor_value)
            print()
        print()

    def get_sorted_berries_list(self):
        return self.berries_lists_sorted

    def get_sorted_berries(self):
        return self.berries_sorted


if __name__ == "__main__":
    bs = BerrySorter(every_berry)
    bs.sort_all(True)
    bs.print_berries()
