from PIL import Image
from image_to_string import ImageToString


def run():
    image = Image.open('tests/data/image_ukr_input_1.png')
    print(ImageToString(image).convert())


if __name__ == '__main__':
    run()
