import validators

def main():
    # 提示用户输入 email 地址
    email = input("Email: ")
    # validators.email(email) 若有效则返回 email 字符串，否则返回一个 ValidationFailure 对象
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
