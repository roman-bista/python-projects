import random
import string


def generate_password():

    print("\n===== RANDOM PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: ").strip())

    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 4:
        print("Password length must be at least 4.")
        return

    include_uppercase = input(
        "Include uppercase letters? (yes/no): "
    ).strip().lower()

    include_special = input(
        "Include special characters? (yes/no): "
    ).strip().lower()

    include_digits = input(
        "Include digits? (yes/no): "
    ).strip().lower()

    # character sets
    lowercase = string.ascii_lowercase

    uppercase = (
        string.ascii_uppercase
        if include_uppercase == "yes"
        else ""
    )

    special = (
        string.punctuation
        if include_special == "yes"
        else ""
    )

    digits = (
        string.digits
        if include_digits == "yes"
        else ""
    )

    # all possible characters
    all_characters = lowercase + uppercase + special + digits

    # ensure at least one required character
    required_characters = []

    if include_uppercase == "yes":
        required_characters.append(
            random.choice(uppercase)
        )

    if include_special == "yes":
        required_characters.append(
            random.choice(special)
        )

    if include_digits == "yes":
        required_characters.append(
            random.choice(digits)
        )

    remaining_length = length - len(required_characters)

    for _ in range(remaining_length):
        required_characters.append(
            random.choice(all_characters)
        )

    # shuffle password characters
    random.shuffle(required_characters)

    # convert list to string
    password = "".join(required_characters)

    print("\nGenerated Password:")
    print(password)


while True:

    generate_password()

    again = input(
        "\nGenerate another password? (yes/no): "
    ).strip().lower()

    if again != "yes":
        print("\nThanks for using Password Generator!")
        break