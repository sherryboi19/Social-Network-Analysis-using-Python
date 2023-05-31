import networkx as nx
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# create an empty graph
G = nx.Graph()

# read the data and add edges to the graph
with open('D:\\Graph_AB.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# Degree Centrality and Heatmap
deg_cent = nx.degree_centrality(G)
# Sorting data to make heatmap
nodedc=[]
valdc=[]
for node, value in sorted(deg_cent.items(), key=lambda x: x[1], reverse=True):
    nodedc.append(node)
    valdc.append(value)
nodedc=np.array(nodedc)
valdc=np.array(valdc)
nodedc=nodedc.reshape(5,19)
valdc=valdc.reshape(5,19)
# Ploting Heatmap
sns.heatmap(valdc,annot=nodedc,fmt="",cmap='RdYlGn',linewidths=0.30,annot_kws={"fontsize":7})
plt.title("Degree Centrality")
plt.show()

# Eigen Centrality and Heatmap
eig_cent = nx.eigenvector_centrality(G)
# Sorting data to make heatmap
nodeec=[]
valec=[]
for node, value in sorted(eig_cent.items(), key=lambda x: x[1], reverse=True):
    nodeec.append(node)
    valec.append(value)
nodeec=np.array(nodeec)
valec=np.array(valec)
nodeec=nodeec.reshape(5,19)
valec=valec.reshape(5,19)
# Ploting Heatmap
sns.heatmap(valec,annot=nodeec,fmt="",cmap='RdYlGn',linewidths=0.30,annot_kws={"fontsize":7})
plt.title("Eigen Centrality")
plt.show()

# Closeness Centrality and Heatmap
close_cent = nx.closeness_centrality(G)
# Sorting data to make heatmap
nodecc=[]
valcc=[]
for node, value in sorted(close_cent.items(), key=lambda x: x[1], reverse=True):
    nodecc.append(node)
    valcc.append(value)
nodecc=np.array(nodecc)
valcc=np.array(valcc)
nodecc=nodecc.reshape(5,19)
valcc=valcc.reshape(5,19)
# Ploting Heatmap
sns.heatmap(valcc,annot=nodecc,fmt="",cmap='RdYlGn',linewidths=0.30,annot_kws={"fontsize":7})
plt.title("Closeness Centrality")
plt.show()

#Betweenness Centrality abd Heatmap
betw_cent = nx.betweenness_centrality(G)
# Sorting data to make heatmap
nodebc=[]
valbc=[]
for node, value in sorted(betw_cent.items(), key=lambda x: x[1], reverse=True):
    nodebc.append(node)
    valbc.append(value)
nodebc=np.array(nodebc)
valbc=np.array(valbc)
nodebc=nodebc.reshape(5,19)
valbc=valbc.reshape(5,19)
# Sorting data to make heatmap
sns.heatmap(valbc,annot=nodebc,fmt="",cmap='RdYlGn',linewidths=0.30,annot_kws={"fontsize":7})
plt.title("Betweenness Centrality")
plt.show()

# PageRank and Heatmap
page_rank = nx.pagerank(G)
# Sorting data to make heatmap
nodepr=[]
valpr=[]
for node, value in sorted(page_rank.items(), key=lambda x: x[1], reverse=True):
    nodepr.append(node)
    valpr.append(value)
nodepr=np.array(nodepr)
valpr=np.array(valpr)
nodepr=nodepr.reshape(5,19)
valpr=valpr.reshape(5,19)
# Sorting data to make heatmap
sns.heatmap(valpr,annot=nodepr,fmt="",cmap='RdYlGn',linewidths=0.30,annot_kws={"fontsize":7})
plt.title("Page Rank")
plt.show()
