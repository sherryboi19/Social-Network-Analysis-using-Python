import networkx as nx
import matplotlib.pyplot as plt

# create an empty graph
G = nx.Graph()

# read the data and add edges to the graph
with open('D:\\Graph_A.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# compute the degree distribution
degree_freq = nx.degree_histogram(G)
# Making Cumulative Degree Frequency 
cumm_degree_freq=list()
cumm_degree_freq.append(degree_freq[0])
lenth=len(degree_freq)
for i in range(1,lenth):
    cumm_degree_freq.append(cumm_degree_freq[i-1]+degree_freq[i])
degree_values = range(len(cumm_degree_freq))
plt.figure(figsize=(10, 5))
plt.plot(degree_values, cumm_degree_freq, 'ro-')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Cummulative Degree Distribution')

# compute the clustering coefficient distribution
cc_freq = list(nx.clustering(G).values())
# Making Cumulative Clustering Coefficient
cumm_cc_val=list()
cumm_cc_val.append(cc_freq[0])
lenthcc=len(cc_freq)
for i in range(1,lenthcc):
    cumm_cc_val.append(cumm_cc_val[i-1]+cc_freq[i])  
cc_hist =  range(len(cumm_cc_val))
plt.figure(figsize=(10, 5))
plt.plot(cumm_cc_val, cc_hist, 'bo-')
plt.xlabel('Clustering coefficient')
plt.ylabel('Frequency')
plt.title('Cummulative Clustering Coefficient Distribution')

# compute the path length distribution with frquencies
pl_freq = {}
for source in G.nodes():
    path_lengths = nx.shortest_path_length(G, source=source)
    for target in path_lengths:
        pl = path_lengths[target]
        if pl in pl_freq:
            pl_freq[pl] += 1
        else:
            pl_freq[pl] = 1            
pl_values = range(max(pl_freq.keys()) + 1)
# Making Cumulative Path Length Frequency
cumm_pl_freq=list()
cumm_pl_freq.append(pl_freq.get(0))
lenpl=len(pl_values)
for i in range(1,lenpl):
    cumm_pl_freq.append(cumm_pl_freq[i-1]+pl_freq.get(i))
    
pl_hist = [pl_freq.get(x, 0) for x in pl_values]
plt.figure(figsize=(10, 5))
plt.plot(pl_values, cumm_pl_freq, 'go-')
plt.xlabel('Path length')
plt.ylabel('Frequency')
plt.title('Cummulative Path length distribution')

# show the plots
plt.show()
