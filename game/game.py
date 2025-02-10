import random

def get_positive_int(prompt):
    """反复提示用户输入一个正整数"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            pass

def main():
    """主函数提示用户输入"""
    level = get_positive_int("Level: ")

    answer = random.randint(1, level)

    guess = get_positive_int("Guess: ")


    while 1:
        if guess > answer:
            print("Too Large!")
        elif guess == answer:
            print("Just right!")
            break
        elif guess < answer:
            print("Too small!")

if __name__ == '__main__':
    main()
