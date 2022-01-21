import math

import make_poffins.berry_factory as bf
from make_poffins.poffin import Poffin


class BestRecipe:
    def __init__(self, poffin: Poffin):
        self.flavor = poffin.main_flavor
        """Spicy, Dry, Sweet, Bitter, Sour"""
        self.level = poffin.level
        """The highest flavor value for the poffin"""
        self.poffin = poffin
        """The poffin made from the given recipe"""
        self.recipe = poffin.berries
        """The recipe to make the poffin"""
        self.num_can_eat = math.ceil(255.0 / self.level)
        """Poffins required to max at least one stat"""
        self.total_values = [x * self.num_can_eat for x in self.poffin.flavor_values]  # noqa ES501
        """Values after eating num_can_eat poffins"""
        self.sheen = self.poffin.smoothness * self.num_can_eat
        """Sheen after eating num_can_eat poffins"""

    def __repr__(self):
        r = "\n".join(map(repr, self.recipe))
        return (f"\n{self.level} {self.flavor} {self.poffin.smoothness} - {self.poffin.flavor_names}\n"  # noqa ES501
                f"Can eat: {self.num_can_eat} for {self.sheen} sheen = {self.total_values}\n"  # noqa ES501
                f"{r}\n")

    def __str__(self):
        r = "\n".join(map(str, self.recipe))
        return (f"\n{self.level} {self.flavor} {self.poffin.smoothness} - {self.poffin.flavor_names}\n"  # noqa ES501
                f"Can eat: {self.num_can_eat} for {self.sheen} sheen = {self.total_values}\n"  # noqa ES501
                f"{r}")


if __name__ == "__main__":
    recipe = [bf.spelon_berry, bf.liechi_berry, bf.petaya_berry, bf.enigma_berry]  # noqa ES501
    p = Poffin([148, 0, 0, 28, 0], 30, recipe)
    br = BestRecipe(p)
    print(repr(br))
    print(br)
