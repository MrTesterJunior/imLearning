from functools import reduce
lista = [0,1,3,1,15,9,10]

listaDoble = map(lambda x: x%2 == 0, lista)
listaPates = filter(lambda x: x%2 == 0, lista)

sumatorio = reduce(lambda x, y: x+2*y, lista)

#sumatorio = reduce(lambda x, y: x+y, range(101))

print((sumatorio))
print(list(listaDoble))

lista = [1,2,3,4]

def sumatorioClasico(lista):
	resultado = 0
	for valor in lista:
		resultado += valor
	return resultado
	
def sumatorioClasicoDoble(lista):
	resultado = 0
	for valor in lista:
		resultado += valor*2
	return resultado

sumatorio = reduce(lambda x,y: x + y, lista)
sumatorioDobles = reduce(lambda x,y: x + 2*y, lista)

print(sumatorio)
print(sumatorioDobles)
print(sumatorioClasico(lista))
print(sumatorioClasicoDoble(lista))
