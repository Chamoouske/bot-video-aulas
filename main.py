from src.infra.browser.BrowserFactory import BrowserFactory
from src.pkg.settings import settings

if __name__ == "__main__":
    browser_name = settings.browser

    browser = BrowserFactory.create_browser(browser_name)
    browser.launch()
    print(f"{browser_name.capitalize()} browser launched successfully!")

    browser.go_to(settings.url_base)

    browser.close()
