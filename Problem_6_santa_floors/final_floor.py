def move_floor(char: str) -> int:
    """
    Returns +1 if '(' else -1 if ')'.
    """
    if char == '(':
        return 1
    elif char == ')':
        return -1
    else:
        print ("ValueErrorInvalid character: only '(' and ')' are allowed.")


def final_floor(instructions: str) -> int:
    """
    Calculates the final floor Santa ends on.
    """
    floor = 0
    for ch in instructions:
        floor += move_floor(ch)
    return floor

# --- Main Program ---
floor=""
if __name__ == "__main__":
    instructions = str(input("Enter Santa's instructions (e.g. (()()) ): ")).strip()
    floor = final_floor(instructions)
    print("Santa ends up on floor:", floor)