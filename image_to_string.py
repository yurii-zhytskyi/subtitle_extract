import pytesseract


class ImageToString:
    def __init__(self, image):
        self.image = image

    def convert(self, lang='ukr') -> str:
        output_text = pytesseract.image_to_string(self.image, lang=lang)
        return output_text.strip()
