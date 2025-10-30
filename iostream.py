from validation import is_float


def get_float_number(prompt: str = "Enter a float number: ") -> float:
    """_summary_

    Args:
        prompt (_type_, optional): _description_. Defaults to "Enter a float number: ".

    Raises:
        TypeError: _description_

    Returns:
        float: _description_
    """
    if not isinstance(prompt, str):
        raise TypeError("The prompt argument type should be 'str'.")

    while True:
        number = input(prompt)
        if is_float(number):
            return float(number)
        else:
            print(f"Error: {number} is invalid.")


if __name__ == "__main__":
    print("test: get_float_number function")
    number = get_float_number()
    print(f"{number}: {type(number)}")
