from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        #opts = ChromeOptions()
        #opts.add_argument("--headless")
        #driver = webdriver.Chrome(options=opts)
        print("Launching Chrome browser.......")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        #opts = FirefoxOptions()
        #opts.add_argument("--headless")
        #driver = webdriver.Firefox(options=opts)
        print("Launching Firefox browser.......")

    else:
        driver = webdriver.Chrome()
        print("Launching default browser.......")

#    return driver
#    browser.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


############ PyTest HTML Report #################

# It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'non Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Desam'


# It is hook for delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
