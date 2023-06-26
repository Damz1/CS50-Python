from bank import value


def test_hello():
    assert value('hello') == 0


def test_hi():
    assert value('hi') == 20


def test_whatsapp():
    assert value('whatsapp') == 100


def test_all_cases():
    assert value('Hello') == 0
    assert value('Hi') == 20
    assert value('Whatsapp') == 100
