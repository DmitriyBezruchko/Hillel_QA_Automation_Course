import pytest

"""
В першому пакунку створтити файл з 5 тестами, що знаходяться у класі. Перед та після тестів повинна 
відпрацювати фікстура, що виведе в консоль повідомлення про початок та кінець свого виконання. 
Нехай тести також виведуть в консоль що небудь. На усі тести поставити мітку "from_class".
"""

@pytest.fixture(scope='class')
def types_testing_fixture():
    print("Executed before the tests")
    yield
    print("Executed after the tests")



class TestTypes:
    @pytest.mark.from_class
    def test_int(self, types_testing_fixture):
        print("first test running")
        assert type(2) is int

    @pytest.mark.from_class
    def test_float(self, types_testing_fixture):
        print("second test running")
        assert type(2.6) is float

    @pytest.mark.from_class
    def test_str(self, types_testing_fixture):
        print("third test running")
        assert type("hello") is str

    @pytest.mark.from_class
    def test_list(self, types_testing_fixture):
        print("fourth test running")
        lt = [1, 2, 3, 4, 5]
        assert type(lt) is list

    @pytest.mark.from_class
    def test_set(self, types_testing_fixture):
        print("fifth test running")
        dt = {1, 2, 3, 4, 5}
        assert type(dt) is set






