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

    #################################################################
    # Capture Video Stream
    #################################################################
    def capture_video(self, width=1280, height=720, isMono=False, flip=None):
        # 웹캠 객체생성
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)

        # 웹캠 옵션설정
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        while True:
            # 현재 영상 캡쳐
            ret, frame = cap.read()

            # 캡쳐 실패시 실행중단
            if ret is False:
                break

            # 흑백전환
            if isMono is True:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # 플립적용
            if flip is not None:
                # flip: 0 -> bottom to top, 1 -> left to right
                frame = cv2.flip(frame, flip)

            cv2.imshow('frame', frame)

            if cv2.waitKey(100) == ord('q'):
                break

        # 객체핸들 릴리즈
        cap.release()
        # cv2.destroyAllWindows()
        cv2.destroyWindow('frame')

    #################################################################
    # Record Video Stream with AVI Codec
    #################################################################
    def record_video(self, video_file_name, width=1280, height=720, flip=None, fps=24):
        # 웹캠 객체생성
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)

        # 웹캠 옵션설정
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # 코덱설정
        # fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        # 실제 적용된 크기
        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        
        # Writer 객체
        out = cv2.VideoWriter(f'{video_file_name}.avi', fourcc, fps, frame_size)

        while cap.isOpened():
            # 현재 영상 캡쳐
            ret, frame = cap.read()

            # 캡쳐 실패시 실행중단
            if ret is False:
                break

            # 플립적용
            if flip is not None:
                # flip: 0 -> bottom to top, 1 -> left to right
                frame = cv2.flip(frame, flip)

            # 윈도우화면에 영상출력
            cv2.imshow('frame', frame)

            # 동영상파일에 Frame 저장
            out.write(frame)

            if cv2.waitKey(int(1000/fps)) == ord('q'):
                break

        # 객체핸들 릴리즈
        cap.release()
        # cv2.destroyAllWindows()
        cv2.destroyWindow('frame')





if __name__ == '__main__':
    cam = WebCam()
    port_list = cam.get_valid_camera_list()
    ic(port_list)

    if len(port_list) > 0:
        # 첫번째 웹캠을 선택
        port_num = port_list[0]
        cam.set_port(port_num)

        # ################################################################
        # # Capture Image(Snapshot)
        # ################################################################
        # file_name = f'{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.png'
        # ic(cam.capture_image(file_name))

        # ################################################################
        # # Capture Video Stream
        # ################################################################
        # cam.capture_video()
        # cam.capture_video(800, 600)
        # cam.capture_video(isMono=True)
        # cam.capture_video(flip=0)
        # cam.capture_video(flip=1)
        # cam.capture_video(isMono=True, flip=1)

        
        
        
























