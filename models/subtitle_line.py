import re


class SubtitleLine:
    def __init__(self, text=None, start=None, end=None):
        self._text_line: str = text
        self._start_time: int = start
        self._end_time: int = end

    def is_filled(self) -> bool:
        return self.text_line is not None \
               and self.start_time is not None\
               and self.end_time is not None

    def is_empty(self) -> bool:
        return self.text_line is None \
               and self.start_time is None \
               and self.end_time is None

    @property
    def text_line(self):
        return self._text_line

    @text_line.setter
    def text_line(self, value: str):
        self._text_line = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value: int):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value: int):
        self._end_time = value
