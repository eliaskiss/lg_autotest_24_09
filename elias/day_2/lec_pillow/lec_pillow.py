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

    ######################################################
    # Convert Image Format
    ######################################################
    def convert_format(self, img_file_path, format):
        img = Image.open(img_file_path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        # /image/buz.jpg --> /image/buz.png
        dir = os.path.dirname(img_file_path)            # image\buz.jpg --> image
        # abs_path = os.path.abspath(img_file_path)     # 'C:\\source\\lg_autotest_24_09\\elias\\day_2\\lec_pillow\\image\\buz.jpg'
        file_name = os.path.basename(img_file_path)     # buz.jpg
        file_name = file_name.split('.')[0]             # buz
        file_name += f'.{format}'                       # buz.png
        path = os.path.join(dir, file_name)             # image + buz.png --> image\buz.png
        img.save(path)
        return path

if __name__ == '__main__':
    img_file_path = './image/buz.jpg'

    # Pillow 객체생성
    pillow = Pillow()

    # ######################################################
    # # 이미지 정보 출력
    # ######################################################
    # img_info = pillow.get_info(img_file_path)
    # ic(img_info)

    ######################################################
    # 이미지 포맷변경
    ######################################################
    new_image = pillow.convert_format(img_file_path, 'png')
    ic(pillow.get_info(new_image))


















