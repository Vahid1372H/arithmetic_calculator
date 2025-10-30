def is_float(number:str) -> bool:
    try:
        float(number)
        return True
    except:
        return False
    

if __name__ == "__main__":
    print("test of is_float: ")
    print(f"True mode (number = 12.5): {is_float("12.5")}")
    print(f"False mode (number = 12q5): {is_float("12q5")}")
