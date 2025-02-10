from twttr import shorten

def test_all():
    """大家一起测！"""
    assert shorten("aaeeiiOOUU") == ""
    assert shorten("twttr") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hell, yeah!") == "Hll, yh!"
    assert shorten("CS50") == "CS50"
    assert shorten("") == ""

