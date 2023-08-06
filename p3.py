import cmath
a = int(input('enter a co-efficient of A:'))
b = int(input('enter a co-efficient of B:'))
c = int(input('enter a co-efficient of C:'))
dis = (b**2) - (4 * a * c)
sol1 = (-b + cmath.sqrt(dis))/(2*a)
sol2 = (+b + cmath.sqrt(dis))/(2*a)
print('solution1 is:',(sol1))
print('solution2 is;',(sol2))