import math
#trigonometria
print(math.sin(2*math.pi/180))
#raiz quadrada
print(math.sqrt(144))

#diferenca entre arredondar ou truncar
#math.trunc(x)
# Return the Real value x truncated to an Integral (usually an integer). Delegates to x.__trunc__().
num_trunc = math.trunc(10.243)
print(num_trunc)
#print('%1.2f' % num_trunc)

print(round(10.243))

#math.floor(x)
#Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.
num_floor = math.floor(10.243)
print(num_floor)
#print('%1.2f' % num_floor)

#math.ceil
#Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
num_ceil = math.ceil(10.243)
print(num_ceil)
#print('%1.2f' % num_ceil)
