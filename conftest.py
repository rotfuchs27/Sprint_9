import pytest
import os
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": False
    })

    driver = Remote(
        command_executor=os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub"),
        options=options
    )
    yield driver
    driver.quit()


