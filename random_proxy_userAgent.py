import time

from fake_useragent import UserAgent
from fp.fp import FreeProxy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "CHANGE ME"
TEST_URL = "https://www.amazon.com"


class WebDriverManager:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        proxy = FreeProxy(timeout=1, rand=True).get()
        user_agent = UserAgent().random

        ser = Service(CHROME_DRIVER_PATH)
        op = webdriver.ChromeOptions()
        op.add_argument("--disable-infobars")
        op.add_argument("start-maximized")
        op.add_argument("--disable-extensions")
        op.add_argument("--start-maximized")
        op.add_argument("no-sandbox")
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--incognito")
        op.add_argument("--disable-xss-auditor")
        op.add_argument("--disable-web-security")
        op.add_argument("--allow-running-insecure-content")
        op.add_argument("--disable-setuid-sandbox")
        op.add_argument("--disable-webgl")
        op.add_argument("--disable-popup-blocking")
        op.add_argument("--disable-blink-features=AutomationControlled")
        op.add_argument("--disable-blink-features=AutomationControlled")
        op.add_experimental_option("useAutomationExtension", False)
        op.add_experimental_option("excludeSwitches", ["enable-automation"])
        op.add_argument("disable-infobars")
        op.add_argument(f"user-agent={user_agent}")
        op.add_argument(f"--proxy-server={proxy}")
        op.add_experimental_option(
            "prefs",
            {
                "profile.default_content_setting_values.media_stream_mic": 2,
                "profile.default_content_setting_values.media_stream_camera": 2,
                "profile.default_content_setting_values.geolocation": 2,
                "profile.default_content_setting_values.notifications": 2,
            },
        )
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.get(TEST_URL)
        print("Title: ", self.driver.title)
        self.driver.maximize_window()
        time.sleep(10)

    def close_driver(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    driver_manager = WebDriverManager()
    try:
        driver_manager.initialize_driver()
        # Perform your actions using the initialized driver
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver_manager.close_driver()
