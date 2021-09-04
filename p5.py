from functools import reduce
lista = [0,1,3,1,15,9,10]

listaDoble = map(lambda x: x%2 == 0, lista)
listaPates = filter(lambda x: x%2 == 0, lista)

sumatorio = reduce(lambda x, y: x+2*y, lista)
#sumatorio = reduce(lambda x, y: x+y, range(101))

print((sumatorio))
print(list(listaDoble))
