num = int(input('enter a number:'))
fact=1
if num < 0:
    print('factorial is not lessthen zero')
elif num == 0:
    print('the factorial 0 is 1')
else:
    for i in range(1,num+1):
        fact = fact * i
    print('the fact of', num, 'is', fact) 
            