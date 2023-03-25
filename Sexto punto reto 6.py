def calcular_contagios(C: int, D: int) -> int:
    total_contagios = C * (2 ** D)
    return total_contagios

if __name__ == "__main__":
    C = int(input("Ingrese el número actual de contagiados: "))
    D = int(input("Ingrese la cantidad de días a proyectar: "))

    total_contagios = calcular_contagios(C, D)
    print("El número total de personas contagiadas después de", D, "días será:", total_contagios)
    