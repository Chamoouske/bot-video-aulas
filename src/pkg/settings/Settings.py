from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Bot Algaworks"
    login: str = ""
    psw: str = ""
    browser: str = "chrome"
    headless: bool = False
    url_base: str = "https://www.algaworks.com"
    course_url: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
