'''
fazer questoes de recursividade


def soma_de_naturais(n):
    if n > 0:
        return(n + soma_de_naturais(n-1))
    else:
        return(0)
    
a = int(input("Digite um numero: "))

print(soma_de_naturais(a))


def soma_ate_o_zero(n):
    if n > 0:
        return(n + soma_ate_o_zero(n-1))
    else:
        return(0)
    
a = int(input("Digite um numero: "))

print(soma_ate_o_zero(a))
'''



def fatorial(n):
    print("\nCalculando o fatorial de ",n)
    if ( n <= 1 ):
#Caso base: fatorial de n <= 1 retorna 1
        return 1
    else:
#Chamada recursiva
        fat = (n * fatorial(n - 1))
        print(f"\nfatorial de {n} = {fat}")
        return fat


a = int(input("Digite um numero: "))

print(fatorial(a))


'''mdc em python'''

