def max_crossing(k, low, mid, high):
    """Retorna a soma do subarranjo máximo que cruza o ponto médio"""
    left_sum = 0
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + k[i]
        if sum > left_sum:
            left_sum = sum
    right_sum = 0
    sum = 0
    for j in range(mid+1, high):
        sum = sum + k[j]
        if sum > right_sum:
            right_sum = sum
    return left_sum + right_sum

def maximum(k, low, high):
    """Retorna a soma do subarranjo máximo
    Algoritmo com complexidade de tempo logaritmica
    Utiliza divisão e conquista
    """
    if (high - low) == 1:
        return k[low]
    else:
        mid = int((low + high) / 2)
        left_sum = maximum(k, low, mid)
        right_sum = maximum(k, mid, high)
        cross_sum = max_crossing(k, low, mid, high)
        return max(left_sum, right_sum, cross_sum)

def maximum_quad(k):
    """"Algoritmo de força bruta que não está sendo utilizado
    É um algoritmo simples e de rápida implementação,
    porém tem complexidade de tempo quadrática
    """
    sum = 0
    max_sum = 0
    for i in range(0, len(k)-1):
        sum = k[i]
        for j in range(i+1, len(k)):
            sum = sum + k[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum
            

def maximum_profit(k):
    """"Retorna o lucro máximo
    Seja deltas um arranjo que contém as diferenças de preços
    entre os dias i-1 e i.
    Este algoritmo retorna a soma do subarranjo
    cujo os valores tenham a maior soma (subarranjo máximo)
    """
    deltas = []
    for i in range(len(k)-1):
        deltas.append(k[i+1] - k[i])
    #Utilzando o algoritmo logarítmico
    return maximum(deltas, 0, len(deltas))
    #Utilzando o algoritmo quadrático
    #return quad(deltas)


k1 = [7,1,5,3,6,4]
k2 = [7,6,4,3,1]
print(maximum_profit(k1))


    

