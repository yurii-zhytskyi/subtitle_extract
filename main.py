from services.args_parser import args
from models.srt_file import SrtFile
from controllers.subtitles_controller import SubtitlesController
from workers.screen_recorder import ScreenRecorder
# from constants import START_TIME


def run():
    # print(START_TIME)
    srt_file = SrtFile(args.subtitles_path)
    subtitles_controller = SubtitlesController(srt_file)
    ScreenRecorder(subtitles_controller).run()


if __name__ == '__main__':
    run()
