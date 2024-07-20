from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

from ABC_utility.test_data import test_data


@pytest.fixture(params=["chrome", "firefox", "edge"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif request.param == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(test_data.base_url)
    driver.implicitly_wait(3)
    yield
    time.sleep(3)
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("ABC_report", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "ABC Test Report"
