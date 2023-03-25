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

if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    

      
resultado = Numeros_ordenar_descendente(a,b,c,d,e)
print("Los números ordenados de mayor a menor son:", resultado)