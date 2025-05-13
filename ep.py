##### EP - GIT ###
# Ao implementar uma função, dê commit no github usando os comandos vistos no workshop!
# Implemente uma função de cada vez, e dê commit em uma função por vez.
# NOME:


def minimo(arr):
    # retorna o menor valor do array
    return min(arr)

def maximo(arr):
    # retorna o maior valor do array
    return max(arr)

def meio(arr):
    # retorna o valor exatamente ao meio do array
    return arr[len(arr) // 2]

def media(arr):
    # retorna a media dos valores do array
    return sum(arr) / len (arr)

def moda(arr):
    # retorna o valor que mais se repete no array
    return max(set(arr), key=arr.count)

def soma(arr, n = 1):
    # soma n a todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [6, 6, 6]
    return [x + n for x in arr]

def subtracao(arr, n):
    # subtrai n em todos os valores do array e retorna o novo array
    # exemplo
    # entrada: arr = [1, 1, 1], n = 5
    # saida: arr = [-4, -4, -4]
    return [x - n for x in arr]

def soma_arr(arr1, arr2):
    # soma de dois arrays elemento-a-elemento e retorna
    return

def produto_interno(arr1, arr2):
    # retorna o produto interno entre dois vetores
    return

