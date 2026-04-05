import requests
import socket
import re
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
██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
             🕵️  IP TRACKER  🕵️
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

def get_ip_info(ip, proxies=None):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5, proxies=proxies)
        return res.json()
    except:
        return None

def get_my_ip(proxies=None):
    try:
        res = requests.get("https://ipinfo.io/json", timeout=5, proxies=proxies)
        data = res.json()
        return data.get("ip"), data
    except:
        return None, None

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
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
        print(YELLOW + f"\n[+] Localização: {lat}, {lon}" + RESET)
        print(GREEN + f"[+] Mapa: {maps_link}" + RESET)
    else:
        print(RED + "[!] Sem localização" + RESET)

def use_proxy():
    proxy = input(CYAN + "\nDigite proxy (ip:porta): " + RESET)

    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    loading()

    ip, data = get_my_ip(proxies)

    if not ip:
        print(RED + "[!] Proxy inválido ou não funcionando" + RESET)
        return

    print(GREEN + "\n[+] IP via Proxy:" + RESET)
    show_result(ip, data)

def main():
    while True:
        banner()

        print(CYAN + "[1] Consultar URL")
        print("[2] Consultar IP")
        print("[3] Meu IP (público e local)")
        print("[4] Usar Proxy\n" + RESET)

        choice = input("Escolha: ")

        if choice == "1":
            user_input = input(CYAN + "\nDigite a URL: " + RESET)
            user_input = clean_input(user_input)

            ip = resolve_domain(user_input)
            if not ip:
                print(RED + "\n[!] URL inválida." + RESET)
                input("\nEnter...")
                continue

            loading()
            data = get_ip_info(ip)

            if not data:
                print(RED + "[!] Erro na API." + RESET)
                input("\nEnter...")
                continue

            show_result(ip, data)

        elif choice == "2":
            ip = input(CYAN + "\nDigite o IP: " + RESET).strip()

            if not is_ip(ip):
                print(RED + "\n[!] IP inválido." + RESET)
                input("\nEnter...")
                continue

            loading()
            data = get_ip_info(ip)

            if not data:
                print(RED + "[!] Erro na API." + RESET)
                input("\nEnter...")
                continue

            show_result(ip, data)

        elif choice == "3":
            loading()

            ip_pub, data = get_my_ip()
            ip_local = get_local_ip()

            if ip_pub:
                print(GREEN + "\n[+] IP Público:" + RESET)
                show_result(ip_pub, data)
            else:
                print(RED + "[!] Erro IP público" + RESET)

            if ip_local:
                print(GREEN + "\n[+] IP Local:" + RESET)
                print(CYAN + ip_local + RESET)

        elif choice == "4":
            use_proxy()

        else:
            print(RED + "\n[!] Opção inválida" + RESET)

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
