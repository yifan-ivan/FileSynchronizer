# FileSynchronizer

[中文](https://github.com/yifan-ivan/FileSynchronizer/blob/master/README_cn.md)

A simple app to sync files between two devices.

## Requirements

Install the following python libraries:

 - watchdog
 - pyftpdlib

You can also use `pip install -r requirements.txt` to install all the requirements.

## Client

### Config file

Defult value:

```yaml
files:
  - "test.txt"

server_ip: 127.0.0.1
server_port: 21
user_name: "admin"
password: "123456"
```

 - `files`: The file need to be synchronized.
 - `server_ip`: Server IP
 - `user_name`: Username of the FTP Server
 - `password`: Password of the FTP Server

### Usage

Put `client.py` and `client.yml` in a folder, run `client.py`.

## Server

### Config file

Defult value:

```yaml
user_name: "admin"
password: "123456"
port: 21

storage_path: "./files"
```

 - `user_name`: Username of the FTP Server
 - `password`: Password of the FTP Server
 - `port`: The port of the FTP Server
 - `storage_path`: The path for the storage

### Useage

put `server.py` and `server.yml` in a folder, run `server.py`，make sure the port is not occupied.