import math #biblioteca de matematica
x1,y1 = input().split(" ")
x2,y2 = input().split(" ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

Distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))#Elevado ao quadrado e na raiz 

print(f"{Distancia:.4f}")