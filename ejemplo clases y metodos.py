class Persona:
	def saludo_general(self):
		return "Hola persona"

class Estudiante(Persona):
	def __init__(self,nombre,edad):
		self.nombre=nombre
		self.edad=edad

	def hola(self):
		return "Mi nombre es %s \n" % self.nombre


e=Estudiante("Arturo",25)
print e.saludo_general()
print e.hola()

class Auto:
	name=""
	kind=""
	color=""
	value=10.01251
	_numero_serie="adsfsvds"
	def description(self):
		desc="%s es un Auto color %s y de tipo %s. Vale $%.2f"(self.nombre,self.color,self.kind,self.value)
		return desc

car1=Auto()
car1.name="nombreauto"
car1.color="tornasolado"
car1.kind="alguntipo"
car1.value=222.3411

print car1.description()
