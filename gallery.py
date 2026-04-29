import os
import time
import random

# Color codes
R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
B = "\033[1;94m"
C = "\033[1;96m"
P = "\033[1;95m"
W = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(G + """
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ 
███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
""" + W)
    print(P + "        WORLD VICTORY  - GALLERY BREACH X\n" + W)

def loading(text, delay=0.05):
    print(Y + text + W)
    for i in range(30):
        print(C + "█" + W, end="", flush=True)
        time.sleep(delay)
    print("\n")

def fake_files():
    print(R + "[+] Scanning Gallery...\n" + W)
    time.sleep(1)

    for i in range(12):
        print(G + f"[IMG_{random.randint(1000,9999)}.jpg] → Loaded" + W)
        time.sleep(0.2)

    print("\n" + B + "[+] Accessing Hidden Files...\n" + W)
    time.sleep(1)

    for i in range(8):
        print(Y + f"[VID_{random.randint(1000,9999)}.mp4] → Decrypted" + W)
        time.sleep(0.2)

def download():
    print("\n" + G + "[+] Downloading Files...\n" + W)
    for i in range(101):
        print(C + f"Downloading: {i}%" + W, end="\r")
        time.sleep(0.03)
    print("\n" + G + "[✔] Download Complete!\n" + W)

def main():
    clear()
    banner()
    time.sleep(1)

    print(R + "[+] Initializing Secure Server..." + W)
    time.sleep(1)
    print(Y + "[+] Bypassing Encryption..." + W)
    time.sleep(1)
    print(B + "[+] Connecting to Target Device...\n" + W)
    time.sleep(1)

    number = input(C + "Enter Target Number: " + W)

    print("\n" + R + f"[✔] Target Locked: {number}" + W)
    time.sleep(1)

    loading("[+] Injecting Payload...")
    loading("[+] Accessing Storage...")

    fake_files()
    download()

    print(P + "\n[✔] FULL GALLERY ACCESS GRANTED 😈" + W)
    print(R + "WORLD  VICTORY - ELITE ACCESS\n" + W)

if __name__ == "__main__":
    main()