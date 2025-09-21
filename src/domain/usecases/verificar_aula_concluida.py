from src.domain.model.Browser import Browser


def verificar_aula_concluida(browser: Browser) -> bool:
    """Function to verify the status of a class in a web application

    Args:
        browser (Browser): Browser instance
    Returns:
        bool: True if the class is completed, False otherwise
    """
    status = False
    if browser.check_class_status():
        status = True
    return status
