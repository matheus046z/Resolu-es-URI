A, B, C, D = [int(x) for x in input().split()]


if B > C and D > A and (C + D) > (A + B) and C >= int(0) and D >= int(0) and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
