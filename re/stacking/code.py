ls = ['0x63\n', '0x61\n', '0x73\n', '0x74\n', '0x6f\n', '0x72\n', '0x73\n', '0x43\n', '0x54\n', '0x46\n', '0x7b\n', '0x77\n', '0x33\n', '0x6c\n', '0x63\n', '0x30\n', '0x6d\n', '0x33\n', '0x5f\n', '0x37\n', '0x30\n', '0x5f\n', '0x72\n', '0x33\n', '0x76\n', '0x33\n', '0x72\n', '0x35\n', '0x33\n', '0x5f\n', '0x33\n', '0x6e\n', '0x36\n', '0x31\n', '0x6e\n', '0x33\n', '0x33\n', '0x72\n', '0x31\n', '0x6e\n', '0x36\n', '0x7d\n', '0x14\n', '0x00\n']
ans = ""
word = {'0': 0, '1':1,'2':2,'3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
for i in ls:
    ans += chr(word[i[2]]*16+word[i[3]])
print(ans)

