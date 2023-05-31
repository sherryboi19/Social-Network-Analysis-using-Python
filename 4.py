import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Read the data and add edges to the graph
with open('D:\\Graph_A.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# FindING the communities using the asyn_lpa_communities method
communities = nx.algorithms.community.asyn_lpa_communities(G)

# assign a unique color to each community and make list of communities
communtiteslist=[]
colors = {}
for i, community in enumerate(communities):
    communtiteslist.append(community)
    for node in community:
        colors[node] = i
# Printing Communities
print(communtiteslist)
# Draw the graph with nodes colored by community
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=[colors[node] for node in G.nodes()])
nx.draw_networkx_edges(G, pos)
plt.title("Communitties in Graph AB")
plt.show()
