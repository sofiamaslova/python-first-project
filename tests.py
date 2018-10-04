count = 6.1231235

print ("Яблок: %d" % count)
print ("Яблок: %f" % count)
print ("Яблок: %s" % count)
print ("Яблок: %+.2f" % count)

count_apples = 6
count_pears = 5
# print ("Яблок: {0}, Груш: {1}", .format (count_apples, count_pears) )

i = 5
f = 5.5
string = 'yes'
list_var = [1, 2, 3]
set_var = {6, 5, 1, 12, 56}

a = {2, 4, 6}
b = {1, 3, 5}
c = a | b
print (a.union(b))
print (c.intersection(b))
print (c.symmetric_difference({1, 2, 3, 4, 5, 6}))
print (c)
d = c - {1, 2}
e = a & d
print(d)
print(e)
g = c ^ b
print(g)

a = {'name': 'Michael', 'age': 18}
print (a.get('ggg', 'fff') )
