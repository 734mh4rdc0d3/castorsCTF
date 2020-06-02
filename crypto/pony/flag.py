from pwn import *
from time import sleep
sleeptime = 0.2

# ascii range 32 - 126

conn = remote("chals20.cybercastors.com",14422)
sleep(sleeptime)

flag = "castorsCTF{k33p_y0ur_k3y5_53cr37_4nd_d0n7_r3u53_7h3m!"
while(True):
	for i in range(32,126):
		print(conn.recv().decode("utf-8") , flag+str(chr(i)))
		conn.send(flag+str(chr(i)))
		sleep(sleeptime)
		result = conn.recv().decode("utf-8")
		if(len(result) == 4):
			flag = flag+str(chr(i))
			break


conn.close()

