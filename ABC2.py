def ABC2(G):
    n = G.order()
    Dist = G.distance_matrix()
    count_abc2 = 0
    ni=0
    nj=0
    for i in range(n):
        for j in range(i+1,n):
            if (Dist[i][j]==1):
                ni=0
                nj=0
                for k in range(n):
                    if (Dist[i][k] > Dist[j][k]):
                        nj=nj+1
                    if (Dist[i][k] < Dist[j][k]):
                        ni=ni+1
                x = float(ni+nj-2)
                y = float(ni*nj)
                count_abc2 = count_abc2 + sqrt(x/y)
    return(count_abc2)
