# Abstracción
class Animal:

    def hacer_sonido(self):
        pass

    def nombre(self):
        pass

    def edad(self):
        pass


# Encapsulamiento
class Mascota(Animal):

    def __init__(self, nombre, edad):
        self._nombre = nombre       # Atributos encapsulados
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa.")


# Herencia y Polimorfismo
class Chancho(Mascota):

    def hacer_sonido(self):
        return "Oink Oink"

    def nombre(self):
        return f"Chancho se llama {self.get_nombre()}"

    def edad(self):
        return f"Edad: {self.get_edad()} años"


class Gallo(Mascota):

    def hacer_sonido(self):
        return "Kikirikí"

    def nombre(self):
        return f"Gallo se llama {self.get_nombre()}"

    def edad(self):
        return f"Edad: {self.get_edad()} años"


# Programa principal
if __name__ == "__main__":

    chancho = Chancho("Pippo", 7)
    gallo = Gallo("Spirit", 3)

    animales = [chancho, gallo]

    for animal in animales:
        print(animal.nombre())
        print(animal.edad())
        print("Sonido:", animal.hacer_sonido())
    
echo "# Guevara-Programacion-Orientada-a-Objetos" >> README.md 
git init 
git add README.md 
git commit -m "primer commit" 
git branch -M main 
git remote add origin https://github.com/Carlos29-gu/Guevara-Programacion-Orientada-a-Objetos.git
 git push -u origin main
         
                  
                  

    
    



    
