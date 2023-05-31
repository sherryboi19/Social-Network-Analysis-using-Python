import networkx as nx
import matplotlib.pyplot as plt
# Create an empty graph
G = nx.Graph()

# Read the data and add edges to the graph
with open('D:\\Graph_AB.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# Specifing myself, my friends, and friends of friends to remove
to_remove = set([639])
your_friends = set(G.neighbors(639))
friends_of_friends = set()
for friend in your_friends:
    friends_of_friends.update(G.neighbors(friend))
to_remove.update(your_friends, friends_of_friends)

# Remove the nodes to get the remaining graph
G.remove_nodes_from(to_remove)

# Check if the remaining graph is connected or not
if nx.is_connected(G):
    # if Connected, find the cut-vertex set
    cut_vertices = set(nx.articulation_points(G))
    print('Cut-vertex set:', cut_vertices)
else:
    # if Disconnected, find the connected components
    components = list(nx.connected_components(G))
    print('Connected components:', components)

nx.draw(G, with_labels=True)

# Show the graph
plt.show()