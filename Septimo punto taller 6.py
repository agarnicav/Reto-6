
def calcular_promedio( a=float, b=float, c=float, d=float, e=float)-> float: 
    promedio= (a+b+c+d+e)/5
    
    return promedio

def calcular_la_mediana( a=float, b=float, c=float, d=float, e=float)-> float: 
    lista= (a,b,c,d,e)
    lista_numeros  = sorted(lista)
    n = len(lista_numeros)
    if n % 2 == 1:
        mediana = lista_numeros[n // 2]
    else:
        mediana = (lista_numeros[n // 2 - 1] + lista_numeros[n // 2]) / 2
    return mediana, lista_numeros, lista
    
   
def Calcular_el_promedio_multiplicativo( a=float, b=float, c=float, d=float, e=float)-> float: 
    Promedio_multiplicativo= (a*b*c*d*e )**1/5
    
    return Promedio_multiplicativo

def Numeros_ordenar_ascendente(a=float, b=float, c=float, d=float, e=float) -> list:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if d > e:
        d, e = e, d
    if c > d:
        c, d = d, c
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    return [a, b, c, d, e]

def Numeros_ordenar_descendente ( a=float, b=float, c=float, d=float, e=float) -> list: 
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    if d < e:
        d, e = e, d
    if c < d:
        c, d = d, c
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
        
    return(a,b,c,d,e )
    

def Calcular_potencia ( a=float, b=float, c=float, d=float, e=float) -> list: 
    numeros = [a , b, c ,d , e ]
    #La potencia del mayor número elevado al menor número
    maximo = max(numeros)
    minimo = min(numeros)
    potencia =  maximo**minimo
    return (potencia)

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
    
    resultado = calcular_promedio(a,b,c,d,e)
    print("El promedio de los números es:", resultado)
    
    resultado =calcular_la_mediana(a,b,c,d,e)
    print("La mediana de los números es:", calcular_la_mediana)
    
    resultado = Calcular_el_promedio_multiplicativo(a,b,c,d,e)
    print("El promedio multiplicativo de los números es:", resultado)
    
    resultado = Numeros_ordenar_ascendente(a,b,c,d,e)
    print("Los números ordenados de menor a mayor son:", resultado)
    
    
    resultado = Numeros_ordenar_descendente(a,b,c,d,e)
    print("Los números ordenados de mayor a menor son:", resultado)
    
    
    resultado = Calcular_potencia(a,b,c,d,e)
    print("La potencia del mayor número elevado al menor número es:", resultado)
    
    resultado = calcular_raíz(a,b,c,d,e)
    print( "La raíz cúbica del menor número es: ", resultado)
    