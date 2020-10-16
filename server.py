from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import yaml
import os

config_file = "server.yml"

def get_config(index):
    with open(config_file) as f:
        return yaml.load(f, Loader=yaml.FullLoader)[index]

if __name__ == "__main__":
    authorizer = DummyAuthorizer()

    authorizer.add_user(get_config("user_name"), get_config("password"), get_config("storage_path"), perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "File Synchronizer FTP Server Powered by pyftpdlib."

    address = ("", get_config("port"))
    server = FTPServer(address, handler)
    server.serve_forever()