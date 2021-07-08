# Problema:
# Ler dois valores float A e B, correspondendo a duas notas
# Calcular a media sendo que a nota A tem peso de 3.5 e a B 7.5


A = float(input())
B = float(input())
p1 = 3.5
p2 = 7.5
MEDIA = ((A * p1) + (B * p2))/(p1 + p2)
print("MEDIA = " + "{:.5f}".format(MEDIA))
