import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 1️⃣ 车牌长度必须在 2 到 6 之间
    if not (2 <= len(s) <= 6):
        return False

    # 2️⃣ 车牌必须以两个字母开头
    if not s[:2].isalpha():
        return False

    # 3️⃣ 确保车牌只包含字母和数字
    if not s.isalnum():
        return False

    # 4️⃣ 找到第一个数字的索引（如果有）
    first_digit_index = next((i for i, c in enumerate(s) if c.isdigit()), None)

    if first_digit_index is not None:  # 说明有数字
        # 确保数字部分只能出现在结尾
        if not s[first_digit_index:].isdigit():
            return False
        # 第一个数字不能是 0
        if s[first_digit_index] == '0':
            return False

    return True  # 所有条件满足，返回 True

main()
