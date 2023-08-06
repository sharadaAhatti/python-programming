num = int(input('enter number:'))
print(f'tables of {num} is')
for i in range(1,11):
    res = num * i
    print(f'{num} x {i} = {res}')    