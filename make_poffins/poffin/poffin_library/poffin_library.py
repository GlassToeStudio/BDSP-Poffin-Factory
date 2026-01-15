import json
import random
import os
from make_poffins.berry import berry_library
from make_poffins.constants import FLAVORS
from make_poffins.poffin.poffin import Poffin


def _load_all_poffins_from_json(json_filename="poffin_recipes.json") -> dict:
    """
    Loads all poffin recipes from a JSON file and constructs Poffin objects.

    Returns:
        A dictionary where keys are flavor names (e.g., "spicy") and
        values are lists of Poffin objects.
    """
    # Build a lookup map of berry names to their actual Berry objects.
    # This is crucial for creating the Poffin objects correctly.
    berry_map = {berry.name: berry for berry in berry_library.every_berry}

    # Construct the full path to the JSON file relative to this script.
    # This makes the script runnable from anywhere.
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, json_filename)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            all_recipes = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find the JSON file at {json_path}")
        return {}

    poffin_lists_by_flavor = {}
    for flavor, recipes in all_recipes.items():
        poffin_list = []
        for recipe in recipes:
            try:
                # Find the berry objects corresponding to the names in the JSON.
                berry_objects = [berry_map[name] for name in recipe['berries']]

                # Create the Poffin object using data from the JSON.
                p = Poffin(
                    flavor_values=recipe['flavor_values'],
                    smoothness=recipe['smoothness'],
                    berries=berry_objects
                )
                poffin_list.append(p)
            except KeyError as e:
                print(
                    f"Warning: Could not find berry '{e}' for recipe '{recipe.get('name', 'N/A')}'. Skipping recipe.")

        poffin_lists_by_flavor[flavor] = poffin_list

    return poffin_lists_by_flavor

# --- Main library data, now loaded dynamically ---


# Load all poffin data when the module is imported.
poffin_list_dict = _load_all_poffins_from_json()

# Recreate the module-level variables to maintain compatibility with other scripts.
spicy_poffin_list = poffin_list_dict.get('spicy', [])
dry_poffin_list = poffin_list_dict.get('dry', [])
sweet_poffin_list = poffin_list_dict.get('sweet', [])
bitter_poffin_list = poffin_list_dict.get('bitter', [])
sour_poffin_list = poffin_list_dict.get('sour', [])

# Combine all lists into a single 'poffin_list' for general use.
poffin_list = [p for poffins in poffin_list_dict.values() for p in poffins]

# --- Functions that use the loaded data ---


def get_random_poffin(flavor: str):
    """Returns a random poffin of a specific flavor."""
    l = poffin_list_dict.get(flavor.lower(), [])
    if not l:
        return None
    return random.choice(l)


def generate_random_poffin_list_n_of_each(n: int, flavors: list[str]) -> list[Poffin]:
    """Return a list of n poffins of each given flavor."""
    return_list = []
    for _ in range(n):
        for f in flavors:
            poffin = get_random_poffin(f)
            if poffin:
                return_list.append(poffin)
    return return_list


def generate_random_poffin_list_n_total_of_random(n: int) -> list[Poffin]:
    """Return a list of size n containing random flavored poffins."""
    return_list = []
    available_flavors = [f for f in FLAVORS if poffin_list_dict.get(f.lower())]
    if not available_flavors:
        return []

    for _ in range(n):
        random_flavor = random.choice(available_flavors)
        poffin = get_random_poffin(random_flavor)
        if poffin:
            return_list.append(poffin)
    return return_list
