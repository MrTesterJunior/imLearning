def normal(x):
	return x
	
def doble(x):
	return 2*x
	
def cuadrado(i):
	return i*i
	
# Función de nivel superior: Permite recibir funciones como parámetros o devolver una función
def sumaTodos(limitTo,f):
	resultado = 0
	for i in range(limitTo+1):
		resultado += f(i)
	return resultado

print(sumaTodos(3, cuadrado))
print(sumaTodos(100, int))
print(sumaTodos(100, normal))
print(sumaTodos(2, doble))
