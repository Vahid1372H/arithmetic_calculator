from validation import is_operator


def get_operator(prompt: str = "Enter an operator: ") -> str:
    """_summary_

    Args:
        prompt (_type_, optional): our prompt shoould be string type. Defaults to "Enter an operator: ".

    Raises:
        TypeError: if the usres enter int type or otherwise type, in output we have a TypeError

    Returns:
        str: return is string type
    """
    if not isinstance(prompt, str):
        raise TypeError("The prompt argument type should be 'str'.")

    while True:
        prompt = input(prompt)
        if is_operator(prompt):
            return str(prompt)
        else:
            print(f"Error: {prompt} is invalid.")


if __name__ == "__main__":
    print("test: get_operator function")
    operator = get_operator()
    print(f"{operator}: {type(operator)}")
