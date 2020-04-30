## Description

The computational routines available here were useful to obtain the results and conjectures presented at the paper *On the Graovac-Ghorbani index for bicyclic graphs with no pendant vertices*. 

Our goal is to make all routines available and contribute to the academic commmunity in computing the Graovac Ghorbani index, which we will refer as ABC2. 

All routines are Python routines written in SageMath (cocalc.com).

Besides, a CSV file containing all bicyclic graphs of order from 4 to 16 is available.

## Graovac Ghorbani index routines for bicyclic graphs

The routines available are:

ABC2(G): compute the ABC2 index for a graph G given as an input.

minimizeABC2(nmin, nmax): return two lists: (i) list containing the G6 code of the graphs with minimal ABC2 among all bicyclic graphs of order from nmin to nmax; (ii) list containing the ABC2 index of the graphs with minimal ABC2 among all bicyclic graphs of order from nmin to nmax;

maximizeABC2(nmin, nmax): return two lists: (i) list containing the G6 code of the graphs with maximal ABC2 among all bicyclic graphs of order from nmin to nmax; (ii) list containing the ABC2 index of the graphs with maximal ABC2 among all bicyclic graphs of order from nmin to nmax;

## Computational experiments

We ran minimizeABC2(nmin, nmax) (resp. maximizeABC2(nmin, nmax)) for each order n ranging from 4 to 16 aiming to find the graphs with minimum (resp. maximum) ABC2 index among all biciclyc graphs of a given order. Both routines call the ABC2(G) routine to compute the ABC2 index of each generated graph.


## Example 1: Obtaining the graphs of orders n = 4,5,6 with minimal ABC2 index

load('minimizeABC2.py')

ListOfG6codes, fABC2 = minimizeABC2(4,6)

print ListOfG6codes[0] ## print G6 code of the graph of order nmin = 4

print fABC2 ## ABC2 index value for the graph of order nmin = 4

G = Graph(ListOfG6codes[0]) ### convert G6 code of a graph to an object graph G in Sage. 

G.show() ## displays the graph G of order nmin = 4





