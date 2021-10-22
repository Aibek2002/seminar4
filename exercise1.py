print("Дано три числа. Если ровно два из них  меньше  5, то вывести yes, иначе вывести no.")

try:
   q = int(input("Введите первое число = "))
   w = int(input("Введите второе число = "))
   e = int(input("Введите третье число = "))
except:
   print("Tek san zhazynyz")
   exit()

def aik(a,b,c):
	if (a<5) and (b<5) and (c>5):
		print("-yes-")
	elif (b<5) and (c<5) and (a>5):
		print("-yes-")
	elif (a<5) and (c<5) and (b>5):
		print("-yes-")
	else:
		print("-no-")
def zhauap():
	print("ОТВЕТ", )
zhauap()
aik(q,w,e)
def paka():
	print("Good bye!")
paka()
