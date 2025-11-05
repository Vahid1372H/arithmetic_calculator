from iostream import get_float_number
from operations import get_operator


def get_operator() -> str:
    operators = {"-", "+", "*", "/", "//", "**","%"}
    user_operator= input("Enter your operator: ")
    if not user_operator in operators :
        return False
    return user_operator


def get_float_number(prompt: str) -> float:
    user_input = input(prompt)
    if user_input is float:
        return float(user_input)
    raise ValueError


def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b


def multiplication(a,b):
    return a * b


def division(a,b):
    return a / b


def division_floor(a,b):
    return a // b


def modulus(a,b):
    return a % b


def power(a,b):
    return a ** b






def main():
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
    result = addition(number_1, number_2, user_operator,user_operators)
    print(result)


if __name__ == "__main__":
    main()