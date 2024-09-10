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

if __name__ == '__main__':
    ssh = MySSH()
    if ssh.connect('139.150.73.242', 'elias', '1111', timeout=5, port=22):
        ic('SSH is connected')
    else:
        ic('SSH is failed')
























