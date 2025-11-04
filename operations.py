from validation import is_operator


def get_operator(operator: str = "Enter an operator: ") -> str:
    operators = {"-", "+", "*", "/", "//", "**","%"}
    if not operator in operators :
        return False
    return True


while True:
    operators = input(operators)
    if is_operator(operators):
        print(operators)
    else:
        print(f"Error: {operators} is invalid.")