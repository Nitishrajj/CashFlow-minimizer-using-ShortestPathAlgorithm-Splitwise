import math

def find_path(details):
    print_bill = []
    max_value = max(details.values())
    min_value = min(details.values())

    if max_value != min_value:
        max_key = get_key_from_value(details, max_value)
        min_key = get_key_from_value(details, min_value)
        result = max_value + min_value
        result = round(result, 1)

        if result >= 0.0:
            print(f"{min_key} needs to pay {max_key}: {abs(min_value):.2f}")
            del details[max_key]
            del details[min_key]
            details[max_key] = result
            details[min_key] = 0.0
        else:
            print(f"{min_key} needs to pay {max_key}: {abs(max_value):.2f}")
            del details[max_key]
            del details[min_key]
            details[max_key] = 0.0
            details[min_key] = result

        find_path(details)

def get_key_from_value(hm, value):
    for key, val in hm.items():
        if val == value:
            return key
    return None

if __name__ == "__main__":
    details = {
        "A": -5.0,
        "B": 25.0,
        "C": -20.0,
        "D": 25.0,
        "E": -20.0,
        "F": -5.0
    }

    find_path(details)