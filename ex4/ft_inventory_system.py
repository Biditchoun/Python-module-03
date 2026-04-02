import sys


def check_input(inventory: dict, add_str: str) -> list:
    add_list = add_str.split(":")
    if len(add_list) != 2:
        print(f"Error - invalid parameter '{add_str}'")
        return None
    try:
        add_list[1] = int(add_list[1])
    except ValueError as err:
        print(f"Quantity error for '{add_list[0]}': {err}")
        return None
    if add_list[0] in inventory:
        print(f"Redundant item '{add_list[0]}' - discarding")
        return None
    if add_list[1] < 0:
        print(f"Quantity error for '{add_list[0]}': negative value ({add_list[1]}) - discarding")
        return None
    return add_list


def inventory_system(av: list) -> None:
    inventory = {}
    ac = len(av)
    if (ac < 2):
        return
    i = 1
    while i < ac:
        item = check_input(inventory, av[i])
        if item:
            inventory.update({item[0]: item[1]})
        i += 1
    print(f"Got inventory : {inventory}")
    print(f"Item list: {inventory.keys()}")
    print(f"Total quantity of the {len(inventory)} items: {sum(inventory.values())}")
    i = 0
    max_item = ""
    min_item = ""
    for item in inventory:
        print(f"Item {item} represents {round(100 * inventory.get(item) / sum(inventory.values()), 1)}%")
        if (max_item == "" or inventory.get(max_item) < inventory.get(item)):
            max_item = item
        if (min_item == "" or inventory.get(min_item) > inventory.get(item)):
            min_item = item
    print(f"Item most abundant: {max_item} with quantity {inventory.get(max_item)}")
    print(f"Item least abundant: {min_item} with quantity {inventory.get(min_item)}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    inventory_system(sys.argv)
