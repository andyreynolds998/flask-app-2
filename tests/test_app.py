import pytest

MOCK_DICTIONARY = {
    "first_name": "Andrew",
    "last_name": "Reynolds",
    "active": 1,
    "age": 23
}

def test_dictionary_has_valid_age():
    assert isinstance(MOCK_DICTIONARY["age"], int)

def test_dictionary_has_valid_username():
    assert MOCK_DICTIONARY.get("username")  == "AndrewReynolds"
