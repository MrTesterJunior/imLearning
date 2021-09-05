
class Perro():
	
	def __init__(self, n, p, e):
		self.nombre=n
		self.peso=p
		self.edad=e

	def __str__(self):
		return "Perro con nombre: %s" % self.nombre
		
	def __float__(self):
		return self.peso
	
	def ladrar(self):
		if self.peso >= 8:
			print("%s: WOOF WOOF" % self.nombre)
		else:
			print("%s: Woof" % self.nombre)


# La herencia se define poniendo entre () la clase padre
class PerroAsistencia(Perro):
	
	def __init__(self, nombre,edad,peso,amo):
		Perro.__init__(self, nombre, peso, edad)
		self.amo = amo
		self.__trabajando = False
		
	def __str__(self):
		return "Perro de asistencia de %s" % self.amo
	
	def pasear(self):
		print("%s: Ayudo a %s a pasear" % (self.nombre, self.amo))
		
	def ladrar(self):
		if self.trabajando:
			print("wif")
		else:
			Perro.ladrar(self)

	def trabajando(self, valor=None):
		if valor==None:
			return self.__trabajando
		else:
			self.__trabajando = valor



bryan = PerroAsistencia("Bryan",10,3,"Peter Griffin")
print(bryan.amo)
bryan.ladrar()


bryan.pasear()
bryan.ladrar()
bryan.pasear()
bryan.ladrar()
