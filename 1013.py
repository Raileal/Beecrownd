A,B,C = input().split(" ")

A = int (A)
B = int(B)
C = int (C)

MaiorAB = (A+B+abs(A-B))/2
R = (C+MaiorAB+abs(C-MaiorAB))/2
print(f"{R:.0f} eh o maior")
