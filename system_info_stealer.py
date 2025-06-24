# system_info_stealer.py
import platform
import socket
import os

def get_system_info():
    print("[*] Collecting system info...\n")

    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except:
        hostname = "N/A"
        ip_address = "N/A"

    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Username": os.getlogin(),
        "Hostname": hostname,
        "IP Address": ip_address
    }

    for key, value in info.items():
        print(f"{key}: {value}")

    with open("system_info.txt", "w") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")

    print("\n[+] Info saved to 'system_info.txt'")

get_system_info()
