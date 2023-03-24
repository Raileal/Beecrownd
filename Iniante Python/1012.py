X = input().split(" ")

A,B,C = X

TOTAL1 = (float(A)*float(C))/2
TOTAL2 = 3.14159 * (float(C)*float(C))
TOTAL3 = ((float(A)+float(B))/2) * float(C)
TOTAL4 = float(B)*float(B)
TOTAL5 = float(A)*float(B)
print("TRIANGULO: %.3f"%TOTAL1)
print("CIRCULO: %.3f"%TOTAL2)
print("TRAPEZIO: %.3f"%TOTAL3)
print("QUADRADO: %.3f"%TOTAL4)
print("RETANGULO: %.3f"%TOTAL5)