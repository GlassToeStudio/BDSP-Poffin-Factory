import math

from make_poffins.berry import berry_factory
from make_poffins.poffin.poffin import Poffin
from make_poffins.poffin.poffin_cooker import PoffinCooker


class RecipeRecord:
    def __init__(self, poffin: Poffin):
        pass
    #     self.flavor = poffin.main_flavor
    #     """Spicy, Dry, Sweet, Bitter, Sour"""
    #     self.level = poffin.level
    #     """The highest flavor value for the poffin"""
    #     self.poffin = poffin
    #     """The poffin made from the given recipe"""
    #     self.recipe = poffin.berries
    #     """The recipe to make the poffin"""
    #     self.num_can_eat = math.ceil(255.0 / self.level)
    #     """Poffins required to max at least one stat"""
    #     self.total_values = [min(x * self.num_can_eat, 255) for x in self.poffin.flavor_values]  # noqa ES501
    #     """Values after eating num_can_eat poffins"""
    #     self.sheen = min(self.poffin.smoothness * self.num_can_eat, 255)
    #     """Sheen after eating num_can_eat poffins"""

    # def __repr__(self):
    #     r = "\n".join(map(repr, self.recipe))
    #     return (f"\n{self.level} {self.flavor} {self.poffin.smoothness} - {self.poffin.flavor_names}\n"  # noqa ES501
    #             f"Can eat: {self.num_can_eat} for {self.sheen} sheen => {self.total_values}\n"  # noqa ES501
    #             f"{r}\n")

    # def __str__(self):
    #     r = "\n".join(map(str, self.recipe))
    #     return (f"\n{self.level} {self.flavor} {self.poffin.smoothness} - {self.poffin.flavor_names}\n"  # noqa ES501
    #             f"Can eat: {self.num_can_eat} for {self.sheen} sheen => {self.total_values}\n"  # noqa ES501
    #             f"{r}")


def main():
    recipe = berry_factory.single_recipe
    cooker = PoffinCooker()
    p = cooker.cook(recipe)
    br = RecipeRecord(p)
    print(repr(br))
    print(br)


if __name__ == "__main__":
    main()
