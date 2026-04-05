#!/usr/bin/env python3
import requests, socket, re, os, time, sys, webbrowser

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

ip_antes = None

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def anonymous_ascii():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⣤⣤⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠿⠿⠿⠟⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⡛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⣋⡉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣧⠸⣿⣶⣶⠖⠒⢲⣶⣶⡿⠃⢸⣿⣿⣿⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠐⠛⠛⠿⢿⣿⣿⣧⡀⠈⠀⠀⠀⠀⠈⠁⢀⣴⣿⣿⣿⠿⠿⠟⠛⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣅⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣷⣄⡀⢠⣿⣿⣿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀
""")

def banner():
    print(f"""{RED}
██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
             ☢︎ Powered by Suprateam  
{RESET}""")

def clean_input(user_input):
    user_input = user_input.strip()
    user_input = user_input.replace("http://", "").replace("https://", "").replace("www.", "")
    return user_input.split("/")[0]

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
        return {}

def get_my_ip():
    try:
        res = requests.get("https://ipinfo.io/json", timeout=5)
        data = res.json()
        return data.get("ip"), data
    except:
        return None, {}

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
        print(YELLOW + f"[+] Localização: {lat}, {lon}" + RESET)
        print(GREEN + f"[+] Mapa: https://www.google.com/maps?q={lat},{lon}" + RESET)

def open_vpn():
    global ip_antes
    ip_antes, _ = get_my_ip()
    print(GREEN + f"[+] IP atual: {ip_antes}" + RESET)
    print(YELLOW + "[~] Abrindo Proton VPN..." + RESET)
    webbrowser.open("https://protonvpn.com/download")

def check_vpn():
    global ip_antes
    if not ip_antes:
        print(RED + "\n[!] Use a opção VPN primeiro!" + RESET)
        return
    loading()
    ip_depois, data = get_my_ip()
    show_result(ip_depois, data)
    if ip_depois != ip_antes:
        print(GREEN + f"[✔] IP mudou: {ip_antes} → {ip_depois}" + RESET)
    else:
        print(RED + "[✘] IP NÃO mudou" + RESET)

def main():
    while True:
        clear()
        anonymous_ascii()
        banner()
        print(CYAN + "[1] Consultar URL")
        print("[2] Consultar IP")
        print("[3] Ver Meu IP (público e local)")
        print("[4] Abrir VPN (Proton VPN)")
        print("[5] Verificar mudança de IP")
        print("[6] Sair/exit\n" + RESET)
        choice = input("Escolha: ")

        if choice == "1":
            url = clean_input(input(CYAN + "Digite a URL: " + RESET))
            ip = resolve_domain(url)
            if ip: show_result(ip, get_ip_info(ip))
        elif choice == "2":
            ip = input(CYAN + "Digite o IP: " + RESET)
            if is_ip(ip): show_result(ip, get_ip_info(ip))
        elif choice == "3":
            ip_pub, data = get_my_ip()
            print(GREEN + "[+] IP Público:" + RESET)
            show_result(ip_pub, data)
            print(GREEN + "[+] IP Local:" + RESET + str(get_local_ip()))
        elif choice == "4":
            open_vpn()
        elif choice == "5":
            check_vpn()
        elif choice == "6":
            break
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
