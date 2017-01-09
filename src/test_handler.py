from handler import handle
import pytest


@pytest.mark.parametrize('city', [
    'las vegas',
    'henderson',
    'boulder city'
])
def test_valid_cities(city):
    event = dict(city=city)
    result = handle(event, None)
    assert 'city' not in result['errors']
    assert 'We only deliver to' not in '::'.join(result['messages'])


@pytest.mark.parametrize('city', [
    'pahrump',
    'searchlight',
    ''
])
def test_invalid_cities(city):
    event = dict(city=city)
    result = handle(event, None)
    assert 'city' in result['errors']
    assert 'We only deliver to' in '::'.join(result['messages'])


@pytest.mark.parametrize('zipCode', [
    '89123',
    '89113',
    '89169'
])
def test_valid_zips(zipCode):
    event = dict(zip=zipCode)
    result = handle(event, None)
    assert 'zip' not in result['errors']


@pytest.mark.parametrize('zipCode', [
    '891231',
    '8916',
    ''
])
def test_invalid_zip_lengths(zipCode):
    event = dict(zip=zipCode)
    result = handle(event, None)
    assert 'zip' in result['errors']


def test_invalid_zip_location():
    event = dict(zip='90120')
    result = handle(event, None)
    assert 'zip' in result['errors']
    assert 'We only deliver to' in '::'.join(result['messages'])


@pytest.mark.parametrize('key', [
    'firstName',
    'lastName',
    'oogabooga'
])
def test_empty_values_fail(key):
    event = {key: ''}
    result = handle(event, None)
    assert key in result['errors']
