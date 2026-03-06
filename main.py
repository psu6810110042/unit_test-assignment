import sys
from _6810110042.fizz_buzz import fizz_buzz
from _6810110042.caesar_cipher import caesarCipher
from _6810110042.alternating_characters import alternatingCharacters
from _6810110042.cat_and_mouse import cat_and_mouse
from _6810110042.directory import create_directory, check_directory
from _6810110042.example import is_even_number
from _6810110042.guess_number import guess_int, guess_float


def run_fizzbuzz():
    try:
        n = int(input("Enter a number for FizzBuzz: "))
        print(f"Result: {fizz_buzz(n)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def run_caesar_cipher():
    s = input("Enter string to encrypt: ")
    try:
        k = int(input("Enter shift amount (k): "))
        print(f"Result: {caesarCipher(s, k)}")
    except ValueError:
        print("Invalid shift amount. Please enter an integer.")


def run_alternating_characters():
    s = input("Enter a string of A's and B's: ")
    print(f"Minimum deletions required: {alternatingCharacters(s)}")


def run_cat_and_mouse():
    try:
        x = int(input("Enter position of Cat A: "))
        y = int(input("Enter position of Cat B: "))
        z = int(input("Enter position of Mouse C: "))
        print(f"Result: {cat_and_mouse(x, y, z)}")
    except ValueError:
        print("Invalid input. Please enter integers.")


def run_directory():
    name = input("Enter directory name: ")
    path = create_directory(name)
    exists = check_directory(path)
    print(f"Directory '{path}' -> exists: {exists}")


def run_is_even_number():
    print("Checking if a random number (0-20) is even...")
    result = is_even_number()
    print(f"Result: {result}")


def run_guess_number():
    try:
        start = int(input("Enter start range: "))
        stop = int(input("Enter stop range: "))
        print(f"Random integer: {guess_int(start, stop)}")
        print(f"Random float: {guess_float(start, stop)}")
    except ValueError:
        print("Invalid input. Please enter integers.")


def main():
    print("========================================")
    print("  Testing Repository Main Application   ")
    print("========================================")

    actions = {
        "1": ("Fizz Buzz", run_fizzbuzz),
        "2": ("Caesar Cipher", run_caesar_cipher),
        "3": ("Alternating Characters", run_alternating_characters),
        "4": ("Cat and Mouse", run_cat_and_mouse),
        "5": ("Directory Tools", run_directory),
        "6": ("Random Even Number", run_is_even_number),
        "7": ("Guess Number Range", run_guess_number),
        "q": ("Quit", lambda: sys.exit(0)),
    }

    while True:
        print("\nAvailable Modules:")
        for key, (name, _) in actions.items():
            if key == "q":
                print(f"  [{key}] {name}")
            else:
                print(f"  [{key}] Run {name}")

        choice = input("\nSelect an option: ").strip().lower()

        if choice in actions:
            print("\n" + "-" * 40)
            actions[choice][1]()
            print("-" * 40)
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
