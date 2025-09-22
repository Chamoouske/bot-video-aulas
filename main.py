from logging import error

from src.infra.browser.BrowserFactory import BrowserFactory
from src.domain.usecases import abrir_curso
from src.pkg.settings import settings, xpath_settings
from src.pkg.logging import basicConfig

if __name__ == "__main__":
    browser_name = settings.browser

    browser = BrowserFactory.create_browser(browser_name)
    try:
        abrir_curso(browser, settings, xpath_settings)
    except Exception as e:
        error(e)
        pass
    browser.close()
