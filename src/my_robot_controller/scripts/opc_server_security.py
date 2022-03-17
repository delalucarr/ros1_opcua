from distutils.command.config import config
import pwd
from pyclbr import Class
import socket
from textwrap import indent
import bcrypt

import json

from matplotlib.font_manager import json_dump

class OPC_SERVER_SECURITY:
    def __init__(self):
        self.server_socket = socket.socket()
        self.salt = bcrypt.gensalt()



    def init_opc_server_securtiy(self,ip):
        self.server_socket.bind(ip, 5000)
        self.server_socket.listen(1)

    
    def set_server_credentials(self,username,password):
        pwd = password.encode('utf-8')
        user = username.encode('utf-8')
        server_hash_pwd = bcrypt.hashpw(pwd, self.salt)
        server_hash_user = bcrypt.hashpw(user , self.salt)



        out_json = dict()
 
        out_json['username'] = server_hash_user.decode()
    
        out_json['password'] = server_hash_pwd.decode()

        out_json['salt'] = self.salt.decode()


        with open('credential.json', 'w') as fp:
            json_dump(out_json,fp,indent = 4 , ensure_ascii= False)
    
    

    def client_authentication(self):
        config_file = open('credential.json')
        config_data = json.load(config_file)
        config_file.close()

        is_client_authenticated= False

        print("waiting for clients.....")
        conn, address = self.server_socket.accept()
        while True:
            recvd_data  = conn.recv(1024).decode()
            recvd_data  = recvd_data.split(" , ")
            user = recvd_data[0]
            pwd = recvd_data[1]
            """
            str = "username , password"
            """

        





         
    
