from src.domain.model import Browser
from src.pkg.settings import Settings, XpathSettings


def realizar_login(browser: Browser, settings: Settings, xpaths: XpathSettings) -> None:
    """Realiza o login em uma aplicação web

    Args:
        browser (Browser): Browser instance
        settings (Settings): Settings instance
    """
    browser.go_to(settings.url_base)
    browser.fill_fild(xpaths.login_input, settings.login)
    browser.fill_fild(xpaths.psw_input, settings.psw)
    browser.click_button(xpaths.login_button)
