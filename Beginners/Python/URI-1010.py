# Problema: 
# Ler o codigo do produto 1, com seu preço e numero de unidades. 
# O mesmo para o produto 2
#Calcular o valor a ser pago


i1 = []
i2 = []

msg = ["Code:", "N. units:", "Price:"]

for i in range(0, 6):
    if i <= 2:
        print(msg[i])
        val = input()
        i1.append(val)
    if i > 2:
        print(msg[i-3])
        val = input()
        i2.append(val)

VA = float(int(i1[1]) * float(i1[2]) + int(i2[1]) * float(i2[2]))
print("VALOR A PAGAR: R$ " + "{:.2f}".format(VA))
