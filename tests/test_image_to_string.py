import unittest
from .test_helper import open_image
from image_to_string import ImageToString


class TestImageToString(unittest.TestCase):
    def test_convert_black_white(self):
        image = open_image('image_ukr_black_1')
        text = ImageToString(image).convert()
        self.assertEqual(text, 'Розвідка вказує на невдоволених космічних шахтарів на місяцях Набу.')

    def test_convert_empty_black(self):
        image = open_image('image_empty_black_1')
        text = ImageToString(image).convert()
        self.assertEqual(text, '')

    def test_convert_color(self):
        image = open_image('image_ukr_color_1')
        text = ImageToString(image).convert()
        self.assertEqual(text, '- За що тебе вигнали, Джар-Джаре? - Це довга історія,')

    def test_convert_empty_color(self):
        image = open_image('image_empty_color_1')
        text = ImageToString(image).convert()
        self.assertEqual(text, '')
