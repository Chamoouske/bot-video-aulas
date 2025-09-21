from src.domain.model.Browser import Browser
from src.infra.browser.Chrome import Chrome
from src.infra.browser.Edge import Edge
from src.infra.browser.Firefox import Firefox


class BrowserFactory:
    @staticmethod
    def create_browser(browser: str) -> Browser:
        browsers: dict[str, type[Browser]] = {
            "chrome": Chrome,
            "firefox": Firefox,
            "edge": Edge,
        }

        _browser = browsers.get(browser.lower())
        if _browser is None:
            raise ValueError(f"Unsupported browser: {browser}")

        return _browser()
