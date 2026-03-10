'''
!5 fatorial
5x!4
5x4x!3
5x4x3x!2
5x4x3x2x!1
5x4x3x2x1x1


def fatorial(num):
    print("Calculando o fatorial de:",num)
    if num == 1:
        return 1
    else:    
        resultado = (num * fatorial(num - 1))
        return(resultado)

print("O fatorial de 4 é:",fatorial(4))
'''

#Conte ate 3
def contar(num):
    print(num) 
    if num < 3:
        return contar(num+1)
     
        

print(contar(1))

'''
#Conte de 3 ate 0
def contar(n):
    if n != -1:
        print(n)
        contar(n-1) 


print(contar(3))'''