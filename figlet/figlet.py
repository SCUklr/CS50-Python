import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    args = sys.argv[1:]

    # 当没有命令行参数时，随机选择一个字体
    if len(args) == 0:
        fonts = figlet.getFonts()
        chosen_font = random.choice(fonts)
        figlet.setFont(font=chosen_font)
    # 当命令行参数为两个且第一个为 -f 或 --font 时，使用用户指定的字体
    elif len(args) == 2 and args[0] in ['-f', '--font']:
        font = args[1]
        # 可选：检查该字体是否存在
        if font not in figlet.getFonts():
            sys.exit("错误：字体 '{}' 不存在。".format(font))
        figlet.setFont(font=font)
    else:
        sys.exit("用法：python figlet.py [-f|--font FONT]")

    # 提示用户输入文本
    user_text = input("请输入要转换的文本：")
    # 使用 FIGlet 渲染文本并输出结果
    output_text = figlet.renderText(user_text)
    print(output_text)

if __name__ == '__main__':
    main()
