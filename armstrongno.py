'''x=input('enter the number ')
l=len(x)
add=0
for j in range(0,l): 
 add+=int(x[j])**l
if int(x)==add:
  print('It is an Armstrong number')
else:
  print('It is not an Armstrong number')

'''
i=0
x=input()
l=len(x)
sum=0
while i<l:
 sum+=int(x[i])**l
 i+=1
if int(x)==sum:
  print('yes')
else:
  print('no')


