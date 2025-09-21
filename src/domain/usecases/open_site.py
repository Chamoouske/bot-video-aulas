from src.domain.model.Browser import Browser


def open_site(browser: Browser, url: str) -> bool:
    """Use case to open a site in a browser

    Args:
        browser (Browser): Browser instance
        url (str): URL to open

    Returns:
        bool: True if the site was opened successfully
    """
    browser.launch()
    browser.go_to(url)
    return True
