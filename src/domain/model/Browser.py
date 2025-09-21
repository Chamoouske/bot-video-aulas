from abc import abstractmethod


class Browser:
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Browser, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @abstractmethod
    def launch(self) -> None:
        """Function to launch the browser instance"""
        pass

    @abstractmethod
    def go_to(self, url_site: str) -> None:
        """Function to navigate to a specific URL

        Args:
            url_site (str): url to navigate
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Function to close the browser instance"""
        pass

    @abstractmethod
    def click_next_page(self) -> None:
        """Function to click the next page button"""
        pass

    @abstractmethod
    def check_class_status(self) -> bool:
        """Function to check the status of a class in a web application"""
        pass
