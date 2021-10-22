print("Дано три числа. Если ровно два из них  меньше  5, то вывести yes, иначе вывести no.")

try:
   a = int(input("Введите первое число = "))
   b = int(input("Введите второе число = "))
   c = int(input("Введите третье число = "))
except:
   print("Tek san zhazynyz")
   exit()

def aik(a):
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
aik(a)
def paka():
	print("Good bye!")
paka()
