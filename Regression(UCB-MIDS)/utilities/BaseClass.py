import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setupBrowser")
class BaseClass:
    def Explicit_wait(self, text):
        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, text)))