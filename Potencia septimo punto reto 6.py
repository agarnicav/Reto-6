def Calcular_potencia ( a=float, b=float, c=float, d=float, e=float) -> list: 
    numeros = [a , b, c ,d , e ]
    #La potencia del mayor número elevado al menor número
    maximo = max(numeros)
    minimo = min(numeros)
    potencia =  maximo**minimo
    return (potencia)


if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    

resultado = Calcular_potencia(a,b,c,d,e)
print("La potencia del mayor número elevado al menor número es:", resultado)
    