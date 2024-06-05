import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.smoke
def test_firstCreditCardProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondProgram(setup):
    print("Good Morning")


@pytest.mark.usefixtures("CrossBrowser")
class TestExample2(BaseClass):
    def test_CrossBrowser(self,CrossBrowser):
        print(CrossBrowser[0])
        print(CrossBrowser[1])
        log = self.getLogger()
        log.info(CrossBrowser[0])
        log.info(CrossBrowser[1])

