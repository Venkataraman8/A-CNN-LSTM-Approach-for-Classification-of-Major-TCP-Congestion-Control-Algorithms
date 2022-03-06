import sys

f = open("TcpVeno-cwnd.data", "r")
s = f.read()
 
cwnd = s.split('\n')
fcwnd = []

sys.stdout = open("TcpVeno_split.txt", "w") 
 
def getVal(s):
    s = s[::-1]
    val = 0
    p10 = 1
 
    for x in s:
        val += int(x)*p10
        p10 *= 10
 
    return val
 
for x in cwnd:
    fcwnd.append(getVal(x.split(' ')[-1]))
 
cwnd = fcwnd
 
fcwnd = []
clist = []
clist.append(getVal('0'))
i = 1
 
while i < len(cwnd):
    if clist[-1] <= cwnd[i]:
        clist.append(cwnd[i])
    else:
        fcwnd.append(clist)
        clist = []
        clist.append(cwnd[i])
    i += 1
 
print((fcwnd))
 
sys.stdout.close()