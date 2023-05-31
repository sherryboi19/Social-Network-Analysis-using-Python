import networkx as nx
from tabulate import tabulate

# create an empty graph
GA = nx.Graph()
GB = nx.Graph()
GAB = nx.Graph()

# read the data and add edges to the graph
with open('D:\\Graph_A.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        GA.add_edge(u, v)
with open('D:\\Graph_B.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        GB.add_edge(u, v)
with open('D:\\Graph_AB.txt', 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        GAB.add_edge(u, v)

# Compute the Measures

# a. Average Degree
# Graph A
sum_degree_A=0
for n,d in GA.degree():
    sum_degree_A+=d
avg_degree_A=sum_degree_A/len(GA)
# Graph B
sum_degree_B=0
for n,d in GB.degree():
    sum_degree_B+=d
avg_degree_B=sum_degree_B/len(GB)
# Graph AB
sum_degree_AB=0
for n,d in GAB.degree():
    sum_degree_AB+=d
avg_degree_AB=sum_degree_AB/len(GAB)

# b. Average Clustering Coefficient
avg_cluster_coef_A = nx.average_clustering(GA)
avg_cluster_coef_B = nx.average_clustering(GB)
avg_cluster_coef_AB = nx.average_clustering(GAB)

# c. Average Path Length
avg_path_length_A = nx.average_shortest_path_length(GA)
avg_path_length_B = nx.average_shortest_path_length(GB)
avg_path_length_AB = nx.average_shortest_path_length(GAB)

# d. Diameter
diameter_A = nx.diameter(GA)
diameter_B = nx.diameter(GB)
diameter_AB = nx.diameter(GAB)

# e. Highest Degree Node
highest_degree_node_A = max(GA.degree(), key=lambda x: x[1])
highest_degree_node_B = max(GB.degree(), key=lambda x: x[1])
highest_degree_node_AB = max(GAB.degree(), key=lambda x: x[1])

# f. Lowest Degree Node
lowest_degree_node_A = min(GA.degree(), key=lambda x: x[1])
lowest_degree_node_B = min(GB.degree(), key=lambda x: x[1])
lowest_degree_node_AB = min(GAB.degree(), key=lambda x: x[1])

# Making Table to Compare 
data=[["Avg Deg",avg_degree_A,avg_degree_B,avg_degree_A], 
        ["Avg CC", avg_cluster_coef_A, avg_cluster_coef_B, avg_cluster_coef_AB], 
        ["Avg Path Len", avg_path_length_A, avg_path_length_B, avg_path_length_AB], 
        ["Diameter", diameter_A, diameter_B, diameter_AB],
        ["Highest Deg", highest_degree_node_A, highest_degree_node_B, highest_degree_node_AB],
        ["Lowest Deg",lowest_degree_node_A, lowest_degree_node_B, lowest_degree_node_AB]]
col_names = ["Measure", "Graph A", "Graph B", "Graph AB"]

#Printing the Table
print(tabulate(data, headers=col_names, tablefmt="pretty"))















