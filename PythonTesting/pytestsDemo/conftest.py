import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("user input data on run time")
    return ["Kamal", "Sharma", "kamal kumar.com"]

@pytest.fixture(params=[("Chrome", "Kamal"), ("Firefox", "Kumar"), ("IE","KK")])
def CrossBrowser(request):
    return request.param