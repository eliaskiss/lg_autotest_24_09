import cv2
from icecream import ic
from datetime import datetime

class WebCam:
    def __init__(self, portNum=None):
        self.port_num = portNum

    #################################################################
    # Get Webcam List
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

    #################################################################
    # Set Port Number
    #################################################################
    def set_port(self, portNum):
        self.port_num = portNum

    #################################################################
    # Capture Webcam Image
    #################################################################
    def capture_image(self, file_name, width=1280, height=720):
        # 웹캠 객체생성
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)

        # 웹캠 옵션설정
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # 카메라 이미지 캡쳐
        _, frame = cap.read()

        # 캡쳐된 이미지를 파일로 저장
        ret = cv2.imwrite(file_name, frame)

        # 객체핸들 릴리즈
        cap.release()

        return ret, file_name

if __name__ == '__main__':
    cam = WebCam()
    port_list = cam.get_valid_camera_list()
    ic(port_list)

    if len(port_list) > 0:
        # 첫번째 웹캠을 선택
        port_num = port_list[0]
        cam.set_port(port_num)

        ################################################################
        # Capture Image(Snapshot)
        ################################################################
        file_name = f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%s")}.png'
        ic(cam.capture_image(file_name))
        
        
        
























