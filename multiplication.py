
a = 9876	
b = 1234

if a<b:
	a,b = b,a

a = str(a)
b = str(b)

M = []

m = 0

sumy = []

for i in range(len(b)):
	x = int(b[-1-i])
	N = []
	for y in a[::-1]:
		y = int(y)
		z = x*y + m
		m = z//10
		n = z%10
		M += [m]
		N += [str(n)]
	if m>0:
		sumy += [[str(m)]+N[::-1]]
	else:
		sumy += [N[::-1]]
	m = 0

max_length = max([len(sumy[i])+i for i in range(len(sumy))])

suma = []

for i in range(max_length):
	x = 0
	for j in range(len(sumy)):
		s = sumy[j] + [0]*j
		if i >= len(s):
			continue
		x += int(s[-1-i])
	x += m
	m = x//10
	x %= 10
	suma += [str(x)]

if m>0:
	suma += [str(m)]

suma = suma[::-1]

max_length = max([len(a), max_length, len(suma)])

	#["0"]*(max_length-len(a))+a))

print(r"\begin{minipage}[t]{0.3\linewidth}\flushright")
print(r"\begin{equation*}\begin{array}{c}")
print(r"\phantom{\times"+ "".join(['0']*(max_length-len(a)))+"}"+a+r"\\")
print(r"\underline{\times\phantom{"+ "".join(['0']*(max_length-len(b)))+"}"+b+r"}\\")
for i in range(len(sumy)):
	x = "".join(sumy[i])
	if i < len(sumy)-1:
		print(r"\phantom{+"+ "".join(['0']*(max_length-len(x)-i))+"}"+x+"".join(["\phantom0"]*i)+r"\\")
	else:
		print(r"\underline{+"+ "\phantom{"+"".join(['0']*(max_length-len(x)-i))+"}"+x+"".join([r"\phantom0"]*i)+r"}\\")


print(r"\phantom{+}"+"".join(suma))
print(r"\end{array}\end{equation*}")
print(r"\end{minipage}")

Num = 3+len(b)

MM = []
for m in M:
	if m==0:
		continue
	MM += [m]

M = MM

mNum = len(M)

for i in range(len(M)//Num+1):
	print(r"\begin{minipage}[t]{0.1\linewidth}\flushleft\begin{align*}")
	K = min([mNum-i*Num, Num])
	for j in range(K):
		m = i*Num+j
		if m >= mNum:
			break
		m = M[m]
		if m == 0:
			continue
		if j < K-1:
			print(m,r"\\")
		else:
			print(m)
	print(r"\end{align*}\end{minipage}")

# a, b , sumy, suma
