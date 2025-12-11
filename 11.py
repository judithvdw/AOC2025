import matplotlib.pyplot as plt
import networkx as nx

with open('inputs/d11.txt') as f:
    lines = f.read().splitlines()
    graph = {line.split()[0][:-1]: line.split()[1:] for line in lines}

G = nx.from_dict_of_lists(graph, create_using=nx.DiGraph)
print(len(list(nx.all_simple_paths(G, 'you', 'out'))))
