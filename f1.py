#type conversion
x=5
y=2.5
z=1j

a=float(x)
b=int(y)
c=complex(x)
d=complex(y)

print(a)
print(b)
print(c)
print(d)

#random number
import random

print(random.randrange(1,10))

#casting
x=int(2)
y=float(2)
z=float("3")
print(x,y,z)

#strings
h="""abababababab"""
print (h)

f="Hello, WOrld"
print(f[1])

for l in "banana":
    print(l)

print(len(f))