import cv2
import numpy as np
from PIL import Image
from controllers.subtitles_controller import SubtitlesController


class ScreenRecorder:
    def __init__(self, subtitles_controller: SubtitlesController):
        self.subtitles_controller = subtitles_controller
        self.video = cv2.VideoCapture('/home/amd64ryzen/Videos/input_video.mkv')

    def run(self):
        success, image = self.video.read()
        count = 0
        while success:
            croped_image = image[1010:1060, 0:1920]
            # img = cv2.cvtColor(croped_image, cv2.COLOR_BGR2RGB)
            # lower = np.array([186, 186, 186], dtype="uint8")
            # upper = np.array([255, 255, 255], dtype="uint8")
            # mask = cv2.inRange(croped_image, lower, upper)
            # output = cv2.bitwise_and(croped_image, croped_image, mask=mask)
            # im_pil = Image.fromarray(output)
            im_pil = Image.fromarray(croped_image)
            self.subtitles_controller.process_image(im_pil)
            # cv2.imwrite("frame%d.jpg" % count, croped_image)
            success, image = self.video.read()
            print('Read a new frame: ', success)
            count += 1
        # image = Image.open('tests/data/image_empty_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_empty_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_ukr_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_ukr_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_empty_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_empty_color_1.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_ukr_color_2.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_ukr_color_2.png')
        # self.subtitles_controller.process_image(image)
        # image = Image.open('tests/data/image_empty_black_1.png')
        # self.subtitles_controller.process_image(image)
