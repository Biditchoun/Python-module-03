import sys


def check_input(inventory: dict, add_str: str) -> list:
    input_list = add_str.split(":")
    if len(input_list) != 2:
        print(f"Error - invalid parameter '{add_str}'")
        return []
    try:
        amount = (int(input_list[1]))
    except ValueError as err:
        print(f"Quantity error for '{input_list[0]}': {err}")
        return []
    if input_list[0] in inventory:
        print(f"Redundant item '{input_list[0]}' - discarding")
        return []
    if amount < 0:
        print(f"Quantity error for '{input_list[0]}': "
              f"negative value ({amount}) - discarding")
        return []
    return [input_list[0], amount]


def create_inventory(av: list) -> dict:
    inventory: dict = {}
    ac = len(av)
    if (ac < 2):
        return inventory
    i = 1
    while i < ac:
        item = check_input(inventory, av[i])
        if item:
            inventory.update({item[0]: item[1]})
        i += 1
    return inventory


def inventory_stats(inventory: dict) -> None:
    if (len(inventory) == 0):
        return
    print(f"Got inventory : {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    all_values = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {all_values}")
    max_item = list(inventory.keys())[0]
    min_item = list(inventory.keys())[0]
    for item in inventory:
        print(f"Item {item} represents "
              f"{round(100 * int(str(inventory.get(item))) / all_values, 1)}%")
        if (int(str(inventory.get(max_item))) < int(str(inventory.get(item)))):
            max_item = item
        if (int(str(inventory.get(min_item))) > int(str(inventory.get(item)))):
            min_item = item
    print(f"Item most abundant: {max_item} "
          f"with quantity {inventory.get(max_item)}")
    print(f"Item least abundant: {min_item} "
          f"with quantity {inventory.get(min_item)}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = create_inventory(sys.argv)
    inventory_stats(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
