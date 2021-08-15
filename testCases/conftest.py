from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="/Users/jeevasubbiah/PycharmProjects/nopecommerce/drivers/chromedriver 8")
        print("Lanching Chrome browser")
    elif browser == "Firefox":
        driver = webdriver.Firefox(
            executable_path="/Users/jeevasubbiah/PycharmProjects/nopecommerce/drivers/geckodriver 2")
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome(
            executable_path="/Users/jeevasubbiah/PycharmProjects/nopecommerce/drivers/chromedriver 8")
        print("Lanching Chrome browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########## Pytest HTML Reports ########

#### It is hook for adding Enviroment info to HTML Reports #####

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] ='Divya'

#### It is hook for delete/Modify Enviroment info to HTML Reports ####

@pytest.mark.optionalhook
def pytest_metadata (metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

