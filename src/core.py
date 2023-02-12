import json


class UnknownItemError(Exception):
    pass


class Item:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def __repr__(self):
        return f"{self.name}"


class Ingredient:
    def __init__(self, name: str, quantity: str):
        self.name = name
        self.quantity = quantity

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def __repr__(self):
        return f"{self.name}, {self.quantity}"


class Larder:
    def __init__(self, ingredients):
        self.ingredients = {
            ingredient.name: ingredient.quantity for ingredient in ingredients
        }

    @property
    def ingredient_names(self):
        return [ingredient.name for ingredient in self.ingredients]

    @classmethod
    def from_json(cls, json_data):
        return cls(Ingredient.from_json(ingredient) for ingredient in json_data)

    def __contains__(self, item):
        if item in self.ingredient_names:
            return True
        return False

    def add(self, item, quantity):
        self.ingredients[item] = quantity

    def pretty_print(self):
        for name, quantity in self.ingredients.items():
            print(f"{name}, {quantity}")


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @property
    def ingredient_names(self):
        return [ingredient.name for ingredient in self.ingredients]

    @classmethod
    def from_json(cls, json_data):
        return cls(**json_data)

    def __contains__(self, item):
        if item in self.ingredient_names:
            return True
        return False

    def __repr__(self):
        return f"Recipe: {self.name}"


class ShoppingList(Larder):
    def __init__(self):
        super().__init__(ingredients=[])


def load_items():
    with open("data/items.json") as fp:
        return [Item.from_json(item) for item in json.loads(fp.read())]


def load_recipes():
    with open("data/recipes.json") as fp:
        return [Recipe.from_json(item) for item in json.loads(fp.read())]


def load_larder():
    with open("data/larder.json") as fp:
        return Larder.from_json(json.loads(fp.read()))


def init():
    """
    Loads items data, larder status, and recipes.
    """
    items = load_items()
    recipes = load_recipes()
    larder = load_larder()
    return items, larder, recipes


def update_shopping_list(shopping_list, item, quantity, known_items, larder, recipes):
    new_shopping_list = ShoppingList()
    if item in [recipe.name for recipe in recipes]:
        for ingredient in [recipe for recipe in recipes if recipe.name == item][
            0
        ].ingredients:
            new_shopping_list.add(ingredient["name"], ingredient["quantity"])

    elif item in [item.name for item in known_items]:
        new_shopping_list.add(
            [known_item.name for known_item in known_items if known_item.name == item][
                0
            ],
            quantity,
        )
    else:
        raise UnknownItemError

    return new_shopping_list
