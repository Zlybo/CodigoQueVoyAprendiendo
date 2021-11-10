import numpy as np


def buscar_repetido(matriz, filas, columnas, i, j):
    valor = matriz[i][j]
    for k in range(filas):
        for l in range(columnas):
            if matriz[k][l] == valor and not (k == i and l == j):
                return (k, l)

    return False


def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    while filas*columnas >= 100 or filas == columnas:
        print(
            "No se pueden mas de 100 datos. Las filas y las columnas no pueden ser iguales")
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))

    matriz = np.random.randint(0, 100, (filas, columnas))

    # forzar repetidos
    matriz[0][0] = 0
    matriz[0][1] = 0

    for i in range(filas):
        for j in range(columnas):
            repetido = buscar_repetido(matriz, filas, columnas, i, j)
            if repetido:
                print(
                    f"Se encontro un valor repetido en {repetido[0]} {repetido[1]}")
                valor = input(
                    "Ingrese el valor por el cual desea reemplazar: ")
                matriz[repetido[0]][repetido[1]] = valor
    # sorteadisimo pai
    for fila in matriz:
        for i in range(len(fila)):
            for j in range(len(fila) - 1):
                if fila[j] > fila[j + 1]:
                    fila[j], fila[j + 1] = fila[j + 1], fila[j]

    print(matriz)


if __name__ == '__main__':
    main()
