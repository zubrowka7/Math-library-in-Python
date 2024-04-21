import math
# abs(число) - модуль;
print('abs(1.2) =', abs(1.2))
print('abs(-1.2) =', abs(-1.2))
# min(числа) - найменше число;
print('\nmin(1, 2, 3) =', min(1, 2, 3))
print('min(-1, -2, -3) =', min(-1, -2, -3))
# max(числа) - найбільше число;
print('\nmax(1, 2, 3) =', max(1, 2, 3))
print('max(-1, -2, -3) =', max(-1, -2, -3))
# pow(число, степінь) - піднесення до степінь, аналог 2 ** 2;
print('\npow(2, 2) =', pow(2, 2))
print('pow(-2, -2) =', pow(-2, -2))
# round(число) - заокруглення;
print('\nround(0.5) =', round(0.5))
print('round(-0.5) =', round(-0.5))
# math.ceil(число) - найбільше, ближче ціле число;
print('\nmath.ceil(1.2) =', math.ceil(1.2))
print('math.ceil(-1.2) =', math.ceil(-1.2))
# math.floor(число) - найменше, ближче ціле число;
print('\nmath.floor(1.2) =', math.floor(1.2))
print('math.floor(-1.2) =', math.floor(-1.2))
# math.factorial(число) - факторіал;
print('\nmath.factorial(5) =', math.factorial(5))
print('math.factorial(-5) = error')
# math.trunc(число) - аналог int, відкидає дробову частину числа;
print('\nmath.trunc(1.2) =', math.trunc(1.2))  # = print(int(1.2))
print('math.trunc(-1.2) =', math.trunc(-1.2))  # = print(int(1,2))
# math.log(число, E) - логарифм;
print('\nmath.log2(4) =', math.log2(4))
print('math.log2(-4) = error')
# math.sqrt(число) - квадратний корінь числа;
print('\nmath.sqrt(4) =', math.sqrt(4))
print('math.sqrt(-4) = error')
# math.sin, math.cos - сінус, косинус;
print('\nmath.sin =', math.sin(3.14/2))  # - сінус;
print('math.cos =', math.cos(0))  # - косинус;
# math.pi, math.e - число пі, є;
print('\nmath.pi =', math.pi)  # - число пі;
print('math.e =', math.e)  # - число є;
