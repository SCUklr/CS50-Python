def main():
    """主函数提示用户输入燃油数（分数），输出百分数或F、E"""
    while True:
        try:
            oil_quantity = input("请按照分数形式（num1/num2）输入燃油量: ")
            num1, num2 = map(int, oil_quantity.split("/"))
            result = convert(num1, num2)
            if result is not None:
                print(result)
                break  # 输入有效时退出循环
        except (ValueError, ZeroDivisionError):
            pass  # 继续提示用户输入

def convert(num1, num2):
    if num2 == 0 or num1 > num2:
        return None  # 返回 None 以表示无效输入

    percentage = round((num1 / num2) * 100)
    return "E" if percentage <= 1 else "F" if percentage >= 99 else f"{percentage}%"

if __name__ == "__main__":
    main()
