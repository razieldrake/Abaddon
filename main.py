#coding UTF-8

from kamene.all import *
import



def Traceroute():
    print('Mode traceroute')
    rep = input('Indiquez la destination finale')
    rep2 = int(input('Inqiuez le nombre de saut maximum'))
    result, nores = sr(IP(dst=rep, ttl=(1, rep2)) / TCP(), timeout=0.5)
    for emis, recu in result:
        print(emis.ttl, recu.src)
    Manual_Menu_Discovering_Mode()





def IdleHostScanning():

def rangePing(FlagManAut):
    print('demarrage du discover ping')
    range = input('Indiquer la plage d adresse ')
    result, nores = sr(IP(dst=range) / ICMP(), timeout=0.5)
    for elem in result:
        if elem[1].type == 0:
            print(elem[1].src + ' existe')
    Manual_Menu_Discovering_Mode()


def SingleHostPing(FlagManAut):
    print("Signle Host Ping started")
    dest = input('Indiquer l ip cible')
    result = sr1(IP(dst=dest) / ICMP(), timeout=0.5)
    result[0][0].show()
    if result.type == 0:  # 0 === echo-reply
        print(result.src + ' existe')
    Manual_Menu_Discovering_Mode()

def ICMP_Sweep():
    network = input('Entrer une plage d adresse type x.x.x.x /yy')
    # construit une liste d adresse du reseau, initialise le counter hote
    addresses = netaddr.IPNetwork(network)
    liveCounter = 0
    # envoi une requete ICMP et attend une réponse
    for host in addresses:
        if (host == addresses.network or host == addresses.broadcast):
            # passe le réseau et le broadcast
            continue

        resp = sr1(IP(dst=str(host)) / ICMP(), timeout=0.5, verbose=0)

        if resp is None:
            print(host, 'ne répond pas')
        elif (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
        ):
            print(host, 'bloque ICMP')
        else:
            print(host, ' est en ligne ')
            liveCounter += 1

    print('{}/{} hotes sont en ligne.'.format(liveCounter, addresses.size))
    Manual_Menu_Discovering_Mode()


def Automatic_Discovering_Mode():

def Manual_Menu_Discovering_Mode():
    print(" Manual Network Discovering Mode")
    print("1- ICMP sweep")
    print("2- Single Host ping Ping")
    print("3- Rrange Ping")
    print("4- Idle Host Scanning")
    print("5- Traceroute")

    choice = input("Please select your choice")
    if (choice==1):
        ICMP_Sweep()
    if (choice == 2)

def Menu_Discovering_mode():
    print("Network Discovering mode")
    print("1- Manual Mode")
    print("2- Automatic Mode")

    rep = input("Automatic or Manual mode?")
    if(rep==1):
        Manual_Menu_Discovering_Mode()
    if(rep==2):
        Automatic_Discovering_Mode()


def Selection_Screen():
    print("1 - Discovering Mode")
    print("2 - Scanning Mode")
    print("3 - Pre-Attack Mode")
    print("4 - Attack Mode")
    print("5 - Report Mode")
    print("6 - Forge Mode")
    print("999 - Exit")
    choice = input("Veuillez selectionnez votre choix")

    if (choice==999):
        sys.exit(0)

print ("********************************************************")
print ("********************************************************")
print ("-------------------------ABADDON------------------------")
print ("********************************************************")
print ("*******************created by : R.A.D.******************")
print ("********************************************************")
print ("******************************************Happy Chaoting")

Selection_Screen()