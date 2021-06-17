import socket

def scan_port(ipaddr,port):
    port_sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port_Result=port_sk.connect_ex((ipaddr,port))
    if port_Result == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(scan_port('127.0.0.1',22))