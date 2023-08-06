n = int(input('enter size of array:'))
array = []
for i in range(n):
    num = int(input(f'enter element {i+1}:'))
    array.append(num)
    positive_sum = 0
    negative_sum = 0
for num in array:    
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
print(f'sum of positive number is {positive_sum}')
print(f'sum of negative number is {negative_sum}')            