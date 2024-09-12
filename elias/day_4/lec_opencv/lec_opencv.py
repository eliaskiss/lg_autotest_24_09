import cv2
from icecream import ic
from datetime import datetime

class WebCam:
    def __init__(self, portNum=None):
        self.port_num = portNum

    #################################################################
    # GEt Webcam List
    #################################################################
    def get_valid_camera_list(self, max_port_num=3):
        camera_port_list = []

        for index in range(max_port_num):
            cap = cv2.VideoCapture(index) # 0, 1, 2...
            ret, frame = cap.read()

            if ret is True and frame is not None:
                camera_port_list.append(index)
            else:
                break

        return camera_port_list

if __name__ == '__main__':
    cam = WebCam()
    port_list = cam.get_valid_camera_list()
    ic(port_list)
























