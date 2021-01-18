from ..common import *
import paramiko
import socket
import time


class LinuxClient:
    def __init__(self,
                 host: str,
                 port: int,
                 user: str,
                 password: str,
                 is_invoke_shell=False) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.is_invoke_shell = is_invoke_shell
        self.client = None
        self.is_connect = False

    def connect(self) -> ResultData:
        """
        建立连接
        :return: 返回连接成功与否
        """
        self.is_connect = False
        result = False
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.is_invoke_shell:
                client.invoke_shell()
            client.connect(hostname=self.host,
                           port=self.port,
                           username=self.user,
                           password=self.password)
            self.client = client
            msg = f'连接成功：{self.host}'
            result = True
            self.is_connect = True
        except paramiko.ssh_exception.AuthenticationException:
            msg = f'服务器{self.host}认证错误：user:{self.user} password:{self.password}'
            self.client = None
        except socket.error:
            msg = f'网络异常：{self.host}'
            self.client = None
        logger_error_debug(msg)
        return ResultData(result, msg)

    def exec_cmd(self, cmd: str) -> ResultData:
        """
        非交互式场景下执行linux命令
        1. 实例初始化调用connect失败后，跳过命令执行；
        2. 网络异常后会，间隔3秒重连50次；
        3. 命令执行失败，返回标准错误输出，执行成功返回标准输出；
        4. 连接服务器失败，命令发送失败，返回False
        :param cmd: 执行的linux命令
        :return: 返回命令执行成功与否
        """
        if not self.client:
            msg = '连接服务器失败，跳过命令执行'
            logger.warning(msg)
            return ResultData(False, msg)
        for _ in range(3):
            try:
                logger.info(f'在机器{self.host}执行命令：{cmd}')
                stdin, stdout, stderr = self.client.exec_command(cmd)
                break
            except paramiko.ssh_exception.SSHException:
                logger.warning(f'终端已断开连接，休眠3秒重新连接服务器')
                time.sleep(3)
                try:
                    self.connect()
                except Exception as e:
                    logger_error_debug(f'重连服务器异常：{e}')
                    raise
        else:
            msg = '命令发送失败'
            logger_error_debug(msg)
            return ResultData(False, msg)
        err = stderr.read().decode()
        if err:
            msg = f'命令执行报错：{err}'
            logger.warning(msg)
            return ResultData(False, msg)
        else:
            rsp_str = stdout.read().decode()
            msg = f'命令执行成功,响应为：{rsp_str}'
            return ResultData(True, msg)

    def upload(self, local_path: str, route_path: str) -> None:
        """
        上传文件到服务器
        :param local_path: 本地路径
        :param route_path: 远程路径
        """
        sftp = self.client.open_sftp()
        sftp.put(local_path, route_path)

    def download(self, local_path: str, route_path: str) -> None:
        """
        从服务器下载文件
        :param local_path: 本地路径
        :param route_path: 远程路径
        """
        sftp = self.client.open_sftp()
        sftp.get(route_path, local_path)

    def close(self) -> None:
        """
        关闭连接
        """
        if self.client:
            self.client.close()
