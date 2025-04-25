from colorama import Fore, Style, init
init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + """
╔═══════════════════════════════════════╗
║      ADVANCED PYTHON SNIFFER          ║
║         Created By Ak$h@y-K           ║
╚═══════════════════════════════════════╝
""")

def colored_packet(src, dst, proto, ttl):
    print(f"{Fore.GREEN}[SRC]{Fore.WHITE} {src} "
          f"{Fore.MAGENTA}→ {Fore.CYAN}[DST]{Fore.WHITE} {dst} "
          f"{Fore.YELLOW}| Proto: {proto} TTL: {ttl}")
