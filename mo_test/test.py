import socket
import threading
import sys
import base64
import hashlib
import struct

HOST = 'localhost'
PORT = 1235
MAGIC_STRING = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
HANDSHAKE_STRING = "HTTP/1.1 101 Switching Protocols\r\n" \
                   "Upgrade:websocket\r\n" \
                   "Connection: Upgrade\r\n" \
                   "Sec-WebSocket-Accept: {0}\r\n" \
                   "WebSocket-Location: ws://{1}:{2}/chat\r\n" \
                   "WebSocket-Protocol:chat\r\n\r\n"


class Th(threading.Thread):
    def __init__(self, conn):
        super(Th, self).__init__()
        self.con = conn

    def run(self):
        while True:
            try:
                pass
            except:
                self.con.close()

    def recv_data(self, num):
        try:
            all_data = self.con.recv(num)
            if not len(all_data):
                return False
        except:
            return False
        else:
            code_len = ord(all_data[1]) & 127
            if code_len == 126:
                masks = all_data[4:8]
                data = all_data[8:]
            elif code_len == 127:
                masks = all_data[10:14]
                data = all_data[14:]
            else:
                masks = all_data[2:6]
                data = all_data[6:]
            raw_str = ""
            for i, d in enumerate(data):
                raw_str += chr(ord(d) ^ ord(masks[i % 4]))
        return raw_str

    def send_data(self, data):
        if data:
            data = data
        else:
            return False
        token = b"\x81"
        length = len(data)
        if length < 126:
            token += struct.pack("B", length)
        elif length <= 0xFFFF:
            token += struct.pack("!BH", 126, length)
        else:
            token += struct.pack("!BQ", 127, length)
        # struct为Python中处理二进制数的模块，二进制流为C，或网络流的形式。
        data = token + data
        self.con.send(data)
        return True


def handshake(conn):
    headers = {}
    shake = conn.recv(1024).decode()

    if not len(shake):
        return False

    data, _ = shake.split('\r\n\r\n', 1)
    for line in data.split('\r\n')[1:]:
        key, val = line.split(': ', 1)
        headers[key] = val

    if 'Sec-WebSocket-Key' not in headers:
        print('This socket is not websocket, client close.')
        conn.close()
        return False

    sec_key = headers['Sec-WebSocket-Key']
    res_key = base64.b64encode(hashlib.sha1((sec_key + MAGIC_STRING).encode()).digest())

    str_handshake = HANDSHAKE_STRING.format(res_key.decode(), HOST, str(PORT))
    print(str_handshake)
    conn.send(str_handshake.encode())
    return True


def new_service(ip, port):
    """start a service socket and listen
    when coms a connection, start a new thread to handle it"""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((ip, port))
        sock.listen(1000)
        print("bind {0}:{1},ready to use".format(ip, port))
    except:
        print("Server is already running,quit")
        sys.exit()

    while True:
        conn, address = sock.accept()
        # 返回元组（socket,add），accept调用时会进入waite状态
        print("Got connection from ", address)
        if handshake(conn):
            print("handshake success")
            try:
                t = Th(conn)
                t.start()
                print('new thread for client ...')
            except Exception as e:
                print('start new thread error')
            except KeyboardInterrupt:
                conn.close()


if __name__ == '__main__':
    # _port = int(sys.argv[1])
    new_service(HOST, PORT)
