#Poo
#=========

class Ropa:

    def __init__(self, marca, talla, color):
        self._marca = marca
        self._talla = talla
        self._color = color

    def get_marca(self):
        return self._marca

    def get_talla(self):
        return self._talla

    def get_color(self):
        return self._color

    def set_marca(self, marca):
        self._marca = marca

    def set_talla(self, talla):
        if talla >= 1:
            self._talla = talla
        else:
            print("La talla ingresada es incorrecta")


class Ropa1(Ropa):

    def diseño(self):
        return "Diseño: Traje Formal"

    def tipo_ropa(self):
        return "Tipo de ropa: Hombre"

    def marca(self):
        return f"Marca: {self.get_marca()}"

    def talla(self):
        return f"Talla: {self.get_talla()}"

    def color(self):
        return f"Color: {self.get_color()}"


class Ropa2(Ropa):

    def tipo_ropa(self):
        return "Tipo de ropa: Mujer"

    def diseño(self):
        return "Diseño: Vestido"

    def marca(self):
        return f"Marca: {self.get_marca()}"

    def talla(self):
        return f"Talla: {self.get_talla()}"

    def color(self):
        return f"Color: {self.get_color()}"


def main():
    ropa_h = Ropa1("Nike", 40, "Negro")
    ropa_m = Ropa2("Zara", 38, "Rojo")

    print("ROPA1")
    print(ropa_h.tipo_ropa())
    print(ropa_h.diseño())
    print(ropa_h.marca())
    print(ropa_h.talla())
    print(ropa_h.color())

    print("ROPA2")
    print(ropa_m.tipo_ropa())
    print(ropa_m.diseño())
    print(ropa_m.marca())
    print(ropa_m.talla())
    print(ropa_m.color())


# Ejecutar programa
main()
