import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # 正则表达式设计原理：
    # 1. 使用 ^ 和 $ 限定整个字符串匹配。
    # 2. (\d{1,2}) 匹配1到2位数字，表示小时。
    # 3. (?::(\d{2}))? 使用非捕获式问号表示冒号及后面的两位数字（分钟）为可选部分。
    # 4. (AM|PM) 匹配大写的 AM 或 PM。
    # 5. 两个时间之间用 " to " 分隔，因此整体模式匹配两个时间。
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    # 分组：1-小时1, 2-分钟1, 3-上午/下午1, 4-小时2, 5-分钟2, 6-上午/下午2
    hour1, minute1, period1, hour2, minute2, period2 = match.groups()
    # 如果分钟部分缺失，则默认设置为 "00"
    minute1 = minute1 if minute1 is not None else "00"
    minute2 = minute2 if minute2 is not None else "00"

    # 转换为整数，进行合法性检查
    hour1_int = int(hour1)
    hour2_int = int(hour2)
    minute1_int = int(minute1)
    minute2_int = int(minute2)

    if not (1 <= hour1_int <= 12) or not (1 <= hour2_int <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= minute1_int < 60) or not (0 <= minute2_int < 60):
        raise ValueError("Invalid minutes")

    def convert_time(hour, minute, period):
        hour = int(hour)
        minute = int(minute)
        if period == "AM":
            if hour == 12:
                hour = 0
        elif period == "PM":
            if hour != 12:
                hour += 12
        return f"{hour:02d}:{minute:02d}"

    time1 = convert_time(hour1, minute1, period1)
    time2 = convert_time(hour2, minute2, period2)

    return f"{time1} to {time2}"

if __name__ == "__main__":
    main()
