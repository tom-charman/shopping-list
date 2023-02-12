import logging

from core import ShoppingList, UnknownItemError, init, update_shopping_list

logger = logging.getLogger(__name__)


items, larder, recipes = init()
shopping_list = ShoppingList()
while True:
    thing = str(input("Name of ingredient:"))
    quantity = str(input("Quantity:"))
    if thing == "stop":
        shopping_list.pretty_print()
    try:
        shopping_list = update_shopping_list(
            shopping_list, thing, quantity, items, larder, recipes
        )
    except UnknownItemError:
        logger.warning(f"{thing} is not known.")
