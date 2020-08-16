import pathlib
from PIL import Image
from .test_constants import TEST_DATA_PATH


def open_image(name) -> Image:
    return Image.open(str(pathlib.Path(TEST_DATA_PATH, f'{name}.png')))
