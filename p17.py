stack = []
def push(element):
    stack.append(element)
    print('element',element,'to be inserted')
def pop():
    if len(stack) == 0:
        print('stack is empty pop operation cannot be performed.')
    else:
        element = stack.pop()
        print('the element', element,'is poped')
def display():
    if len(stack) == 0:
        print('element cannot be present.')
    else:
        print('element to be display', stack)
while True:
    print('\n your choice(1-4)')
    print('1.push')
    print('2.pop')
    print('3.display')
    print('4.quit')
    choice = int(input('enter your choice:'))
    if choice == 1:
        element = input('enter element to be inserted:')
        push(element)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('enter valid chice:')      
                                  