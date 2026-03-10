''' o q preciso saber de ED




Estruturas lineares:

Listas, tuplas, conjuntos (sets) e dicionários

como fazer classes

Arrays: Uma coleção de elementos do mesmo tipo, acessados por um índice. Podem ser de tamanho fixo. 

Listas: Uma sequência de elementos. Podem ser implementadas de diferentes formas, como listas encadeadas, que permitem inserções rápidas. 

Pilha (Stack): Uma estrutura onde o último elemento inserido é o primeiro a ser removido (LIFO - "Last-In, First-Out"). 

Fila (Queue): Uma estrutura onde o primeiro elemento inserido é o primeiro a ser removido (FIFO - "First-In, First-Out"). 



Estruturas não-lineares:

Árvores: Organizam dados de forma hierárquica, com nós "pai" e "filho". 

Grafos: Representam conjuntos de nós conectados por arestas, usados para modelar relações complexas. 

Tabelas Hash (Hash tables): Estruturas que usam uma função de hash para mapear chaves a valores, permitindo buscas rápidas. 




Algoritmos associados:

Estude algoritmos para realizar operações como busca (linear, binária) e ordenação (bubble sort, merge sort) sobre essas estruturas. 
teste.remove(23)




#listas = pode ter repetido, tem indice, mutavel, varios tipos de dados diferentes numa so [,,,,]

teste = ['carro',23, 1.2333,23,23,True]
teste.remove('carro') #remove a primeira vez da variavel
print(teste)


teste.append('adicionado1')
teste.insert(1,'adcionado2')
teste.extend('abc')#parecido com o append mas ele quebra em varios elementos 
teste.remove('carro') or teste.remove(23)

print(teste.pop(0))  #remove com so 1 idex e se eu printar ela me da o item q foi removido naquele idex



#teste.clear()limpa tudo
#print(teste.index('adicionado1')) retorna o index de um elemento q eu chamei
#print(teste[0]) retorna o elemento do index q eu pedi da lista
#print(teste.count(23))
#print(23 in teste) and ('tel' not in teste) #verificar se ta ou n

num = [1,27,3,0,65,4,9,-0,2,4,53,]

num.sort() #ordenda crescente
num.sort(reverse=True) #ordenda decrescente
num.sort(key=) #ordendem personalizada
print(num.copy())




#listas aninhadas sao arrays = matrizes e tabelas (listas dentro de listas)

exemplo_de_matriz_comprimida = [[1,2,3],[4,5,6],[7,8,9]]

del exemplo_de_matriz_comprimida[1][1]

print(exemplo_de_matriz_comprimida)  # [[1, 2, 3], [7, 8, 9]]

#print(exemplo_de_matriz_comprimida[2][1])#8
#todos as operacoes com listas funcionam na matriz (ate pq esta matriz é so varias listas juntas)

#fazer matrizes usando a biblioteca numpy
import numpy as np #pega somente uma funçao da biblioteca em vez de importar ela toda
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)




#Pilhas = parecido com lista, mas, primeiro a entrar é o ultimo a sair (pilha de pratos) e o ultimo a entrar é tbm o ultimo a sair

so uma lista e manuseiala com append e pop


#filas = usa listas mas o primeiro a entrar é tbm o ultimo a sair (fila de banco). Usa sempre um apppend(0) e pop()



        #Comprensao de listas


lista_original = [1, 2, 3, 4, 5]
quadrados_com_loop = []
for x in lista_original:
    if x % 2 == 0:
        quadrados_com_loop.append(x**2)



lista_original = [1, 2, 3, 4, 5]

quadrados_com_loop = [x**2 for x in lista_original if x %2==0] 

print(quadrados_com_loop)



#tuplas sao listas imutaveis, n da pra apagar as variaveis, mudar de idice ou atribuir outros dados nelas. listas geralmente sao pra 1 tipo de valor, tuplas normalmente varios

tupla = (0, "abc", True,3)

#tupla[0] = 2 n funciona
#tupla.pop() n funciona

tupla_listas = ([0,1],['a','b'])

tupla_listas[0][1] = 2 #os elementos das tuplas n podem ser mudados, mas se tiver listas nelas(tuplas),, os itens dentro delas(listas) podem ser alterados

#as tuplas podem ser empacotadas e desempacotadas

#a,b = tupla_listas #desempacotar


list1 = [ 'a',1,2] #listas
list2= ['b',3,4] #listas
list3= ['c',5,6] #listas

list_geral = list1, list2, list3 #empacotar

print(list_geral) #tupla de listas


#conjuntos (sets) = se usa {} ou a funcao set(), lista sem indices e ordem, n aceitam dados mutaveis (listas,dicionarios, outros sets) e por fim, n da pra ter elementos repetidos, ele elimina automaticamente os repetidos 

conjunto_nome = {'sofia', 'pedro','antonieta', 'jao'}
#operacoes= mesmas da matematica (uniao (junta conjuntos), interseccao(pega os elementos em comum de 2 ou mais conjuntos), diferenca(a-b pega os elementos de a diferentes e n comuns a b), diferenca simetrica(tir4a os elementos comuns e junta o resto))

conjunto_nome_comparar = {'jao', 'maria','antonieta', 'carlos'}

print(conjunto_nome.union(conjunto_nome_comparar)) #{'sofia', 'pedro','antonieta','jao', 'maria', 'carlos'}
print(conjunto_nome.intersection(conjunto_nome_comparar))  #{'antonieta', 'jao'}
print(conjunto_nome.difference(conjunto_nome_comparar)) #{'sofia', 'pedro'}
print(conjunto_nome.symmetric_difference(conjunto_nome_comparar)) #{'sofia', 'pedro','maria', 'carlos'}



#dicionarios sao listas com chaves:valores (sendo q tanto a chave quanto o valor podem ser qualquer tipo de dado imutavel, so posso usar exclusivamente a chave pra acessar o valor, n vice versa. Operacoes: acessar itens, adcionar, atribuir ou trocar, deletar e iterar )

# Dicionário com chaves do tipo string
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "Guarabira"
}

# Acessando valores através das chaves
#print(pessoa["nome"])
#print(pessoa["idade"])

pessoa = dict(profissao = 'pintor', idade = 'velha')

print(pessoa)

'''
