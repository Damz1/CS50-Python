from numb3rs import validate


def test_true_validate():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('192.168.0.1') == True
    assert validate('0.0.0.0') == True
    assert validate('10.0.0.0') == True


def test_false_validations():
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
