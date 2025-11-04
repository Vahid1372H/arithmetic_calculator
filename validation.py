def is_float(number: str) -> bool:
    try:
        float(number)
        return True
    except:
        return False


if __name__ == "__main__":
    print("test of is_float: ")
    print(f"True mode (number = 12.5): {is_float("12.5")}")
    print(f"False mode (number = 12q5): {is_float("12q5")}")


def is_operator(operator: str) -> bool:
    if not operator.isnumeric() or operator.isalpha():
        return True
    return False


if __name__ == "__main__":
    print("test of is_operator: ")
    print(f"True mode (operator = *): {is_operator("*")}")
    print(f"False mode (operator = 1@): {is_operator("1")}")