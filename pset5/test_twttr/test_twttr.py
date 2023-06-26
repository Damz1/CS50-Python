from twttr import shorten
import pytest


def test_lower_case():
    assert shorten('view') == 'vw'
    assert shorten('xbcd') == 'xbcd'


def test_upper_case():
    assert shorten('VIEW') == 'VW'
    assert shorten('XBcd') == 'XBcd'


def test_numbers_input():
    assert shorten('123') == '123'


def test_punctuation():
    assert shorten('./:') == './:'
