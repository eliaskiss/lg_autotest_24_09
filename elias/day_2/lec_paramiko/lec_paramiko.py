import paramiko
from paramiko import SSHClient
from scp import SCPClient
import os
import stat
import time
from icecream import ic
import sys

ic.configureOutput(includeContext=True)

class MySSH:
    def __init__(self):
        self.client = None      # SSH Client Object
        self.scp_client = None  # SCP Client Object
        self.ftp_client = None  # SFTP Client Object

    #####################################################################
    # Check Connection
    #####################################################################
    def isAlive(self):
        if self.client is None:
            return False
        else:
            return self.client.get_transport().is_active()

    #####################################################################
    # Connect Host
    #####################################################################
    def connect(self, host, user_id, user_password, port=22, timeout=None):
        # 접속여부 확인
        if self.client is None:
            self.client = SSHClient()

            # 이 코드를 추가해야만
            # 'not found in known hosts'라는 예외가 발생하지 않음
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=host, port=port, username=user_id,
                                password=user_password, timeout=timeout)

            if self.isAlive():
                self.password = user_password
                return True
            else:
                return False

    #####################################################################
    # Disconnect
    #####################################################################
    def disconnect(self):
        if self.client is not None:
            self.client.close()

    #####################################################################
    # Execute Shell Command
    #####################################################################
    def exeCommand(self, command, isReturn = False):
        if self.isAlive():
            stdin, stdout, stderr = self.client.exec_command(command)

            if isReturn is True:
                return stdout.readlines()
        else:
            ic('Client is not connected!!!')

    #####################################################################
    # Execute Shell Command as root (sudo)
    #####################################################################
    def sudoCommand(self, command, isReturn=False):
        if self.isAlive():
            stdin, stdout, stderr = self.client.exec_command('sudo ' + command, get_pty=True)

            stdin.write(self.password + '\n')
            time.sleep(0.1)

            if isReturn is True:
                return stdout.readlines()
        else:
            ic('Client is not connected!!!')

    #########################################################
    # Get File From Host (SFTP)
    # srcFilePath: Server(host), dstFilePath: Local(PC, Client)
    #########################################################
    def getFromHost(self, srcFilePath, dstFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        self.ftp_client.get(srcFilePath, dstFilePath)

















if __name__ == '__main__':
    ssh = MySSH()
    if ssh.connect('139.150.73.242', 'elias', '1111', timeout=5, port=22):
        ic('SSH is connected')

        # ###############################################################
        # # Process List 파일생성 (ps -ef > process_list.txt)
        # ###############################################################
        # ssh.exeCommand('ps -ef > process_list.txt')

        # ###############################################################
        # # 파일목록 가져오기 (ls -al)
        # ###############################################################
        # file_list = ssh.exeCommand('ls -al', isReturn=True)
        # # ic(file_list)
        # for file in file_list:
        #     print(file, end='')

        # ###############################################################
        # # temp 폴더로 이동 후 process_list.txt 파일 생성
        # ###############################################################
        # ssh.exeCommand('cd temp') # temp폴더로 이동
        # ssh.exeCommand('ps -ef > process_list.txt') # process_list.txt 파일생성
        #
        # # ; - 앞의 명령어가 실패해도, 뒤에 명령어를 실행
        # # && - 앞의 명령어가 성공했을때만, 뒤에 명령어를 실행
        # # & - 앞의 명령어를 background로 실행하고 나서 뒤에 명령어를 실행
        # ssh.exeCommand('cd temp && ps ?-ef > process_list.txt')  # process_list.txt 파일생성

        # ###############################################################
        # # Shell Script 파일생성 후 실행권한을 주고 실행
        # ###############################################################
        # ssh.exeCommand('echo "ps -ef > process_list.txt" > make_process_list.sh')   # shell script 파일생성
        # ssh.exeCommand('chmod +x ./make_process_list.sh')                            # 실행권한 추가
        # ssh.exeCommand('./make_process_list.sh')                                    # shell script 실행

        # ###############################################################
        # # sudo 커맨드 실행
        # ###############################################################
        # ssh.exeCommand('sudo mkdir /temp/elias')
        # ssh.sudoCommand('mkdir /temp/elias')


    else:
        ic('SSH is failed')
























