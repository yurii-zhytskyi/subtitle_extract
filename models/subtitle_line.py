import re


class SubtitleLine:
    def __init__(self, text='', start=0, end=0):
        self._text_line: str = text
        self._start_time: int = start
        self._end_time: int = end

    @property
    def text_line(self):
        return self._text_line

    @text_line.setter
    def text_line(self, value: str):
        a = re.compile(r'(^|\s+)-(\s+|$)')
        self._text_line = a.sub('\\1‒\\2', value)

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value: int):
        self._start_time = value

    @property
    def end_time(self):
        return self._start_time

    @end_time.setter
    def end_time(self, value: int):
        self._end_time = value
