"""
В другому пакунку створити файл з 3 параметризованими тестами, один з яких буде ітеруватись
і перевіряти одиничні значення, другий перевірятиме пари значень, третій перевірятиме будь-які
значення на ваш розсуд, але кожному значенню має бути присвоєний псевдонім.
На кожен з тестів має бути застосована одна глобальна фікстура. На усіх тестах має бути мітка "param"
"""
import pytest


@pytest.fixture(scope='package')
def params_testing_fixture():
    print("Executed before the tests")
    yield
    print("Executed after the tests")

@pytest.mark.param
@pytest.mark.parametrize("test_input", ([1, 2, 3, 4, 5], [345, 236, 788]))
def test_iteration(test_input, params_testing_fixture):
    for i in test_input:
        assert i


@pytest.mark.param
@pytest.mark.parametrize("test_input, expected", [("10 + 10", 20), ("35 - 8", 27), ("5 * 8", 40)])
def test_pairs(test_input, expected, params_testing_fixture):
    assert eval(test_input) == expected


@pytest.mark.param
@pytest.mark.parametrize("one, two, three", [(1, 2, 3), (55, 44, 33)],)
def test_with_alias(one, two, three, params_testing_fixture):
    assert one
    assert two
    assert three
