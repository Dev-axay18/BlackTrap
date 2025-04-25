import struct
import socket

def parse_packet(data):
    ip_header = data[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4

    ttl = iph[5]
    protocol = iph[6]
    src_addr = socket.inet_ntoa(iph[8])
    dest_addr = socket.inet_ntoa(iph[9])

    print(f"[IP] {src_addr} -> {dest_addr} | Protocol: {protocol}, TTL: {ttl}")
