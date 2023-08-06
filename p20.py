try:
    x = int(input('enter value of X:'))
    y = 10/x
    print('result', y)
except ValueError:
    print('enter valid number! plz enter valid number')
except ZeroDivisionError:
    print('value cannot divisible by zero')
finally:
    print('exception handling ex completed')        