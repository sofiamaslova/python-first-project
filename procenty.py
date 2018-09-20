import math
print ('vvedite procentnuyu stavku')
p = int(input())
print ('vvedite summu vklada v rublyax')
x = int(input())
print ('vvedite summu vklada v kopeikah')
y = int(input())
z = round(((x+y/100)*(1+p/100)), 2)
print ('summa vklada cherez god budet', z) 

