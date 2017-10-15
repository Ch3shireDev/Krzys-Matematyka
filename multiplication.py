from tex import *

def TexMultiplication(a, b):
	if a<b:
		a, b = b, a

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
		if m > 0:
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

	TexBegin(0.3)
	PhantomBegin()
	print(r"\times"+ "".join(['0']*(max_length-len(a))))
	End()
	print(a+r"\\")
	Tex("underline")
	print(r"\times")
	k = max_length-len(b)
	if k > 0:
		Tex("phantom")
		print("".join(['0']*k))
		End()
	print(b)
	print("}"+r"\\")

	for i in range(len(sumy)):
		x = "".join(sumy[i])
		if i < len(sumy)-1:
			k = max_length-len(x)-i
			if k > 0:
				Tex("phantom")
				print("+"+ "".join(['0']*k))
				End()
			print(x)
			print(r"".join([r"\phantom0"]*i)+r"\\")
		else:
			Tex("underline")
			print("+")
			k = max_length-len(x)-i
			if k > 0:
				Tex("phantom")
				print("".join(['0']*k))
				End()

			print(x)
			print(r"".join([r"\phantom0"]*i))
			End()
			print(r"\\")


	print(r"\phantom{+}")
	print("".join(suma))
	TexEnd()

	Num = 3+len(b)

	MM = []
	for m in M:
		if m==0:
			continue
		MM += [m]

	M = MM

	mNum = len(M)

	for i in range(len(M)//Num+1):
		TexBegin()
		K = min([mNum-i*Num, Num])
		for j in range(K):
			m = i*Num+j
			if m >= mNum:
				break
			m = M[m]
			if m == 0:
				continue
			print(m)
			if j < K-1:
				print(r"\\")
		TexEnd()

	# print("")

def MultBlank(a, b):
	if a<b:
		a, b = b, a

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
		if m > 0:
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

	TexBegin(0.3)
	PhantomBegin()
	print(r"\times"+ "".join(['0']*(max_length-len(a))))
	End()
	print(a+r"\\")
	Tex("underline")
	print(r"\times")
	k = max_length-len(b)
	if k > 0:
		Tex("phantom")
		print("".join(['0']*k))
		End()
	print(b)
	print("}"+r"\\")

	for i in range(len(sumy)):
		x = "".join(sumy[i])
		if i < len(sumy)-1:
			k = max_length-len(x)-i
			if k > 0:
				Tex("phantom")
				print("+"+ "".join(['0']*k))
				End()
			# print(x)
			for a in str(x):
				Blank()
			print(r"".join([r"\phantom0"]*i)+r"\\")
		else:
			Tex("underline")
			print("+")
			k = max_length-len(x)-i
			if k > 0:
				Tex("phantom")
				print("".join(['0']*k))
				End()

			# print(x)
			for a in str(x):
				Blank()
			print(r"".join([r"\phantom0"]*i))
			End()
			print(r"\\")


	print(r"\phantom{+}")
	# print("".join(suma))
	for a in suma:
		Blank()
	TexEnd()

	Num = 3+len(b)

	MM = []
	for m in M:
		if m==0:
			continue
		MM += [m]

	M = MM

	mNum = len(M)

	for i in range(len(M)//Num+1):
		TexBegin()
		K = min([mNum-i*Num, Num])
		for j in range(K):
			m = i*Num+j
			if m >= mNum:
				break
			m = M[m]
			if m == 0:
				continue
			# print(m)
			Blank()
			if j < K-1:
				print(r"\\")
		TexEnd()

	# print("")