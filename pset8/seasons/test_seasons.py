from seasons import check_birthday


def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday('1990-08-28') == ("1990", "08", "28")
    assert check_birthday('1990-8-28') == None
    assert check_birthday("augost 28 1990") == None


if __name__ == "__main__":
    main()
