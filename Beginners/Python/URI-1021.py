# Problema:
# Ler um floating point com duas casas decimais representando valor monetário
# Calcular o menor numero possivel de notas e moedas em que o valor pode ser decomposto


notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
qtnotas = []
valor = float(input())
N = int(valor)
i = int(0)

if 0 <= N <= 1000000:
    while True:

        floor = (valor * 100) // (notas[i] * 100)
        resto = round(valor % notas[i], 2)
        valor = resto
        qtnotas.append(floor)
        i += 1

        if i >= 12:
            break
else:
    print("Input deve ser entre 0 e 1000000")

print("NOTAS:")

for i in range(0, 6):
    print(str(int(qtnotas[i])) + " nota(s) de R$ " + "{:.2f}".format(notas[i]))

print("MOEDAS:")

for i in range(6, 12):
    print(str(int(qtnotas[i])) + " moeda(s) de R$ " + "{:.2f}".format(notas[i]))
