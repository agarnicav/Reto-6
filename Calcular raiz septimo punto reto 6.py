def calcular_raíz ( a=float, b=float, c=float, d=float, e=float) -> list: 
    numeros = [a , b, c ,d , e ]
    minimo = min(numeros)
    raíz_cubica = minimo ** (1/3)

    return(raíz_cubica)


if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    
resultado = calcular_raíz(a,b,c,d,e)
print( "La raíz cúbica del menor número es: ", resultado)