X = input().split(" ")
Y = input().split(" ")

A,B,C = X
A1,B1,C1 = Y

Total = (int(B)*float(C)) + (int(B1)*float(C1))

print(f'VALOR A PAGAR: R$ {Total:.2f}')

