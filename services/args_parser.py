import pathlib
import argparse


class SourcePathAction(argparse.Action):
    def __call__(self, custom_parser, namespace, values, option_string=None):
        values = pathlib.Path(values)
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser(description='Extract subtitles through video in web browser using recording and OCR',
                                 prog='Extract subtitles')
parser.add_argument('subtitles_path', help='output subtitles path', action=SourcePathAction)

args = parser.parse_args()
