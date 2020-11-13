import math
import networkx as nx

G = nx.Graph()                               #Creating an empty graph
H = nx.Graph()

#function*****************************
def calculate_distance(coord1, coord2):
    """ Return the distance between two geographical points. """

    deg2rad = math.pi / 180
    phi1 = (90.0 - coord1[0]) * deg2rad
    phi2 = (90.0 - coord2[0]) * deg2rad

    th1 = coord1[1] * deg2rad
    th2 = coord2[1] * deg2rad

    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(th1 - th2) + \
           math.cos(phi1) * math.cos(phi2))
    # cos = (math.sin(phi1) * math.sin(phi2) + math.cos(th1 - th2) * \
    #        math.cos(phi1) * math.cos(phi2))

    if cos > 1:
       cos = 1

    distance = math.acos(cos) * 6373

    return distance
#function end ***************************

infile = open('positions.txt', 'rt')
lines = infile.read().splitlines()
infile.close()

l = 0
nodes_dict = {}                                 #Creating a node dictionary
for i in range(len(lines)):
    if (lines[i] not in nodes_dict.values()):
        nodes_dict[l] = lines[i]
        l = l+1

for i in range(len(nodes_dict)):                #Creating Graph by all nodes from dict
    G.add_node(i)

nodes_dict_tuples = {}                          #Creating another dict with cood as tuple
for i in range(len(nodes_dict)):
    latlonrank = nodes_dict[i].split(', ')
    lat = float(latlonrank[0])
    lon = float(latlonrank[1])
    cood = (lat,lon)
    nodes_dict_tuples[i] = cood

print "Approximate range of router in outdoors is 60 meters""\n"
dis = int(raw_input("Enter router range in meters: "))  # Reading range from user
diskm = float(dis)/1000                         #Converting dis to float for division

for i in range(len(nodes_dict)):                #Creating edges if distance less than connectable distance
    for j in range(i+1,len(nodes_dict)):
        if(calculate_distance(nodes_dict_tuples[i],nodes_dict_tuples[j])< diskm):
            G.add_edge(i,j)    

#unsorted_nodes = range(62)
#sorted_nodes = sorted(unsorted_nodes, key = int(latlonrank[2]))
sorted_nodes = []                               #Creating a list with sorted node weights
for i in range(1,5):
    for j in range(len(nodes_dict)):
        if int(nodes_dict[j].split(', ')[2]) == i:
            sorted_nodes.append(j)
            
count = 0
for i in range(len(sorted_nodes)):              #Removing nodes one by one and checking if graph is connected or not
    list_nodes = G.nodes()
    list_edges = G.edges()
    for j in range(len(list_nodes)):            #Making a copy of graph in other memory location
        H.add_node(list_nodes[j])
    for k in range(len(list_edges)):
        H.add_edge(list_edges[k][0],list_edges[k][1])                  
    H.remove_node(sorted_nodes[i])
    if nx.is_connected(H) == True:
        G.remove_node(sorted_nodes[i])

print "Total Number of Nodes:", (len(G.nodes()))
print G.nodes()
