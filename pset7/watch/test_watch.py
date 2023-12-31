from watch import parse


def test_parse():

    input = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
    output = 'https://youtu.be/xvFZjo5PgG0'
    assert parse(input) == output

    input = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    output = 'https://youtu.be/xvFZjo5PgG0'
    assert parse(input) == output

    input = '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
    output = None
    assert parse(input) == output
