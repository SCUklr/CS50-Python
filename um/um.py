import re
import sys

def main():
    # 不传提示字符串，确保输出中不会包含额外文本
    text = input()
    print(count(text))

def count(s):
    """
    利用正则表达式统计字符串中独立单词 "um" 出现的次数：
      - 模式 r"\bum\b" 中，\b 表示单词边界，
        确保只匹配独立的 "um"，不会匹配 "yummy" 等包含 "um" 的单词；
      - flags=re.IGNORECASE 使匹配不区分大小写。
    """
    matches = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
