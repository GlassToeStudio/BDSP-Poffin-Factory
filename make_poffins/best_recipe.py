import math

from make_poffins.berry import Berry
from make_poffins.poffin import Poffin


class BestRecipe:
    def __init__(self, flavor: str, level: int, poffin: Poffin, recipe: tuple[Berry]):
        self.flavor = flavor
        """Spicy, Dry, Sweet, Bitter, Sour"""
        self.level = level
        """The highest flavor value for the poffin"""
        self.poffin = poffin
        """The poffin made from the given recipe"""
        self.recipe = recipe
        """The recipe to make the poffin"""
        self.num_can_eat = math.ceil(255.0 / self.level)
        """Poffins required to max at least one stat"""
        self.total_values = [x * self.num_can_eat for x in self.poffin.flavor_values]
        """Values after eating num_can_eat poffins"""
        self.sheen = self.poffin.smoothness * self.num_can_eat
        """Sheen after eating num_can_eat poffins"""

    def __repr__(self):
        r = "\n\t".join(str(self.recipe).replace(",", "-").replace("(", "").replace(")", "").strip().split("$"))
        return f"\n{self.flavor}: {self.level} * {self.num_can_eat=} ({self.sheen=}," f"{self.total_values}) - {self.poffin.smoothness=} - {self.poffin.flavor_names}" f"\n\t- {r}"


class RecipeCombo:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
