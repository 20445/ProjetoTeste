def maximizeABC2(nmin,nmax):
    load('ABC2.py')
    ExtremalGraphs = [] ### set the list of extremal graphs for each order
    fABC2 = [] ### set the list of the ABC2 index for each extremal graph
    ExtremalGraph6strings = [] ### set the list of G6 codes for extremal graphs of each order
    for n in range(nmin,nmax+1):
        Gnew = Graph()
        fABC2_new = 0
        for H in graphs.nauty_geng("%d %d:%d -c" %(n,n+1,n+1)):
            fABC2_H = ABC2(H)
            if fABC2_H > fABC2_new:
                Gnew = H
                fABC2_new = fABC2_H
        ExtremalGraphs.append(Gnew)
        fABC2.append(fABC2_new)
        G6code = Gnew.graph6_string()
        ExtremalGraph6strings.append(G6code)
    return(ExtremalGraph6strings,fABC2)