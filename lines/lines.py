import sys

"""
在名为 lines.py 的文件中，实现一个程序，该程序只需要一个命令行参数、一个 Python 文件的名称（或路径），
并输出该文件中的代码行数（不包括注释和空行）。
如果用户没有指定一个命令行参数，或者指定的文件的名称不是以 .py 结尾，或者指定的文件不存在，则程序应通过 sys.exit 退出。
假设任何以 # 开头的行（前面可以加空格）都是注释。（不应将文档字符串视为注释。）假设任何仅包含空格的行都是空白。
"""

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# 获取文件名
filename = sys.argv[1]

# 确保文件名以 .py 结尾
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    sys.exit("File does not exist")

# 统计有效行数
count = 0
for line in lines:
    stripped_line = line.lstrip()

    if not stripped_line or stripped_line.startswith("#"):
        continue # 用continue，遇到不符合要求的行直接回到循环开头，不计数

    count += 1

print(count)
