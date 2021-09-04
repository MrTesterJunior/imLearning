
def maximo(*l):
	if len(l) == 0:
		return 0
	m = l[0]
	for element in l:
		if element > m:
			m = element
	
	return m
	
def minimo(*l):
	if len(l) == 0:
		return 0
	m = l[0]
	for element in l:
		if element < m:
			m = element
	
	return m

def media(*l):
	if len(l) == 0:
		return 0
	m = 0
	for element in l:
		m += element
	
	return m/len(l)

funciones = {
	'max': maximo,
	'min': minimo,
	'med': media
}


def returnF(nombre):
	return funciones.get(nombre)
	
	
#print(maximo(1,4,7,8,3,6,123,-1,16,100,121,18))
#print(minimo(1,4,7,8,3,6,123,-1,16,100,121,18))
#print(media(1,4,7,8,3,6,123,-1,16,100,121,18))

#print(maximo(1,3,-1,15,9))
#print(minimo(1,3,-1,15,9))
#print(media(1,3,-1,15,9))

print(returnF("max")(1,4,5,6))
print(returnF("min")(1,4,5,6))
print(returnF("med")(1,4,5,6))
