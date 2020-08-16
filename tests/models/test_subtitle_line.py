import unittest
from models.subtitle_line import SubtitleLine


class TestSubtitleLine(unittest.TestCase):
    def test_text_line(self):
        subtitle_line = SubtitleLine()
        some_text = 'some text'
        subtitle_line.text_line = some_text

        self.assertEqual(subtitle_line._text_line, some_text)

    def test_text_line_replace_dash_center(self):
        subtitle_line = SubtitleLine()
        subtitle_line.text_line = 'some - text'

        self.assertEqual(subtitle_line._text_line, 'some ‒ text')

    def test_text_line_replace_dash_start(self):
        subtitle_line = SubtitleLine()
        subtitle_line.text_line = '- text'

        self.assertEqual(subtitle_line._text_line, '‒ text')

    def test_text_line_replace_dash_end(self):
        subtitle_line = SubtitleLine()
        subtitle_line.text_line = 'some -'

        self.assertEqual(subtitle_line._text_line, 'some ‒')

    def test_text_line_not_replace_dash(self):
        subtitle_line = SubtitleLine()
        subtitle_line.text_line = 'some-text'

        self.assertEqual(subtitle_line._text_line, 'some-text')


if __name__ == '__main__':
    unittest.main()
