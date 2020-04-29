## Computing the Graovac Ghorbani index for bicyclic graphs

We describe all routines developed to obtain the results of the paper *On the Graovac-Ghorbani index for bicyclic graphs with no pendant vertices*. 

Our goal is to make all routines available and contribute to the academic commmunity in computing the Graovac Ghorbani index, which we will refer as ABC2. 

All routines are written in SageMath (cocalc.com)

Routines available are:

ABC2(G): compute the ABC2 index for a graph G given as an input.
minimizeABC2(n): return the graph with minimal ABC2 among all bicyclic graphs of order n.
maximizeABC2(n): return the graph with maximal ABC2 among all bicyclic graphs of order n.

## Description of the computational tests

We ran minimizeABC2(n) for n ranging from 4 to 16. For each order.


Realizamos experimentos computacionais em grafos bicíclicos de até 16 vértices para caracterizar os grafos com o índice mínimo e máximo de Graovac-Ghorbani. Esses grafos foram gerados usando o pacote Nauty-Traces que gera os grafos em formato graph6. Os índices ABC_ {GG} foram computados no software BlueJ. 

Para validar nossos testes, preparamos então o código fonte abaixo na linguagem python que pode ser testado no link www.cocalc.com. 

Primeiramente, é necessário fazer o upload de todos os arquivos anexos na plataforma, que considera todos os grafos biciclicos para n=4,5,...,16. Após isto, abra um novo projeto em branco, e solicite um novo 'sagews'. Agora, basta apenas copiar e colar o seguinte código abaixo e realizar os testes, de acordo com o número *n* de vértices. 

```
ficheiro = open(arquivo.csv) #exemplo: bic5.csv
reader = ficheiro.readlines()
n=5 #number of vertices of graph
for i in reader:
    G=Graph(i.strip())
    graus = G.degree_sequence()
    graus.sort(reverse=True)
    Dist = G.distance_matrix()
    abc2=0
    di=0
    dj=0
    for i in range(n):
        for j in range(n):
            if (Dist[i][j]==1):
                di=0
                dj=0
                for k in range(n):
                    if (Dist[i][k] > Dist[j][k]):
                        di=di+1
                    if (Dist[i][k] < Dist[j][k]):
                        dj=dj+1
                abc2= abc2 + sqrt((di+dj-2)/(di*dj))
    abc2=(abc2/2)
    G.show()
    print 'abc2 = =', float(abc2)
```




