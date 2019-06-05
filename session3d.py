#Bitwise operator

a=8   #1000
b=12  #1100
c=a&b #1000
d=a|b #1100
e=a^b #0100
print(c)
print(d)
print(e)
"""

x=12 #1100
y=3
#Right shift operation
#z=x>>y #1100>>3->0001
z=x<<y #1100>>3 ->1100000
print(z)
"""
x=-13 #2s complement put 1 in space then again take 2s complement

y=2
z=x>>y
print(z)
