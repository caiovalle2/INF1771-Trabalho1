import random

etapas = {'2': 35, '3': 40, '4': 45, '5': 50, '6': 55, '7': 60, '8': 65, '9': 70,
          'B': 75, 'C': 80, 'D': 85, 'E': 90, 'G': 95, 'H': 100, 'I': 110, 'J': 120, 'K': 130, 'L': 140,
          'N': 150, 'O': 155, 'P': 160, 'Q': 165, 'S': 170, 'T': 180}



def criar_populacao():
    person_total = [1.5, 1.4, 1.3, 1.2, 1.1, 1.0] * 11
    populacao = []
    for i in range(1000):
        individuo = [[] for _ in range(24)]
        person_total2 = person_total.copy()
        for j in range(24):
            individuo[j].append(person_total2.pop(random.randint(0, len(person_total2) - 1)))
        while person_total2:
            x = random.randint(0,23)
            value = person_total2.pop(random.randint(0, len(person_total2) - 1))
            if value not in individuo[x]:
                individuo[x].append(value)
        populacao.append(individuo)
    return populacao

def crossover(ind1, ind2):
    filho = [[] for _ in range(24)]
    for i in range(24):
        if i % 2 == 0:
            filho[i] = ind1[i]
        else:
            filho[i] = ind2[i]
    if not verifica_energia(filho):
        return ind1
    return filho

def mutacao(ind):
    lista = [1.5, 1.4, 1.3, 1.2, 1.1, 1.0]
    indice1 = random.randint(0, 23)
    novo_valor = random.randint(0, 5)
    if len(ind[indice1]) == 5:
        ind[indice1].pop(novo_valor)
        alterar_posicao(ind)
        return ind

    while lista[novo_valor] in ind[indice1]:
        novo_valor = random.randint(0, 4)

    ind[indice1].append(lista[novo_valor])
    if not verifica_energia(ind):
        ind[indice1].pop()
        alterar_posicao(ind)
    return ind

def alterar_posicao(ind):
    i = 0
    value = 0
    while value == 0:
        if ind[i]:
            value = ind[i].pop()
        i += 1

    for x in range(len(ind)):
        if x != i and value not in ind[x]:
            ind[x].append(value)
            return ind
def verifica_energia(ind):
    energia = {"1.0": 0, "1.1": 0, "1.2": 0, "1.3": 0, "1.4": 0, "1.5": 0}
    for i in ind:
        energia["1.0"] += 1 if 1.0 in i else 0
        energia["1.1"] += 1 if 1.1 in i else 0
        energia["1.2"] += 1 if 1.2 in i else 0
        energia["1.3"] += 1 if 1.3 in i else 0
        energia["1.4"] += 1 if 1.4 in i else 0
        energia["1.5"] += 1 if 1.5 in i else 0

    for key, value in energia.items():
        if value > 11:
            return 0
    return 1

def geracao():
    populacao = criar_populacao()
    for ger in range(200):
        avaliar(populacao)
        nova_populacao = []
        for i in range(1000):
            filho = crossover(populacao[0],populacao[1])
            if random.random() <= 0.3:
                filho = mutacao(filho)
            nova_populacao.append(filho)
        populacao = nova_populacao
    return min(populacao, key=tempo_gasto)


def avaliar(populacao):
    populacao.sort(key=tempo_gasto)

def tempo_gasto(ind):
    total = 0
    dif = [value for key,value in etapas.items()]
    for i in range(len(ind)):
        total += dif[i]/sum(ind[i])
    return total