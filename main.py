import requests
import socket
import re
import webbrowser

def is_ip(ip):
    return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip)

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

def get_location(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()
        return data.get("loc"), data
    except:
        return None, None

def main():
    user_input = input("Digite IP ou domínio: ").strip()

    if is_ip(user_input):
        ip = user_input
    else:
        ip = resolve_domain(user_input)
        if not ip:
            print("Erro ao resolver domínio")
            return

    loc, data = get_location(ip)

    if not loc:
        print("Erro ao pegar localização")
        return

    lat, lon = loc.split(",")

    link = f"https://www.google.com/maps?q={lat},{lon}"

    print(f"\nIP: {ip}")
    print(f"Cidade: {data.get('city')}")
    print(f"País: {data.get('country')}")
    print(f"\nMapa: {link}")

    webbrowser.open(link)

if __name__ == "__main__":
    main()
