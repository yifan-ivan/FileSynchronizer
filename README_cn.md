# FileSynchronizer

一个简单的同步两台设备上文件的小程序。

## 依赖

安装以下Python包：

 - watchdog
 - pyftpdlib

你也可以使用 `pip install -r requirements.txt` 来安装所有依赖。

## Client

### 配置文件

默认值：

```yaml
files:
  - "test.txt"

server_ip: 127.0.0.1
server_port: 21
user_name: "admin"
password: "123456"
```

 - `files`: 需要同步的文件
 - `server_ip`: 服务器的IP地址
 - `user_name`: FTP服务器的用户名
 - `password`: FTP服务器的密码

### 使用

将 `client.py` 和 `client.yml` 放在一个目录下，运行 `client.py`

## Server

### 配置文件

默认值：

```yaml
user_name: "admin"
password: "123456"
port: 21

storage_path: "./files"
```

 - `user_name`: FTP服务器的用户名
 - `password`: FTP服务器的密码
 - `port`: FTP服务器端口
 - `storage_path`: 文件存储路径

### 使用

将 `server.py` 和 `server.yml` 放在一个目录下，运行 `server.py`，确保端口未被占用