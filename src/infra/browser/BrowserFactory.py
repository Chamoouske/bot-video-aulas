from src.domain.model.Browser import Browser
from src.infra.browser import Chrome, Edge, Firefox, Chromium


class BrowserFactory:
    @staticmethod
    def create_browser(browser: str, *args, **kwargs) -> Browser:
        browsers: dict[str, type[Browser]] = {
            "chrome": Chrome,
            "chromium": Chromium,
            "firefox": Firefox,
            "edge": Edge,
        }

        _browser: type[Browser] | None = browsers.get(browser.lower())
        if _browser is None:
            raise ValueError(f"Unsupported browser: {browser}")

        return _browser(*args, **kwargs)
