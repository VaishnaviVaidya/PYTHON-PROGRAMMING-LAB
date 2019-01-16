s=int(input('user input seconds '))
d=s//86400
print('the number of days are ')
print(d)
r=s%86400
h=r//3600
print('hours ')
print(h)
x=r%3600
y=x//60
print('minutes ')
print(y)
z=x%60
print('seconds ')
print(z)

