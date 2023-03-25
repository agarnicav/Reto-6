import math

def calcular_area_perimetro_circulo(r= float, a= float, b= float) -> float:
    area_circulo = math.pi * r**2
    perimetro_circulo = 2 * math.pi * r
    return area_circulo, perimetro_circulo
    

def calcular_area_perimetro_rectangulo(a= float, b= float) -> float:
    area_rectangulo = a * b
    perimetro_rectangulo = 2 * (a + b)
    return area_rectangulo, perimetro_rectangulo


if __name__ == "__main__":
    r = float(input("Ingrese el radio del círculo en centimetros: "))
    a = float(input("Ingrese la base del rectángulo en centimetros: "))
    b = float(input("Ingrese la altura del rectángulo en centimetros: "))

    resultado_circulo = calcular_area_perimetro_circulo(r, a, b)
    print("El área del círculo es:", resultado_circulo[0], "cm^2")
    print("El perímetro del círculo es:", resultado_circulo[1], "cm")
    
    resultado_rectangulo = calcular_area_perimetro_rectangulo(a, b)
    print("El área del rectángulo es:", resultado_rectangulo[0], "cm^2")
    print("El perímetro del rectángulo es:", resultado_rectangulo[1], "cm")
