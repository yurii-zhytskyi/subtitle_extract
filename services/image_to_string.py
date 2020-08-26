import pytesseract
from PIL import Image


def convert_image_to_string(image: Image, lang='ukr') -> str:
    output_text = pytesseract.image_to_string(image, lang=lang)
    return output_text.strip()
