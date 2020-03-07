a,b=5,6
a,b=b,a #values on RHS go into stack
print(a)
print(b)

a = a ^ b
b = b ^ a
a = a ^ b
print(a)
print(b)