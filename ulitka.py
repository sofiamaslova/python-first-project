print('vvedite dlinu shesta')
h = int(input())
print('vvedite dnevnoi put')
a = int(input())
print('vvedite nochnoy put')
b = int(input())
i = 0
if a<b:
    print('ochen slabaya ulitka')
while h>0:
    h=h-a+b
    i+=1
else:
    print('ulitka zakonchit svoy put cheres', i, 'dney')	 
