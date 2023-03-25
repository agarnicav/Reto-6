def calcular_total_compra(P: int, M: int, H: int, B: int) -> int:
    total_pan = P * 300
    total_leche = M * 3300
    total_huevos = H * 350
    total_compra = total_pan + total_leche + total_huevos
 
    return total_pan, total_leche, total_huevos, total_compra


def calcular_vueltas_o_deuda(total_compra, B):
    if B >= total_compra:
        vueltas = B - total_compra
        return vueltas
    else:
        deuda = total_compra - B
        return -deuda


if __name__ == "__main__":
    P = float(input("Ingrese la cantidad de panes que se compraran : "))
    M = float(input("Ingrese la cantidad de leche que se compraran : "))
    H = float(input("Ingrese la cantidad de huevos que se compraran: "))
    B = float(input("Ingrese la cantidad de dinero en pesos que lleva : "))
    
    resultado = calcular_total_compra(P, M, H, B)
    
    print("EL total de dinero que se gasta en pan es: ", resultado[0])
    print("La cantidad de dinero que se gasta en leche es: ", resultado[1])
    print("La cantidad de dinero que se gasta en huevos es: ", resultado[2])
    print("La cantidad de dinero que se gasta es :", resultado[3])

    vueltas_o_deuda = calcular_vueltas_o_deuda(resultado[3], B)
    if vueltas_o_deuda >= 0:
        print(" Sus vueltas son: ", vueltas_o_deuda)
    else:
        print(" Queda debiendo", -vueltas_o_deuda)
