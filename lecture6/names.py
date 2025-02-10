import csv
import sys
from PIL import Image

# ======== 1. 处理文本文件 (names.txt) ========

# 让用户输入两个名字，并存入 names.txt（追加模式）
names = []
for _ in range(2):
    name = input("What's your name? ")
    names.append(name)

with open("names.txt", "a") as file:
    for name in names:
        file.write(f"{name}\n")

print("\nAll names sorted:")

# 读取 names.txt 并排序输出
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())  # 去除换行符

for name in sorted(names):
    print(f"Hello, {name}")

# ======== 2. 处理 CSV 文件 (students.csv) ========

print("\nProcessing students.csv...")

students = []

# 读取 students.csv，处理 name 和 home 字段
try:
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})
except FileNotFoundError:
    print("students.csv not found, creating a new one.")
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writeheader()

# 按照 name 排序
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# 让用户输入新学生信息，并追加写入
new_name = input("\nEnter a new student's name: ")
new_home = input("Enter their home: ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": new_name, "home": new_home})

print("New student added to students.csv!")

# ======== 3. 处理 GIF 动画 (costumes.gif) ========

print("\nCreating an animated GIF...")

# 让用户提供图片文件路径（可以修改文件名）
image_files = ["costume1.gif", "costume2.gif"]  # 这里假设有两张 gif 图片

images = []
try:
    for img in image_files:
        image = Image.open(img)
        images.append(image)

    images[0].save(
        "costumes.gif", save_all=True, append_images=images[1:], duration=200, loop=0
    )
    print("Animated GIF 'costumes.gif' created successfully!")
except FileNotFoundError:
    print("One or more costume images not found. Please make sure costume1.gif and costume2.gif exist.")

# ======== 代码结束 ========
print("\nAll tasks completed successfully!")
