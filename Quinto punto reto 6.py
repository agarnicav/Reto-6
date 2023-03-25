
def calcular_Valor_Prestamo(C: int, I: int, n: int, ) -> int:
    Valor_Prestamo = C* (1+I)**n
 
    return (Valor_Prestamo)


if __name__ == "__main__":
    C = float(input("Ingrese el monto del préstamo: "))
    i = float(input("Ingrese la tasa de interés anual en decimal: "))
    n = int(input("Ingrese la cantidad de meses del préstamo: "))


    valor_prestamo = calcular_Valor_Prestamo(C, i/12, n)  
    print("El valor total del préstamo con interés compuesto es:", valor_prestamo)
