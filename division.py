from tex import *

def number(tab):
	if type(tab) is int:
		return tab
	else:
		return int("".join([str(x) for x in tab]))

def TexDivision(a, b):
	div = str(a//b)
	rest = str(a%b)
	aa = str(a)
	bb = str(b)
	print(div + " r. "+rest)
	l = len(div)+4+len(rest)
	print("".join(["_"]*l))
	print(a, end="")
	print("".join([" "]*(l-len(aa))), end="")
	print(": " + bb)

	x = aa[0]
	i = 1


	x = [x]
	while number(x) < number(b) and i < len(aa):
		x += aa[i]
		i += 1
	x = number(x)
	y = x % b
	print(x-y)
	x = y

	x = [x]
	while number(x) < number(b) and i < len(aa):
		x += aa[i]
		i += 1
	x = number(x)
	y = x % b
	print(x)
	
	y = x % b
	print(x-y)
	x -= y
	x = [x]
	while number(x) < number(b) and i < len(aa):
		x += aa[i]
		i += 1
	x = number(x)
	print(x)


TexDivision(987, 22)

