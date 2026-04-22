#!/env/bin/python3

import sys

class InvalidParameter(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def get_inventory(parameter: list[str]) -> dict:
    """
        parse the parameter to get the key value dictionary
    """
    length = len(parameter)
    inventory = {}
    redundant = set()
    key = set()
    if (length != 1):
        for i in range(1, length):
            try:
                item = parameter[i].split(':')
                if (len(item) != 2):
                    raise InvalidParameter(f"Error - Invalid parameter '{','.join(item)}'")
                if not item[1].isdigit():
                    raise ValueError(f"Quantity error for 'key':" 
                                    f"invalid literal for int() with base 10: '{item[1]}'"
                                    )
                if item[0] not in key:
                    inventory.update({
                        item[0]: int(item[1])
                    })
                    key.add(item[0])
                else:
                    redundant.add(item[0])
                if (redundant):
                    for re in redundant:
                        raise InvalidParameter(f"Redundant {re} - discarding")
            except Exception as e:
                print(f"{e}")
    print(f"Got inventory: {inventory}")
    keys = list(inventory.keys())
    print(f"Item list: {keys}")
    total_values = sum(list(inventory.values()))
    print(f"Total quantity of the {len(keys)} items: {total_values}")
    
    for key, value in inventory.items():
        print(f"Item {key} represents: {get_percentage(total_values, value)}%")
    temp_min = ["", str(min(inventory.values()))]
    temp_max = ["", str(max(inventory.values()))]
    for key, value in inventory.items():
        if (value == int(temp_max[1])):
            temp_max[0] = key
            break
    for key, value in inventory.items():
        if (value == int(temp_min[1])):
            temp_min[0] = key
            break
    print(f"Item most abundant: {temp_max[0]} with quantity {temp_max[1]}")
    print(f"Item least abundant: {temp_min[0]} with quantity {temp_min[1]}")
    inventory.update(
        {
            'magic_item': 1
        }
    )
    return inventory

def get_percentage(total:int, item_value: int) -> float:
    return (round(((item_value / total) * 100), 1))

if __name__ == "__main__":
    inventory = get_inventory(sys.argv)
    print(inventory)

