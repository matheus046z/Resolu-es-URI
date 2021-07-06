notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
qtnotas = []
N = int(input())
print(N)
i = int(0)

if 0 <= N <= 1000000:
    while True:
        floor = N // notas[i]
        resto = N % notas[i]

        if floor >= 0:
            qtnotas.append(floor)
            N = resto
            i += 1

        if i >= 7:
            break
    for i in range(0, 7):
        print(str(int(qtnotas[i])) + " nota(s) de R$ " + str(int(notas[i])) + ",00")
else:
    print("Input deve ser entre 0 e 1000000")
