def is_float(number: str) -> bool:
    """_summary_

    Args:
        number (str): _description_

    Returns:
        bool: _description_
    """
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
    """validation of is_operator function

    Args:
        operator (str): operator is string type

    Returns:
        bool: output of validation is True or False
    """
    operators = {"-", "+", "*", "/", "//", "**","%"}
    if not operator in operators :
        return False
    return True


if __name__ == "__main__":
    print("test of is_operator: ")
    print(f"True mode (operator = *): {is_operator("*")}")
    print(f"False mode (operator = 1@): {is_operator("1@")}")