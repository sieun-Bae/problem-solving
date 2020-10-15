a, b, c = map(int, input().split())

a%=c
b%=c

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)
print((a-b)%c)
print((a%c - b%c)+c)%c