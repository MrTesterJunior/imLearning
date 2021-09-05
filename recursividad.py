
def countdown(numero):
	print(numero)
	if numero > 0:
		countdown(numero-1)

def sumatorio(n):
	if n == 0:
		return 0
	return n + sumatorio(n-1)


		
#countdown(10)
print(sumatorio(5))
