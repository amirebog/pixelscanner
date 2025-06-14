import socket
import ssl
import json
import os
import time
from datetime import datetime

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
    2222: "SSH-ALT"
}

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def logo():
    print("\033[96m")
    print("██████╗ ██╗██╗     ███████╗██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗")
    print("██╔══██╗██║██║     ██╔════╝██║ ██╔╝██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║")
    print("██████╔╝██║██║     █████╗  █████╔╝ █████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║")
    print("██╔═══╝ ██║██║     ██╔══╝  ██╔═██╗ ██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║")
    print("██║     ██║███████╗███████╗██║  ██╗███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║")
    print("╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝")
    print("                            \033[90mby Pixel Haven Dev\033[0m\n")

def get_ip_info(ip):
    print("[*] Getting IP info...")
    try:
        raw = os.popen(f"curl -s https://ipinfo.io/{ip}/json").read()
        data = json.loads(raw)
        for k in ["ip", "city", "region", "country", "org", "loc"]:
            if k in data:
                print(f"   \033[94m{k.title():>8}:\033[0m {data[k]}")
        if "loc" in data:
            print(f"   \033[92mGoogle Maps:\033[0m https://maps.google.com?q={data['loc']}")
        return data
    except:
        print("   [!] Could not fetch IP info.")
        return {}

def check_ssl(ip, port):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=ip) as s:
            s.settimeout(2)
            s.connect((ip, port))
            return True
    except:
        return False

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1.5)
        s.connect((ip, port))
        banner = ""
        try:
            s.send(b"Hello\r\n")
            banner = s.recv(1024).decode(errors="ignore").strip()
        except:
            pass
        s.close()
        ssl_ok = check_ssl(ip, port) if port in [443, 8443] else False
        return {
            "port": port,
            "ssl": ssl_ok,
            "banner": banner
        }
    except:
        return None

def scan_range(ip, ports_to_scan):
    results = []
    for port in ports_to_scan:
        result = scan_port(ip, port)
        if result:
            print(f"\033[92m[OPEN] {port:<5}\033[0m {'[SSL]' if result['ssl'] else ''}")
            if result['banner']:
                print(f"       \033[90mBanner:\033[0m {result['banner']}")
            results.append(result)
    return results

def menu():
    clear()
    logo()
    print("Menu:")
    print("1) Scan common remote service ports (SSH, FTP, RDP, etc.)")
    print("2) Scan all ports (1-65535)")
    print("3) Show IP information")
    print("4) Exit\n")

def main():
    target = ""
    ip_info = {}

    while True:
        menu()
        choice = input("Choose an option: ").strip()
        clear()

        if choice == "1":
            if not target:
                target = input("Enter target IP or domain: ").strip()
                ip_info = get_ip_info(target)
            print("\n[Scanning common remote ports...]\n")
            for port, service in common_ports.items():
                res = scan_port(target, port)
                if res:
                    print(f"\033[92m[OPEN] {port:<5} {service}\033[0m {'[SSL]' if res['ssl'] else ''}")
                    if res['banner']:
                        print(f"       \033[90mBanner:\033[0m {res['banner']}")
                else:
                    print(f"\033[91m[CLOSED] {port:<5} {service}\033[0m")
            input("\nPress Enter to continue...")

        elif choice == "2":
            if not target:
                target = input("Enter target IP or domain: ").strip()
                ip_info = get_ip_info(target)
            print("\n[Scanning all ports 1-65535...]\n")
            results = scan_range(target, range(1, 65536))
            print(f"\nScan complete. {len(results)} open ports found.")
            input("\nPress Enter to continue...")

        elif choice == "3":
            if not target:
                target = input("Enter target IP or domain: ").strip()
                ip_info = get_ip_info(target)
            print("\n[IP Information]\n")
            if ip_info:
                for k,v in ip_info.items():
                    print(f"{k.title()}: {v}")
            else:
                print("No info available.")
            input("\nPress Enter to continue...")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
