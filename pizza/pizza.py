import sys
import csv
from tabulate import tabulate

"""
在名为 pizza.py 的文件中，实现一个程序，该程序只需要一个命令行参数、一个 CSV 文件的名称（或路径），
并输出格式化的 ASCII 表格（grid 格式）。
如果用户没有指定一个命令行参数，或者指定的文件的名称不是以 .csv 结尾，或者指定的文件不存在，则程序应通过 sys.exit 退出。
"""

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

# 首先确认扩展名是.csv
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

# 打开CSV
try:
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        table = [row for row in reader]  # 读取所有行到列表

except FileNotFoundError:
    sys.exit("File does not exist")


# 使用 tabulate 进行表格格式化
print(tabulate(table, headers="firstrow", tablefmt="grid"))
