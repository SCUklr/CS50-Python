import emoji
def main():
    """主函数"""
    user_input = input("请输入包含表情符号代码的字符串：")
    convert(user_input)

def convert(string):
    """转换"""
    converted = emoji.emojize(string, language='alias')
    print(converted)

main()
