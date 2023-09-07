from numb3rs_regex import validate

def test_numeric_values():
    # 0-199
    assert validate("1.2.3.4") == True
    assert validate("05.108.90.12") == True
    assert validate("127.0.0.1") == True
    assert validate("198.0.0.1") == True

    # 200-249
    assert validate("249.201.214.49") == True

    # 250-255
    assert validate("255.255.255.0") == True

def test_alpha_values():
    # Any other string
    assert validate("cat") == False