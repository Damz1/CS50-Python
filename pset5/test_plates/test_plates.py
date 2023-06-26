from plates import is_valid

# Test case for valid vanity plate


def test_valid_vanity_plate():
    assert is_valid("AB1234") == True

# Test case for invalid vanity plate starting with a number


def test_invalid_vanity_plate_starting_with_number():
    assert is_valid("1A234") == False

# Test case for invalid vanity plate with numbers in the middle


def test_invalid_vanity_plate_numbers_in_middle():
    assert is_valid("AB1C34") == False

# Test case for invalid vanity plate with '0' as the first number


def test_invalid_vanity_plate_starting_with_zero():
    assert is_valid("AB0123") == False

# Test case for invalid vanity plate with punctuation marks


def test_invalid_vanity_plate_with_punctuation():
    assert is_valid("AB!234") == False

# Test case for only numbers


def test_plates_all_numbers():
    assert is_valid("1234") == False

# Test case for invalid lenghts


def test_plates_length_checks():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDE") == True
