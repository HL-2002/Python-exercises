from um import count

def test_substring():
    assert count("yummy") == 0
    assert count("yummy yum") == 0

def test_ums():
    assert count("regular, um, expressions") == 1
    assert count("hello, um, world") == 1
    assert count("um...") == 1

def test_many_um():
    assert count("should we, um, have more yummy treats?") == 1