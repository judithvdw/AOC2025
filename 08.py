import math
import networkx as nx
from utils.parsing import parse_ints
from itertools import combinations
from math import prod

with open('inputs/d8.txt') as f:
    coords = parse_ints(f.read().splitlines())

G_all = nx.Graph()
for i, j in combinations(coords, 2):
    G_all.add_edge(i, j, weight=math.dist(i, j))

edges = sorted(G_all.edges(data=True), key=lambda x: x[2]['weight'])

G = nx.Graph()
G.add_nodes_from(coords)
i = 0

while not nx.is_connected(G):
    u, v, d = edges[i]
    G.add_edge(u, v, weight=d['weight'])
    i += 1
    if i == 1000:
        comps = sorted(nx.connected_components(G), key=len, reverse=True)
        print(prod(len(c) for c in comps[:3]))

print(u[0] * v[0])
