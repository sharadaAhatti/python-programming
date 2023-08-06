def insert_sorted(array, num):
    index = 0
    while index < len(array) and array[index] < num:
        index += 1
    array.insert(index, num)
n = int(input('enter array size:'))
array = []
for i in range(n):
    num = int(input(f'enter element {i+1}:')) 
    array.append(num)
num_to_insert = int(input('enter to be searched:'))
insert_sorted(array, num_to_insert)  
print('updated array:',array)    