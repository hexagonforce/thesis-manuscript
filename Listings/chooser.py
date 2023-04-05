from sklearn.cluster import KMeans
import numpy as np
from pathlib import Path
import networkx as nx

# graph_files = List of graphml files from the ITZ

topo_names = []
X = []
for graph_file in graph_files:
    G = nx.read_graphml(graph_file)
    geoextent = G.graph['GeoExtent']
    if geoextent in ['Country', 'Region'] and nx.number_of_nodes(G) <= 40:
        X.append((nx.number_of_nodes(G), nx.number_of_edges(G)))
        topo_names.append(G.graph['Network'])

kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(X)
topo_to_cluster = dict(zip(topo_names, kmeans.labels_))

