from busca import Busca
from genetico import *

custo_total = 0
mapa = Busca('kanto.txt')
mapa.cria_mapa()
coordenadas = {mapa.mapa[linha][coluna]: [linha,coluna] for linha in range(len(mapa.mapa)) for coluna in range(len(mapa.mapa[linha])) if mapa.mapa[linha][coluna] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'B', 'C','D', 'E', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'S', 'T']}

coordenadas = [values for key,values in sorted(coordenadas.items())]
for i in range(len(coordenadas)-1):
    #Exibe o caminho da etapa
    custo_total += mapa.busca_heuristica(coordenadas[i],coordenadas[i+1])
    print('Custo da rota: ',mapa.busca_heuristica(coordenadas[i],coordenadas[i+1]))
    mapa.exibe_caminho()
    mapa.caminho = []
    input('')
print('Custo total: ', custo_total)



# Segunda parte

geracao = geracao()
print(geracao)
print(tempo_gasto(geracao))