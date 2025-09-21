from src.domain.model.Browser import Browser


def next_page(browser: Browser) -> bool:
    """Function to navigate to the next page in a web application

    Args:
        browser (Browser): Browser instance
    Returns:
        bool: True if the navigation was successful
    """
    browser.click_next_page()
    return True
