from unittest.mock import patch
from horoscope import Horoscope

@patch('horoscope.Horoscope.fetch', return_value={'description': "fake"})
def test_horoscope_fetch(mock_fetch):
    aries = Horoscope('aries')
    test_response = aries.fetch()
    assert test_response == {'description': 'fake'}

@patch('horoscope.Horoscope.fetch', return_value={'description': "fake"})
def test_horoscope_fetch(mock_fetch):
    aries = Horoscope('aries')
    test_response = aries.fetch()
    assert test_response == {'description': 'fake'}

@patch('horoscope.fetch', return_value={'description': "fake"})
def test_horoscope_as_func(mock_fetch):
    aries = Horoscope.fetch('aries', 'today')
    assert aries == {'description': 'fake'}