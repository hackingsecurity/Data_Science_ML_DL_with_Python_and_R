

## nformación sobre propiedad y métodos

* print(help(list)) -> Conocer el objeto
* print(dir(list))  -> Métodos y atributos del objeto
* import inspect ; print(inspect.getmembers(list)) -> más zoom en el objeto
* print(type(10)) -> conocer el tipo de dato
* \# comentario
* 


## depurador

* import pdb    -> n(next), s(step), c(continue), p (variable), q (quit)
	* pdb.set_trace() -> Para ejecución y muestra variables


## formateo de salida

* print("hi", "wordl", sep=" - ", end="") -> sep -> separador y end -> final
* print(f" string...  {var1}, string... {var2}" ) -> {} sustituye a una variable


## Entrada

* input("Introduce valor/string")


## Tipos de datos

* listas (list)
	* l = [ "a", 1, "b", [1,2]] -> Conjunto arbitrario de valores
		* l[0] -> index a la primera posición
* Tuplas  -> inmutables
	* tupla = ("a", "b", "c") -> valores constantes y ejecución más rápida
* Diccionarios -> clave[inmutable]-valor
	* dic = { "a": [1,2,3,4], "b":"v1", "c":0}


## Operadores



### Aritméticos


* +  -> Concatenar
* <=, >, <, >=, == # Desbloquea los booleanos, usarlos con número, string
* +=, -=, *=, /=  -> operaciones


### Pertenecia

*  "T" in "Teruel"
* "u" not int "Madrid"

### Lógicos

* ( 1 < 2 or 2 < 3 )
* ( not ( 1 < 2))
* (1 < 2 and 2 < 3)


## Control de flujo


* if : elif  : else :
* for num in range(0, len(lista)):
* while num > 0 :


## Funciones 


* def name_f (arg1, arg2):


## Clases

* class Coche:
	* def \__init\__(self, arg1,arg2): -> constructora
	* def getters (self): -> mostrar campos del objeto
	* def setters(self): -> modificar campos del objeto
	* def \__str__(self): -> respresentar un objeto como cadena de texto

### Herencia

* class CocheElectrico(Coche):
	*  def \__init\__(self, arg1,arg2): -> constructora
		* super().\__init__(arg1, arg2)
	* def getter(self): -> sobre escritura de la clase padre



## Modulos (programación modular)

* Organizar código, definir funciones, clases y variables, reutilizar
* moduloX.py (nombre del fichero del módulo)
	*  import moduloX (al importar no añadimos ".py")
		* moduloX.test_func() -> hacer uso de una función
	* from moduloX import Test  as t -> invoca solo la clase del módulo y con un alias
		* t.get_nombre()

### Paquete

* Nos permite organizar los módulos en python
	* mkdir paquete
	* cd paquete
	* touch moduloY.py
	* \__init__.py -> fichero que tiene que existir en el paquete
		* \__all__  = [ 'moduloY', 'moduloX'] -> importa los modulos
	* import paquete.moduloY as m2
		* m2.test_func2()
	* from paquete.moduloY import test_func2




