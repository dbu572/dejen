def move_floor(char: str) -> int:
    """
    Returns +1 if '(' else -1 if ')'.
    Raises ValueError if any other character is found.
    """
    if char == '(':
        return 1
    elif char == ')':
        return -1
    else:
        print("ValueErrorInvalid character: only '(' and ')' are allowed.")


def first_basement_position(instructions: str) -> int:
    """
    Returns the 1-based position where Santa first enters the basement (floor -1).
    Returns -1 if Santa never enters the basement.
    """
    floor = 0
    for i in instructions:
        floor += move_floor(i)
        if floor == -1:
            return floor  # First time reaching the basement
    


# --- Main Program ---
position=0
if __name__ == "__main__":
    instructions = input("Enter Santa's instructions (only '(' and ')'): ").strip()
    #strip meances remove white spaces from start and end of string
    position = first_basement_position(instructions)
    if position == -1:
        print("Santa never enters the basement.")
    else:
        print("Santa enters the basement at position:", position)

