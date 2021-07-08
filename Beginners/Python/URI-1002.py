# Problema:
# Calcular a area da circunferencia de raio R
# Input contem um valor de floating point
# Resultado apresenta o valor "A" com quatro casas decimais

π = 3.14159
R = float(input())
A = float(round(π * (R ** 2), 4))
print("A=" + "{:.4f}".format(A))
