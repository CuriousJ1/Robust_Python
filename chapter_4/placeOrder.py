from typing import Union
def place_order() -> Optional[HotDog]:
    order = get_order()
    result = dispense_snack(order.name)

    if result is None
        print_error_code("An error occurred" + result)
        return None
#    Return our HotDog 
    return result