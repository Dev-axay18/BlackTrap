from scapy.all import sniff, IP
from sniffer.color_console import colored_packet

def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        colored_packet(ip_layer.src, ip_layer.dst, ip_layer.proto, ip_layer.ttl)

def start(interface=None):
    sniff(prn=process_packet, iface=interface, store=False)
