from logging import WARNING, DEBUG, INFO
from logging import basicConfig
from logging import FileHandler, StreamHandler


file_handler = FileHandler("logs.log", "a")
file_handler.setLevel(WARNING)


stream_handler = StreamHandler()


basicConfig(
    level=INFO,
    format="%(levelname)s: %(asctime)s -> %(message)s",
    handlers=[file_handler, stream_handler],
)
