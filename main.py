from multiplication import *
# from division import *
from random import randint

# TexDivision(921,4)

def Math(ar, br, cr, dr, n=6):
	for i in range(n):
		x, y = "0", "0"
		while '0' in x or '0' in y:	
			a = randint(ar,br)
			b = randint(cr,dr)
			x, y = str(a), str(b)
		MultBlank(a,b)
		TexMultiplication(a,b)
		print("")

Math(10,99,10,99)
Math(10,99,100,999)
Math(100,999,100,999)
Math(1000,9999,1000,9999)