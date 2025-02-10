import pytest
from um import count

def test_single_um():
    # 输入仅包含 "um"，应返回 1
    assert count("um") == 1

def test_multiple_um():
    # 多个 "um"，中间带有逗号或空格
    assert count("um, um, um") == 3

def test_case_insensitive():
    # 测试大小写不敏感；"album" 中的 "um" 不计入
    assert count("Um, thanks for the album.") == 1

def test_ignore_substrings():
    # "um" 作为其他单词的子串不应匹配
    assert count("yummy album dumb scrumptious") == 0

def test_with_punctuation():
    # 带有标点符号的情况
    assert count("um? um! (um)") == 3

def test_complex():
    # 复杂情况：仅匹配独立的 "um"
    text = "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
    # 只有两个独立的 "um" 应被匹配
    assert count(text) == 2
