def main():
    """主函数，负责输入输出"""
    twi_name = input("Input:")
    real_name = convert(twi_name)
    print(f"Output:{real_name}")

def convert(string):
    """转换，去掉元音"""
    new_str = ""
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for char in string:
        if char not in vowels:
            new_str += char
        else:
            char += ""

    return new_str


if __name__ == "__main__":
    main()
