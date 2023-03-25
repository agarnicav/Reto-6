
import math

def calcular_volumen_esfera(r1: float) -> float:
    volumen_esfera = (4/3) * math.pi * r1**3
    return volumen_esfera

def calcular_area_superficial_esfera(r1: float) -> float:
    area_superficial_esfera = 4 * math.pi * r1**2
    return area_superficial_esfera

def calcular_volumen_cono(r2: float, h: float) -> float:
    volumen_cono = (1/3) * math.pi * r2**2 * h
    return volumen_cono

def calcular_area_superficial_cono(r2: float, h: float) -> float:
    generatriz = math.sqrt(r2**2 + h**2)
    area_superficial_cono = math.pi * r2**2 + math.pi * r2 * generatriz
    return area_superficial_cono

if __name__ == "__main__":
    r1 = float(input("Ingrese el valor del radio de la esfera (r1): "))
    r2 = float(input("Ingrese el valor del radio de la base del cono (r2): "))
    h  = float(input("Ingrese el valor de la altura del cono (h): "))
   
    resultado = calcular_volumen_esfera(r1)
    print("El volumen de la esfera es: ", resultado)
    
    resultado =  calcular_area_superficial_esfera(r1)
    print("El area superficial de la esfera es:  ", resultado)
    
    resultado = calcular_volumen_cono(r2, h)
    print("El volumen del cono es: ", resultado)
    
    resultado = calcular_area_superficial_cono(r2, h)
    print("El area superficial del cono es: ", resultado)

    
    

    