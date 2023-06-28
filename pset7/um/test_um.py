from um import count


def test_count():
    s = 'um'
    assert count(s) == 1

    s = 'um?'
    assert count(s) == 1

    s = 'Um, thanks for the album.,'
    assert count(s) == 1

    s = 'Um, thanks, um...'
    assert count(s) == 2
