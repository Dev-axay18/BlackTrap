import socket
import sys

def start_sniffing(callback):
    host = socket.gethostbyname(socket.gethostname())
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_data, addr = sniffer.recvfrom(65535)
            callback(raw_data)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        sys.exit()
