a = 'A'
b = 'B'
c = 1.1
formato = 'a={}, b={}, c={:.2f}'.format(a,b,c)
formato2 = f'a = {a}, b = {b}, c = {c}'
formato3 = 'b = {1}, c = {2}, a = {0}'.format(a,b,c)

string = 'c = {2}, b = {1}, a = {0}'
formato4 = string.format(a,b,c)


print(formato)
print(formato2)
print(formato3)