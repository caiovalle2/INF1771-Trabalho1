# Inf1771 - Trabalho 1
Trabalho realizado para a disciplina de inteligência artificial na PUC-Rio.

# Resumo:
O trabalho consistia em desenvolver o algorítmo A* para encontrar a rota com o menor custo, além de encontrar a melhor combinação
de jogadores para realizar cada percurso.

# Funcionamento:
Para encontrar a rota com solução ótima para cada etapa do algorítmo de busca A*, o código desenvolvido realiza uma busca
em todos os campos da matriz obtida pelo mapa que ja foram 'abertos' até encontrar o destino, ou seja, o
algorítmo implementado, a partir da origem, expande o campo que ele está apontando e coloca os campos adjacentes em aberto.
Enquanto não encontra o destino, o campo que é apontando é o menor custo total que está aberto, após isso, ele é exapandido
e seus adjacentes ficam abertos.

Dessa maneira, ficaria:

    origem: [0,0] destino: [2,4]
    abertas: origem(0,0)
    expandidas:

    ORR..
    ..R..
    ....F

Na primeira vez, o campo O é expandido e seus adjacentes são colocados dentro da lista de abertas, alem de calculados os custos
desses campos. Visto isso, na proxima vez, o algorítmo apontará para o campo aberto de menor custo:
   
    origem: [0,0] destino: [2,4]
    abertas: [1,0], [0,1]
    expandidas: (0,0)

    ORR..
    ..R..
    ....F

Como o [1,0] tem o menor custo(custo igual a 1), então os proximos passos serão baseados neste campo. o [1,0] é expandido
e seus adjacentes são abertos.

Para as proximas etapas, o algorítmo vai repetir os mesmos passos anteriores até encontrar o destino.

Na busca heuristica, o custo é baseado não só no custo de cada deslocamento entre campos adjacentes, como também tem o custo da distância euclidiana como a função heuristica entre o campo que está sendo apontado e o destino. Dessa forma, o algoritmo tende a priorizar os campos mais próximos do objetivo e aumentando a eficiência.

A função busca_heuristica recebe as coordenadas do inicio e destino, retornando o menor custo.





Para segunda parte, foi utilizado algoritmo genetico para encontrar a melhor combinação entre os personagens


A população é uma lista de indivíduos, e estes são listas de listas, onde cada sublista representa uma etapa e contem as informações das agilidades dos personoagens como:

  individuo = [[1.5,1.3,1.1],...] - na etapa 1 foram utilizadas as agilidades 1.5, 1.3 e 1.1.
  
 Dessa forma, o programa inicia com a funcao geracao que cria uma populacao inicial de 1000 individuos. Em cada geração a funcao avalia ordena a lista de população com o tempo gasto por cada individuo. O programa cria 1000 filhos através do crossover entre os dois melhores individuos, ou seja, com o menor tempo gasto. Uma função com a mutação dos filhos foi adicionado para que possa gerar individuos melhores. No final, é refeito todo o processo para os filhos da população atual.
 
 Nos testes, o algoritmo parecia melhorar conforme aumenta o número de gerações, individuos e filhos. Porem, os individuos ficavam diferentes para as mesmas configurações e o valor era próximo de 1200.
 
