# python_poo
introduccion a la programacion orientada en python

## ¿ por que aprender poo ?

imagina que quieres crear un videojuego. Tiene guerreros, magos, dragones... cada uno con sus propios puntos de vida, ataques y habilidades. ¿ como los organizo en codigo sin repetir todo una y otra vez ?

- La **programacion orientada a objetos (poo)** es la respuesta. en lugar de escribir instrucciones sueltas, modelas el mundo real con *objetos* que tiene caracteristicas y comportamiento. es la forma en la que estan construidos la malloria de los programas profesionales del mundo

![alt text](Gemini_Generated_Image_z4vg1hz4vg1hz4vg.png)

## clase y objeto

- una clase es un tipo de gato cuyas variables se llaman objetos o instancias.

- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio "objeto" del mundo real.

- las clases estan compuestas por dos elementos:
     - **Atributos:** informacion que almacena la clase. 
     - **Metodos:** operaciones que pueden realizarse con la clase.

## Definicion de una clase en python 

```
python 

class Nombreclase:

    def_init_(self,variable1,variable2):
     self.atributo1 = valor1
     self.atributo2 = valor2

    def nombremetodo(Self):
        bloquecodigo


```

- `class`: palabra reservada en python para definir una clase
-  ` Ǹombreclas ` : nombre de la clase que se quiere crear.
- ` def `: palabras reservada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ajecuta la primera vez que una clase) como los diferentes metodos que tiene.
- ` _init `: palabra reservada en python para definir el metodo constructor de la clase. El metodo ` _init_ ` es lo primero que se ejecuta cuando creas una objeto de una clase.
- `(self, variablex) ` : parametros del constructor de la clase. El parametro `self` es obligatorio y despues puede tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.
- ` self.AtributoX` : forma de utilizacion y acceso a los atributos de la clase.
- `nombreMetodo ` : mombre del metodo de la clase.
- `self` : parametros del metodo. el parametro `self`es obligatorio y despues puedes tener tantos parametros `self ` es obligatorio y puedes  tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.
- ` bloquecodigo ` : instrucciones  que ejecutara el metodo

**Al definir una tenga en cuenta:**
- puedes definir tantos atributos como necesites.
- puedes definir tantos metodos como nesesites.
- puedes definir tantos parametros en el constructor y en los metodos como necesites.