from pydantic_settings import BaseSettings


class XpathSettings(BaseSettings):
    login_input: str = "/html/body/div[2]/form/div/div[2]/div[1]/input"
    psw_input: str = "/html/body/div[2]/form/div/div[2]/div[2]/input"
    login_button: str = "/html/body/div[2]/form/div/div[2]/div[3]/button"
    first_lesson_button: str = '//*[@id="tab-curriculum"]/ol/li[1]/ol/li[1]'
    wait_to_complete: str = "/html/body/div[3]/div/div[2]/span"
    next_lesson_button: str = "/html/body/div[2]/a"
    complete_lesson_when_not_a_video: str = "/html/body/div[4]/div/div[1]/a"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
