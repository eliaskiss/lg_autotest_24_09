from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
from PIL import ImageOps

import os
from enum import Enum
from icecream import ic
from datetime import datetime

ic.configureOutput(includeContext=True)

class FILTER(Enum):
    BLUR = 0
    CONTOUR = 1
    DETAIL = 2
    EDGE_ENHANCE = 3
    EDGE_ENHANCE_MORE = 4
    EMBOSS = 5
    FIND_EDGES = 6
    SHARPEN = 7
    SMOOTH = 8
    SMOOTH_MORE = 9

class Pillow:
    ######################################################
    # Get Image File Information
    ######################################################
    def get_info(self, img_file_path):
        img = Image.open(img_file_path)
        return ({'FileName':img.filename,
                 'Format':img.format,
                 'Format Desc.':img.format_description,
                 'Width':img.width,
                 'Height':img.height,
                 'Mode':img.mode})

if __name__ == '__main__':
    img_file_path = './image/buz.jpg'

    # Pillow 객체생성
    pillow = Pillow()

    ######################################################
    # 이미지 정보 출력
    ######################################################
    img_info = pillow.get_info(img_file_path)
    ic(img_info)



















