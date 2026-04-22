#!/env/bin/python3

import sys


class InvalidParameter(Exception):
    def __init__(self, error: str = "Unknown error") -> None:
        super().__init__(error)


def get_inventory(parameter: list[str]) -> dict[str, int]:
    """
        parse the parameter to get the key value dictionary
    """
    length = len(parameter)
    inventory: dict[str, int] = {}
    redundant = set()
    key_ = set()
    if (length != 1):
        for i in range(1, length):
            try:
                item = parameter[i].split(':')
                if (len(item) != 2):
                    raise InvalidParameter(
                                    f"Error - Invalid parameter"
                                    f"'{','.join(item)}'"
                                    )
                if not item[1].isdigit():
                    raise ValueError(
                                    f"Quantity error for 'key':"
                                    f"invalid literal for int() "
                                    f"with base 10: '{item[1]}'"
                                    )
                if item[0] not in key_:
                    inventory.update({
                        item[0]: int(item[1])
                    })
                    key_.add(item[0])
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
    if (inventory):
        for key, value in inventory.items():
            print(
                f"Item {key} represents: "
                f"{get_percentage(total_values, value)}%"
                )
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
        print(
            f"Item most abundant: {temp_max[0]}"
            f"with quantity {temp_max[1]}"
            )
        print(
            f"Item least abundant: {temp_min[0]}"
            f"with quantity {temp_min[1]}"
            )
    else:
        try:
            raise InvalidParameter(
                            "Inventory is empty"
                            " (no parameter provided)"
                            )
        except Exception as e:
            print(f"Error : {e}")
    inventory.update(
        {
            'magic_item': 1
        }
    )
    return inventory


def get_percentage(total: int, item_value: int) -> float:
    return (round(((item_value / total) * 100), 1))


if __name__ == "__main__":
    inventory = get_inventory(sys.argv)
    print(f"Updated inventory: {inventory}")
