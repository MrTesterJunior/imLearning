
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

pix = Perro("Pix", 5.4, 8)
pix.peso = 5.4

manolo = Perro("Manolo", 12, 3)
pix.ladrar()
manolo.ladrar()

pix.nombre="PIX"


