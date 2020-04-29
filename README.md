# Geração de grafos bicíclicos extremais em relação ao Índice ABC_GG

Este é um arquivo que contém o código e os arquivos de teste referente aos grafos bicíclicos que acompanham nosso artigo de nome: *On the Graovac-Ghorbani index for bicyclic graphs with no pendant vertices*. 

O objetivo deste arquivo é corroborar com a pesquisa e ratificar todos os testes computacionais realizados neste trabalho e demais trabalhos futuros de pesquisadores. 

## Testes computacionais

Realizamos experimentos computacionais em grafos bicíclicos de até 16 vértices para caracterizar os grafos com o índice mínimo e máximo de Graovac-Ghorbani. Esses grafos foram gerados usando o pacote Nauty-Traces e estão em código g6, no formato 'csv'. Os índices $ABC_ {GG}$ foram computados no software BlueJ. 

Para validar nossos testes, preparamos então o código fonte abaixo na linguagem python que pode ser testado no link www.cocalc.com gerando um novo projeto em branco e apenas copiando e colando o seguinte código:

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




