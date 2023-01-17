"""
В третьому пакунку створити довільну кількість тестів (але не менше 3-х), організованих довільно,
але на конжному має бути 2 мітки: одна спільна для усіх тестів в цьому пакунку ("pack"),
інша -- спільна для як мінімум 2-х тестів ("joint"), і ще інша для остачі тестів ("rest").
На кожен тест в пакунку має бути застосована фікстура.
"""
import pytest

@pytest.fixture(scope='package')
def marks_testing_fixture():
    print("Executed before the tests")
    yield
    print("Executed after the tests")


@pytest.mark.pack
@pytest.mark.joint
def test_one(marks_testing_fixture):
    assert True


@pytest.mark.pack
@pytest.mark.joint
def test_two(marks_testing_fixture):
    assert True


@pytest.mark.rest
@pytest.mark.pack
def test_three(marks_testing_fixture):
    assert True

