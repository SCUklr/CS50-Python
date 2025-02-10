def main():
    """主函数读取用户输入时间，返回结果"""

    user_time = input("请输入您现在的时间： ")
    
    result = convert(user_time)

    if result >= 7 and result <= 8:
        print("breakfast time")

    elif result >= 12 and result <= 13:
        print("lunch time")

    elif result >= 18 and result <= 19:
        print("dinner time")


def convert(time):
    """对用户输入进行处理,转换为小时"""

    hours, minutes = time.split(":")
    # 永远要记得把str->int
    hours = int(hours)
    minutes = int(minutes)
    # 转化为小时
    time_in_hours = float(hours + minutes / 60)
    # 例如，给定一个time（"7:30"即 7 小时 30 分钟），convert应该返回7.5（即 7.5 小时）。
    return time_in_hours

if __name__ == "__main__":
    main()
