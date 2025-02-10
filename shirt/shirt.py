import sys
from PIL import Image, ImageOps

"""
在名为 shirt.py 的文件中，实现一个程序，该程序接收两个命令行参数：
1. `sys.argv[1]` - 现有的 JPEG/PNG 图像文件（输入）
2. `sys.argv[2]` - 目标 JPEG/PNG 图像文件（输出）

要求：
- 读取输入图像
- 确保输入和输出文件扩展名相同，并且仅支持 `.jpg`、`.jpeg`、`.png`
- 读取 `shirt.png` 并调整输入图像尺寸，使其适应 `shirt.png`
- 叠加 `shirt.png` 到调整后的输入图像上，并保存到输出文件
- 处理各种错误情况并 `sys.exit()` 提示错误
"""

# 检查命令行参数
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_file, output_file = sys.argv[1], sys.argv[2]

# 扩展名检查一下
valid_extensions = (".jpg", ".jpeg", ".png")
# 下面这个ai帮我写的太复杂了
if not (input_file.lower().endswith(valid_extensions) and output_file.lower().endswith(valid_extensions)):
    sys.exit("Invalid output")

# 确保输入和输出文件的扩展名一致
if input_file.split(".")[-1].lower() != output_file.split(".")[-1].lower():
    sys.exit("Input and output have different extensions")

# 处理文件不存在的情况
try:
    image = Image.open(input_file)
except FileNotFoundError:
    sys.exit("Input does not exist")

# 读取 `shirt.png`
shirt = Image.open("shirt.png")

# 调整输入图片的大小，使其匹配 `shirt.png`
resized_image = ImageOps.fit(image, shirt.size)

# 叠加 `shirt.png` 到调整后的输入图像
resized_image.paste(shirt, mask=shirt)

# 保存输出文件
resized_image.save(output_file)
