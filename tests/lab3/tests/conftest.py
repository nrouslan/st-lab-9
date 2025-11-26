import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Chrome"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")

    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page_url():
    """URL страницы логина"""
    # Путь к локальному файлу
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return f"file:///{os.path.join(current_dir, '../web/index.html')}"
