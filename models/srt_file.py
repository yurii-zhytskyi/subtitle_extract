import re
from datetime import datetime, timezone
from typing import List
from pathlib import Path
from .subtitle_line import SubtitleLine
from services.format_timestamp import format_timestamp


class SrtFile:
    def __init__(self, file_path: Path):
        self._subtitles: List[SubtitleLine] = [SubtitleLine()]
        self._file = file_path.open('w')
        # TODO move to constant
        self.start_time = datetime.now().timestamp()

    def __del__(self):
        self._file.close()

    def current_subtitle_line(self) -> SubtitleLine:
        return self._subtitles[-1]

    def add_subtitle_line(self, subtitle_line: SubtitleLine) -> None:
        self._subtitles.append(subtitle_line)

    def write_current_subtitle(self) -> None:
        subtitle_line = self.current_subtitle_line()

        if subtitle_line.is_filled():
            start = format_timestamp(subtitle_line.start_time - self.start_time)
            end = format_timestamp(subtitle_line.end_time - self.start_time)
            text = re.compile(r'(^|\s+)-(\s+|$)').sub('\\1‒\\2', subtitle_line.text_line)
            formatted_subtitle_line = '\n'.join([str(len(self._subtitles)), f'{start} --> {end}', text, '', ''])

            self._file.write(formatted_subtitle_line)
