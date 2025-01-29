class CompraBoletos:
    def _init_(self):
        self.num_boletos = 0
        self.nombre_persona = ""
        self.num_personas = 0
        self.usa_tarjeta_cineco = False

    def calcular_costo(self):
        valor_base = 12
        costo_total = self.num_boletos * valor_base

        # Descuentos por cantidad de boletos
        if self.num_boletos > 5:
            costo_total *= 0.85  # 15% de descuento
        elif 3 <= self.num_boletos <= 5:
            costo_total *= 0.90  # 10% de descuento
        # Hasta 2 boletos no hay descuento (se mantiene igual)

        # Descuento adicional por usar tarjeta CINECO
        if self.usa_tarjeta_cineco:
            costo_total *= 0.90  # 10% adicional de descuento

        return costo_total

    def save_to_file(self, filename):
        with open(filename, 'a') as f:  # Modo 'a' para no sobrescribir
            f.write("-------- Nueva Compra --------\n")
            f.write(f"Nombre persona: {self.nombre_persona}\n")
            f.write(f"Numero de boletos: {self.num_boletos}\n")
            f.write(f"Numero de personas: {self.num_personas}\n")
            f.write(f"Tarjeta CINECO: {'Si' if self.usa_tarjeta_cineco else 'No'}\n")
            f.write(f"Costo total: ${self.calcular_costo():.2f}\n")
            f.write("\n")  

    def get_datos_compra(self, repetir=False):
        """
        Obtiene los datos de la compra. Si repetir=True, no se pide el nombre.
        """
        if not repetir:  # Solo pedir el nombre al principio
            self.nombre_persona = input("Ingrese el nombre del cliente que realiza la compra: ")
        
        while True:
            try:
                self.num_personas = int(input("Ingrese el número de personas acompañantes (incluyéndose): "))
                if self.num_personas < 1:
                    print("Debe haber al menos una persona.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número válido.")

        while True:
            try:
                self.num_boletos = int(input(f"Ingrese el número de boletos a comprar (máximo {7 * self.num_personas}): "))
                if self.num_boletos < 1 or self.num_boletos > 7 * self.num_personas:
                    print(f"Solo se pueden comprar hasta {7 * self.num_personas} boletos.")
                else:
                    break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        respuesta = input("¿Pagará con tarjeta CINECO? (si/no): ").strip().lower()
        self.usa_tarjeta_cineco = respuesta == "si"

        return self.usa_tarjeta_cineco


def main():
    print("El boleto vale $12, pero se pueden obtener descuentos por la compra.")
    respuesta = input("¿Desea realizar una compra? (si/no): ").strip().lower()

    if respuesta == "si":
        compra = CompraBoletos()
        repetir = False

        while True:
            # Obtiene los datos de la compra
            usa_tarjeta = compra.get_datos_compra(repetir=repetir)
            costo_total = compra.calcular_costo()

            # Muestra el costo y guarda la compra
            print(f"El costo total es de: ${costo_total:.2f}")
            compra.save_to_file("compra.txt")
            print("Compra guardada con éxito.")

            # Pregunta si desea realizar otra compra
            otra_compra = input("¿Quiere realizar otra compra? (si/no): ").strip().lower()
            if otra_compra == "si":
                print("Iniciando nueva compra...")
                repetir = True  # Solo reinicia el proceso desde los datos, no desde el nombre
            else:
                print("Compra finalizada.")
                break
    else:
        print("Operación cancelada.")


if __name__ == "__main__":
    main()