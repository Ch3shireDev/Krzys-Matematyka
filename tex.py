
def TexBegin(x = 0.05):
	print(r"\begin{minipage}[t]{"+str(x)+r"\linewidth}")
	print(r"\begin{align*}\begin{array}{c}")

def TexEnd():	
	print(r"\end{array}\end{align*}")
	print(r"\end{minipage}")

def PhantomBegin():
	Tex("phantom")

def Tex(x):
	print("\\"+x+"{")

def End():
	print("}")

def Blank():
	print(r"\textvisiblespace")