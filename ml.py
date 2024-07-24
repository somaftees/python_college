from numpy import random

#random int number
x = random.randint(100)
print(x)


#random float number from 0-1
z =random.rand()
print(z)

#random int 1d array
y = random.randint(100, size=(5))
print(y)

print("---------------------------------------")

#random int 2d array
t = random.randint(100, size=(3,5))
print(t)


print("---------------------------------------")

#random float 1d array with numbers from 0-1
r =random.rand(5)
print(r)

print("---------------------------------------")

#random float 2d array with numbers from 0-1
d =random.rand(2,3)
print(d)


print("---------------------------------------")

#random choice a number from your array
c =random.choice([11,14,21,3,2])
print(c)


print("---------------------------------------")

#random choice 2d array from your array
b =random.choice([11,14,21,3,2], size=(3,5))
print(b)
