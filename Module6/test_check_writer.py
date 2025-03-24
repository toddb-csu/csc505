# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 6: Critical Thinking Assignment
#
# This Python program will test the methods in our check_writer script
#
from check_writer import convert_number_to_words, get_amount, get_formatted_check_amount, split_amount
from unittest.mock import patch
import pytest


def test_convert_number_to_words_one():
    assert convert_number_to_words(1) == 'one'


def test_convert_number_to_words_ten():
    assert convert_number_to_words(10) == 'ten'


def test_convert_number_to_words_eleven():
    assert convert_number_to_words(11) == 'eleven'


def test_convert_number_to_words_twenty():
    assert convert_number_to_words(20) == 'twenty'


def test_convert_number_to_words_twenty_one():
    assert convert_number_to_words(21) == 'twenty-one'


def test_convert_number_to_words_ninety_nine():
    assert convert_number_to_words(99) == 'ninety-nine'


def test_convert_number_to_words_one_hundred():
    assert convert_number_to_words(100) == 'one hundred'


def test_convert_number_to_words_two_hundred_fifteen():
    assert convert_number_to_words(215) == 'two hundred fifteen'


def test_convert_number_to_words_five_hundred_five():
    assert convert_number_to_words(505) == 'five hundred five'


def test_convert_number_to_words_one_thousand():
    assert convert_number_to_words(1000) == 'one thousand'


def test_convert_number_to_words_ten_thousand():
    assert convert_number_to_words(10000) == 'ten thousand'


def test_convert_number_to_words_fifteen_thousand():
    assert convert_number_to_words(15000) == 'fifteen thousand'


def test_convert_number_to_words_sixteen_thousand_five_hundred():
    assert convert_number_to_words(16500) == 'sixteen thousand five hundred'


def test_convert_number_to_words_seventeen_thousand_five_hundred_five():
    assert convert_number_to_words(17505) == 'seventeen thousand five hundred five'


def test_convert_number_to_words_seventeen_thousand_five_hundred_seventeen():
    assert convert_number_to_words(17517) == 'seventeen thousand five hundred seventeen'


def test_convert_number_to_words_twenty_five_thousand_five_hundred_seventeen():
    assert convert_number_to_words(25517) == 'twenty-five thousand five hundred seventeen'


@patch('builtins.input', lambda *args: 0.01)
def test_get_amount_one_cent():
    assert get_amount() == 0.01


@patch('builtins.input', lambda *args: 0.00)
def test_get_amount_zero():
    assert get_amount() == 0.00


@patch('builtins.input', lambda *args: -0.01)
def test_get_amount_negative_one_cent():
    assert get_amount() == 0.00


@patch('builtins.input', lambda *args: 'test')
def test_get_amount_string():
    assert get_amount() == 0.00


def test_split_amount():
    assert split_amount(10.75) == (10, 75)


def test_get_formatted_check_amount():
    assert get_formatted_check_amount('ten', 5) == "ten and 05/100 dollars"


def test_get_formatted_check_amount_with_zero_cents():
    assert get_formatted_check_amount('five', 0) == "five and 00/100 dollars"
