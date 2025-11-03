from validation import is_float


def get_float_number(prompt: str = "Enter a float number: ") -> float:
    """get flost number from users

    Args:
        prompt (float, user): checking that is number float or no? . Defaults to "Enter a float number: ".

    Raises:
        TypeError: The type of number that we want should be str.

    Returns:
        float: return float number and type of number that means str.
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
