from iostream import get_float_number
from operations import get_operator


def get_operator() -> str:
    """Define the operators and validation it, also the output is string type.

    Returns:
        str: output is one of the operators that you choices it.
    """
    operators = {"-", "+", "*", "/", "//", "**","%"}
    user_operator= input("Enter your operator: ")
    if not user_operator in operators :
        return False
    return user_operator


def get_float_number(prompt: str) -> float:
    """get float number from users

    Args:
        prompt (str): the output is float type.

    Raises:
        ValueError: if the type of number is not float, we have a ValueError in output.

    Returns:
        float: get float number from user_input.
    """
    user_input = input(prompt)
    try:
        return float(user_input)
    except:
        raise ValueError("Invalid operator!")



def addition(a,b) -> float: 
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: addition of two numbers
    """
    return a + b

def subtraction(a,b)-> float:
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: subtraction of two numbers
    """
    return a - b


def multiplication(a,b)-> float:
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: multiplication of two numbers
    """
    return a * b


def division(a,b)-> float:
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: division of two numbers
    """
    return a / b


def division_floor(a,b)-> float:
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: division_floor of two numbers
    """
    return a // b


def modulus(a,b)-> float:
    """get two float numbers

    Args:
        a (flaot): output is float number
        b (float): output is float number

    Returns:
        float: modulus of two numbers
    """
    return a % b


def power(a,b)-> float:
    """get two float numbers

    Args:
        a (float): output is float number
        b (float): output is float number

    Returns:
        float: power of two numbers
    """
    return a ** b






def main():
    """test the operators
    """
    number_1 = get_float_number("Enter your first number: ")
    number_2 = get_float_number("Enter your second number: ")
    user_operator = get_operator()
    user_operators = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division,
        "//": division_floor,
        "%": modulus,
        "**": power,
    }
    result = user_operators[user_operator](number_1, number_2)
    print(result)


if __name__ == "__main__":
    main()