import unittest
from .test_helper import open_image
from services.image_to_string import convert_image_to_string


class TestImageToString(unittest.TestCase):
    def test_convert_black_white(self):
        text = convert_image_to_string(open_image('image_ukr_black_1'))
        self.assertEqual(text, 'Розвідка вказує на невдоволених космічних шахтарів на місяцях Набу.')

    def test_convert_empty_black(self):
        text = convert_image_to_string(open_image('image_empty_black_1'))
        self.assertEqual(text, '')

    def test_convert_color(self):
        text = convert_image_to_string(open_image('image_ukr_color_1'))
        self.assertEqual(text, '- За що тебе вигнали, Джар-Джаре? - Це довга історія,')

    def test_convert_empty_color(self):
        text = convert_image_to_string(open_image('image_empty_color_1'))
        self.assertEqual(text, '')


if __name__ == '__main__':
    unittest.main()
