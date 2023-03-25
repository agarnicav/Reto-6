def calcular_promedio( a=float, b=float, c=float, d=float, e=float)-> float: 
    promedio= (a+b+c+d+e)/5
    
    return promedio

if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    
    resultado = calcular_promedio(a,b,c,d,e)
    print("El promedio de los números es:", resultado)