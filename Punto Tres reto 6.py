
def calcular_cantidad_carne(N= float, M = float, K= float)-> float: 
    carne_gallinas = N * 6
    carne_gallos = M * 7
    carne_pollitos = K * 1
    Total_carne_Gallina_Gallos_Pollitos = carne_gallinas + carne_gallos + carne_pollitos
    return  Total_carne_Gallina_Gallos_Pollitos , carne_gallinas , carne_gallos , carne_pollitos
  
if __name__ == "__main__":
    N = float(input("Ingrese cantidad de gallinas: "))
    M = float(input("Ingrese cantidad de gallos: "))
    K = float(input("Ingrese cantidad de pollitos: "))
    
    resultado = calcular_cantidad_carne(N, M, K)

    print("La cantidad de carne en kilos de gallinas es: ", resultado[1])
    print("La cantidad de carne en kilos de gallos es: ", resultado[2])
    print("La cantidad de carne en kilos de pollitos es:", resultado[3])
    print("La cantidad de carne en kilos de las aves:", resultado[0])


