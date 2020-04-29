# Geração de grafos bicíclicos extremais em relação ao Índice ABC_GG

Descrevemos logo abaixo, o código fonte bem como anexamos os arquivos de teste referente aos grafos bicíclicos descrito no nosso artigo de nome: *On the Graovac-Ghorbani index for bicyclic graphs with no pendant vertices*. 

O nosso objetivo é corroborar com a pesquisa e ratificar todos os testes computacionais realizados neste trabalho e demais trabalhos futuros de pesquisadores. 

## Testes computacionais

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




