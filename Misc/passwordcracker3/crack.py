import hashlib
def sha256hash(word):
	result =  hashlib.sha256(word).hexdigest()
	return result
f = open('rockyou.txt', "r")
words = f.readlines()
i = 0
for word in words:
	p = "castorsCTF{"+word[:-1]+"}"
	ans = sha256hash(p)
	if ans == "7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12":
		print("flag is "+ p)
		break
	i+=1
