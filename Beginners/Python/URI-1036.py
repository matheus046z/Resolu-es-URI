A, B, C = [float(x) for x in input().split()]

raiz = B**2 - 4 * A * C

if A != 0 and raiz > 0:
    R1 = round((-B + raiz**(1/2)) / (2 * A), 5)
    R2 = round((-B - raiz**(1/2)) / (2 * A), 5)
    print("R1 = " + str(R1))
    print("R2 = " + str(R2))

else:
    print("Impossivel calcular")
