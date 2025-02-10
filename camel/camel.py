def main():
    """主函数"""
    camel_case = input("请输入变量名： ")
    snake_case = convert(camel_case)
    print(snake_case)
def convert(camel):
    """转换"""
    snake = ""
    for char in camel:
        if char.isupper():
            snake = snake + "_" + char.lower()
        else:
            snake = snake + char
    return snake

if __name__ == "__main__":
    main()
