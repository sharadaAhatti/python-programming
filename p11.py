def cal_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def cal_lcm(a,b):
    gcd = cal_gcd(a, b)
    lcm = (a * b) // gcd
    return lcm 

num1 = int(input('enter first number:'))
num2 = int(input('enter second number:'))

gcd = cal_gcd(num1,num2)
print(f'number {num1} and {num2} the GCD is {gcd}')

lcm = cal_lcm(num1,num2)
print(f'number {num1} and {num2} the LCM is {lcm}')   