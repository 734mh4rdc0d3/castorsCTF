from pwn import *
import time

sleeptime = 0.1

arith = remote("chals20.cybercastors.com", 14429)
print(arith.recv())
arith.send("\r")
time.sleep(sleeptime)

digits = {
	"zero":0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	"+":"+",
	"-":"-",
	"*":"*",
	"//":"//",
	"1":1,
	"2":2,
	"3":3,
	"4":4,
	"5":5,
	"6":6,
	"7":7,
	"8":8,
	"9":9,
	"0":0,
	"divided-by":"//",
	"minus": "-",
	"multiplied-by": "*",
	"plus":"+"
}

while(True):
	a = str(arith.recv())
	print(a)
	a = a[10:][:-5]
	a = a.split(" ")
	exp = ""
	for part in a:
		exp += str(digits[part])
	result = eval(exp)
	time.sleep(sleeptime)
	arith.send(str(result)+"\n")
	time.sleep(sleeptime)
	a = arith.recv()
	print(a)
	if("Correct answer" not in str(a)):
		break

arith.close()