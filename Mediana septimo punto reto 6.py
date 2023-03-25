def calcular_la_mediana( a=float, b=float, c=float, d=float, e=float)-> float: 
    lista= (a,b,c,d,e)
    lista_numeros  = sorted(lista)
    n = len(lista_numeros)
    if n % 2 == 1:
        mediana = lista_numeros[n // 2]
    else:
        mediana = (lista_numeros[n // 2 - 1] + lista_numeros[n // 2]) / 2
    return mediana, lista_numeros, lista
    
if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    
    
resultado =calcular_la_mediana(a,b,c,d,e)
print("La mediana de los números es:", calcular_la_mediana)