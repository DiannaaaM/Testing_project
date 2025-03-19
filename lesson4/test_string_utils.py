import pytest
from lesson4.string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("country", "Country"),
    ("language", "Language"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("_SDFG", "_sdfg"),
    (":dfgfdv", ":dfgfdv"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    123abc", "123abc"),
    ("     ", ""),
    ("  _SDFG", "_SDFG"),
    (" dfgfdv", "dfgfdv"),
    (" some text", "some text"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('123', '123'),
    ('', ''),
    ('qwer', 'qwer'),
    ('1', '1'),
    ('const', 'const'),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("hello", "l") == True
    assert string_utils.contains("qwerty", 'q') == True
    assert string_utils.contains('school', 'o') == True
    assert string_utils.contains('sdfg', 'g') == True
    assert string_utils.contains('sdfg', 'g') == True
    assert string_utils.contains('Sdfg', 'S') == True


@pytest.mark.negative
def test_contains_negative():
    assert string_utils.contains("hello", "g") == False
    assert string_utils.contains("qwerty", 'n') == False
    assert string_utils.contains('school', '1') == False
    assert string_utils.contains('sdfg', '.') == False
    assert string_utils.contains('sdfg', 'Z') == False
    assert string_utils.contains('Sdfg', 'u') == False


@pytest.mark.positive
def test_delete_positive():
    assert string_utils.delete_symbol("Swimm", "wi") == 'Smm'
    assert string_utils.delete_symbol("colledge", 'col') == 'ledge'
    assert string_utils.delete_symbol('1234567', '12345') == '67'
    assert string_utils.delete_symbol('qwertyU', 'qwerty') == 'U'
    assert string_utils.delete_symbol("Some text", 'Some') == ' text'
    assert string_utils.delete_symbol('carpit', 'carpit') == ''


@pytest.mark.negative
def test_delete_negative():
    assert string_utils.delete_symbol("Swimm", "a") == 'Swimm'
    assert string_utils.delete_symbol("colledge", '1') == 'colledge'
    assert string_utils.delete_symbol('delete method', 'some') == 'delete method'
    assert string_utils.delete_symbol('qwertyU', '') == 'qwertyU'
    assert string_utils.delete_symbol('anims', 'animals') == 'anims'