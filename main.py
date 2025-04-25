import argparse
from scapy.all import get_if_list, conf
from sniffer.advanced_sniffer import start
from sniffer.color_console import banner

if __name__ == "__main__":
    banner()
    print("\n[💡] Available interfaces:")
    for iface in conf.ifaces:
        print(f"   • {iface}")
    parser = argparse.ArgumentParser(description="Python Network Sniffer Tool")
    parser.add_argument('-i', '--interface', help='Network interface (optional)', default=None)

    args = parser.parse_args()

    try:
        print("\n[*] Sniffing started... Press Ctrl+C to stop.\n")
        start(args.interface)
    except KeyboardInterrupt:
        print("\n[!] Sniffing stopped by user.")
        exit(0)  
