dias = int(input())

anos = dias // 365
meses = (dias % 365) // 30
dias = (dias % 365) % 30

print(str(anos) + " ano(s)")
print(str(meses) + " mes(es)")
print(str(dias) + " dia(s)")
