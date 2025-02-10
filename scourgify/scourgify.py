import sys
import csv

"""
在名为 scourgify.py 的文件中，实现一个程序，该程序接收两个命令行参数：
1. 现有的 CSV 文件（输入）
2. 新的 CSV 文件（输出）

要求：
- 读取输入 CSV 文件，其列顺序为 name, house。
- 解析 `name`，将 "姓, 名" 拆分为 `first` 和 `last`，然后写入输出文件，列顺序变为 first, last, house。
- 如果参数个数错误或文件无法读取，使用 `sys.exit()` 退出并提示错误信息。
"""

# 检查命令行参数个数,把第二个和第三个参数匹配一下
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

# 读取csv

try:
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # 读取 CSV 并解析为字典
        students = []

        for row in reader:
            last, first = row["name"].split(", ")  # 拆分姓名
            students.append({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

# 写入新的 CSV 文件
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    writer.writerows(students)
