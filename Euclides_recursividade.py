'''
num = 17
den = 3

while (den != 0):
    x = num % den
    num = den
    den = x

print(num)    
'''

a = int(input("Digite o numerador: "))
b = int(input("Digite o denominador: "))


def mdc_recursivo(a, b):
  if b == 0:
    return a
  else:
    return mdc_recursivo(b, a % b)
  
print(mdc_recursivo)