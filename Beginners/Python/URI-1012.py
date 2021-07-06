A, B, C = input().split()
A, B, C = float(A), float(B), float(C)
pi = 3.14159

ATRI = (A * C)/2
AC = pi * C**2
ATRA = ((A + B) * C)/2
AS = B * B
AR = A * B

print("TRIANGULO: " + "{:.3f}".format(ATRI))
print("CIRCULO: " + "{:.3f}".format(AC))
print("TRAPEZIO: " + "{:.3f}".format(ATRA))
print("QUADRADO: " + "{:.3f}".format(AS))
print("RETANGULO: " + "{:.3f}".format(AR))
