import time
from PIL import Image
from services.image_to_string import convert_image_to_string
from models.subtitle_line import SubtitleLine
from models.srt_file import SrtFile


class SubtitlesController:
    def __init__(self, srt_file: SrtFile):
        self.srt_file = srt_file

    def process_image(self, image: Image):
        text = convert_image_to_string(image)
        curr_subtitle_line = self.srt_file.current_subtitle_line()

        if curr_subtitle_line.text_line is None:
            if text != '':
                curr_subtitle_line.start_time = time.time()
                curr_subtitle_line.text_line = text
            # if curr_subtitle_line.is_empty():
            # elif curr_subtitle_line.is_filled():
            #     new_subtitle_line = SubtitleLine(text, time.time())
            #     self.srt_file.add_subtitle_line(new_subtitle_line)

        # if curr_subtitle_line.text_line is not None:
        else:
            if curr_subtitle_line.text_line != text:
                curr_subtitle_line.end_time = time.time()
                self.srt_file.write_current_subtitle()

                if text != '':
                    new_subtitle_line = SubtitleLine(text, time.time())
                    self.srt_file.add_subtitle_line(new_subtitle_line)
                else:
                    self.srt_file.add_subtitle_line(SubtitleLine())
