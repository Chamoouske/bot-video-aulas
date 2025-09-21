from src.infra.browser.BrowserFactory import BrowserFactory
from src.domain.usecases import open_site
from src.pkg.settings import settings

if __name__ == "__main__":
    browser_name = settings.browser

    browser = BrowserFactory.create_browser(browser_name)

    open_site(browser, settings.url_base)
    browser.close()
