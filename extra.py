

def is_alphabet(char):
    """
    Checks if a given character is an alphabet using comparison operators.

    Args:
      char: The character to check.

    Returns:
      True if the character is an alphabet (a-z or A-Z), False otherwise.
    """
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        return True
    else:
        return False

# Get input from the user
input_char = input("Enter a character: ")

# Check if the input is a single character
if len(input_char) == 1:
    # Check if the character is an alphabet and print the result
    if is_alphabet(input_char):
        print(f"'{input_char}' is an alphabet.")
    else:
        print(f"'{input_char}' is not an alphabet.")
