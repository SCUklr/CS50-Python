months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("请输入一个日期（例如 9/8/1636 或 September 8, 1636）：")

    if "/" in date_input:
        parts = date_input.split("/")
        # 检查是否有恰好三个部分
        if len(parts) != 3:
            continue
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        except ValueError:
            continue
    else:
        # 处理 Month D, YYYY 格式
        parts = date_input.split(",")
        if len(parts) != 2:
            continue
        f_part = parts[0].strip()  # 删除前后空白
        f_parts = f_part.split()
        if len(f_parts) != 2:
            continue
        month_name = f_parts[0]
        try:
            day = int(f_parts[1])
            year = int(parts[1].strip())
        except ValueError:
            continue
        try:
            # 将月份名称转换为数字
            month = months.index(month_name) + 1
        except ValueError:
            continue

    # 对两种格式统一进行范围验证
    if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 1):
        continue

    print(f"{year:04d}-{month:02d}-{day:02d}")
    break
