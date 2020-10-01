import dotenv
import os
import smbclient
import sys

from smbclient import path

dotenv.load_dotenv()
smb_password = os.getenv('SMB_PASSWORD')
smb_server = os.getenv('SMB_SERVER')
smb_user = os.getenv('SMB_USER')

if smb_password is None:
    print('No password specified, using default...')
    smb_password = os.getenv('DEFAULT_PASSWORD')
    print("smb_password={}".format(smb_password))

if smb_server is None:
    print('No server specified, using default...')
    smb_server = os.getenv('DEFAULT_SERVER')
    print("smb_server={}".format(smb_server))

if smb_user is None:
    print('No user specified, using default...')
    smb_user = os.getenv('DEFAULT_USER')
    print("smb_user={}".format(smb_user))

smbclient.register_session(smb_server, username=smb_username, password=smb_password)
