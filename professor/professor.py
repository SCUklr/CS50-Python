import random
import sys

def main():
    level = get_level()
    score = 0

    # Generate 10 math problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        attempts = 0

        # Allow the user up to 3 tries to get the correct answer
        while attempts < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                # Non-numeric input counts as an incorrect attempt
                print("EEE")
                attempts += 1
                continue

            if guess == correct:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

        # After three unsuccessful attempts, show the correct answer
        if attempts == 3 and guess != correct:
            print(f"{x} + {y} = {correct}")

    print("Score:", score)
    sys.exit(0)

def get_level():
    """Prompt the user for a level until a valid input (1, 2, or 3) is provided."""
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Continue looping until a valid integer is entered

def generate_integer(level):
    """Generate a non-negative integer with the specified number of digits.
       For level 1, return an integer in [0, 9].
       For level 2, return an integer in [10, 99].
       For level 3, return an integer in [100, 999].
    """
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
