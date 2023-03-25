 def Calcular_el_promedio_multiplicativo( a=float, b=float, c=float, d=float, e=float)-> float: 
    Promedio_multiplicativo= (a*b*c*d*e )**1/5
    
    return Promedio_multiplicativo

if __name__ == "__main__":
    a = float(input("Ingrese el primer número "))
    b = float(input("Ingrese el segundo  número "))
    c = float(input("Ingrese el tercero  número "))
    d = float(input("Ingrese el cuarto  número "))
    e = float(input("Ingrese el quinto  número "))
    
  
resultado = Calcular_el_promedio_multiplicativo(a,b,c,d,e)
print("El promedio multiplicativo de los números es:", resultado)