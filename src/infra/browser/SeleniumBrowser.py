from selenium import webdriver

from src.domain.model.Browser import Browser
from src.pkg.settings import XpathSettings


def verify_browser_contains_driver(func):
    def inner(*args, **kwargs):
        if args[0].driver is None:
            raise Exception(
                "Driver not initialized. Use BrowserFactory to create a browser instance."
            )
        return func(*args, **kwargs)

    return inner


class SeleniumBrowser(Browser):
    driver: webdriver.Remote
    xpaths: XpathSettings

    def __init__(self, xpaths: XpathSettings = XpathSettings()):
        self.driver = None
        self.xpaths = xpaths

    @verify_browser_contains_driver
    def launch(self):
        pass

    @verify_browser_contains_driver
    def go_to(self, url: str) -> None:
        self.driver.get(url)

    @verify_browser_contains_driver
    def check_class_status(self) -> bool:
        return False

    @verify_browser_contains_driver
    def click_next_page(self) -> None:
        pass

    @verify_browser_contains_driver
    def close(self) -> None:
        self.driver.quit()
