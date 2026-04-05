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

ip_antes = None

def clear():
    os.system("clear")

def anonymous_ascii():
    # Boneco anônimo no topo do menu, sem cortar
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

def get_my_ip():
    try:
        res = requests.get("https://ipinfo.io/json", timeout=5)
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

def open_vpn():
    global ip_antes

    print(YELLOW + "\n[~] Salvando IP atual..." + RESET)
    ip_antes, _ = get_my_ip()

    print(GREEN + f"[+] IP atual: {ip_antes}" + RESET)
    print(YELLOW + "\n[~] Abrindo VPN..." + RESET)

    url = "https://protonvpn.com/download"
    os.system(f'termux-open-url "{url}"')

    print(CYAN + "\n[!] Ative a VPN e volte aqui depois." + RESET)

def check_vpn():
    global ip_antes

    if not ip_antes:
        print(RED + "\n[!] Use a opção de VPN primeiro!" + RESET)
        return

    loading()
    ip_depois, data = get_my_ip()

    print(GREEN + "\n[+] IP atual:" + RESET)
    show_result(ip_depois, data)

    print(YELLOW + "\n[~] Comparação:" + RESET)

    if ip_depois != ip_antes:
        print(GREEN + f"[✔] IP mudou: {ip_antes} → {ip_depois}" + RESET)
    else:
        print(RED + "[✘] IP NÃO mudou (VPN pode não estar ativa)" + RESET)

def main():
    while True:
        clear()
        anonymous_ascii()
        banner()

        print(CYAN + "[1] Consultar URL")
        print("[2] Consultar IP")
        print("[3] Ver Meu IP (público e local)")
        print("[4] Ativar VPN (VPN Free)")
        print("[5] Verificar mudança de IP")
        print("[6] Sair/Exit\n" + RESET)

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
            show_result(ip, data)

        elif choice == "2":
            ip = input(CYAN + "\nDigite o IP: " + RESET).strip()

            if not is_ip(ip):
                print(RED + "\n[!] IP inválido." + RESET)
                input("\nEnter...")
                continue

            loading()
            data = get_ip_info(ip)
            show_result(ip, data)

        elif choice == "3":
            loading()
            ip_pub, data = get_my_ip()
            ip_local = get_local_ip()

            print(GREEN + "\n[+] IP Público:" + RESET)
            show_result(ip_pub, data)

            print(GREEN + "\n[+] IP Local:" + RESET)
            print(CYAN + str(ip_local) + RESET)

        elif choice == "4":
            open_vpn()

        elif choice == "5":
            check_vpn()

        elif choice == "6":
            confirm = input(YELLOW + "\nTem certeza que deseja sair? (s/n): " + RESET).lower()

            if confirm == "s":
                print(YELLOW + "\n[~] Finalizando..." + RESET)
                time.sleep(0.5)
                print(GREEN + "[+] Encerrando IP TRACKER..." + RESET)
                time.sleep(1)
                break
            else:
                print(CYAN + "\n[~] Retornando ao menu..." + RESET)
                time.sleep(1)

        else:
            print(RED + "\n[!] Opção inválida" + RESET)

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
