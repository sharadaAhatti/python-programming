n = int(input('enter array size:'))
array = []
for i in range(n):
    num = int(input(f'enter element {i+1}:'))
    array.append(num)
target = int(input('enter element to be searched:'))
found = False
index = -1
for i in range(n):
    if array[i] == target:
        found = True
        index = i
        break
if found:
    print(f'search item is {target} is {index}')
else:
    print('element not present in array!!')    
    