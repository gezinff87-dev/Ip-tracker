import requests
import socket
import re
import sys
import os
import time

# CORES
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    clear()
    print(f"""{GREEN}
██╗██████╗     █████╗ ███╗   ██╗ █████╗ ██╗     ██╗   ██╗███████╗██████╗ 
██║██╔══██╗   ██╔══██╗████╗  ██║██╔══██╗██║     ╚██╗ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ███████║██╔██╗ ██║███████║██║      ╚████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██╔══██║██║╚██╗██║██╔══██║██║       ╚██╔╝  ██╔══╝  ██╔══██╗
██║██║        ██║  ██║██║ ╚████║██║  ██║███████╗   ██║   ███████╗██║  ██║
╚═╝╚═╝        ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}""")

def clean_input(user_input):
    user_input = user_input.strip()
    user_input = user_input.replace("http://", "")
    user_input = user_input.replace("https://", "")
    user_input = user_input.replace("www.", "")
    user_input = user_input.split("/")[0]
    return user_input

def is_ip(ip):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip)

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def get_ip_info(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        return res.json()
    except:
        return None

def loading():
    print(YELLOW + "\n[~] Coletando dados..." + RESET)
    time.sleep(1)

def show_result(ip, data):
    print(GREEN + f"\n[+] IP: {ip}" + RESET)
    print(CYAN + f"[+] País: {data.get('country')}" + RESET)
    print(CYAN + f"[+] Cidade: {data.get('city')}" + RESET)
    print(CYAN + f"[+] Região: {data.get('region')}" + RESET)
    print(CYAN + f"[+] Org: {data.get('org')}" + RESET)

    loc = data.get("loc")
    if loc:
        lat, lon = loc.split(",")
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        print(YELLOW + f"\n[+] Localização aproximada: {lat}, {lon}" + RESET)
        print(GREEN + f"[+] Abrir no mapa: {maps_link}" + RESET)
    else:
        print(RED + "[!] Localização não disponível" + RESET)

def main():
    banner()

    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input(CYAN + "Digite IP ou domínio: " + RESET)

    user_input = clean_input(user_input)

    if is_ip(user_input):
        ip = user_input
    else:
        ip = resolve_domain(user_input)
        if not ip:
            print(RED + "\n[!] Domínio inválido ou não resolvido." + RESET)
            return

    loading()

    data = get_ip_info(ip)
    if not data:
        print(RED + "[!] Erro ao consultar API." + RESET)
        return

    show_result(ip, data)

if __name__ == "__main__":
    main()
