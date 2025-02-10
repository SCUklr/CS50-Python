def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("请输入文本： ")
    print(convert(user_input))

# 文件底部调用main函数
if __name__ == "__main__":
    main()
