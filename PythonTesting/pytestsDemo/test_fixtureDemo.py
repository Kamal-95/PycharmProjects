import pytest



@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixture Demo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixture Demo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture Demo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixture Demo3 method")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixture Demo4 method")