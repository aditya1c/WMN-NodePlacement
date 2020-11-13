import math
import networkx as nx

G = nx.Graph()                               #Creating an empty graph
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

infile = open('nodes.txt', 'rt')
lines = infile.read().splitlines()
infile.close()

l = 0
nodes_dict = {}                                 #Creating a node dictionary
for i in range(len(lines)):
    if (lines[i] not in nodes_dict.values()):
        nodes_dict[l] = lines[i]
        l = l+1

posfile = open('positions.txt', 'wt')
for i in range(len(nodes_dict)):
    posfile.write(nodes_dict[i])
    posfile.write('\n')
posfile.close()

for i in range(len(nodes_dict)):                #Creating Graph by all nodes from dict
    G.add_node(i)

nodes_dict_tuples = {}                          #Creating another dict with cood as tuple
for i in range(len(nodes_dict)):
    latlon = nodes_dict[i].split(', ')
    lat = float(latlon[0])
    lon = float(latlon[1])
    cood = (lat,lon)
    nodes_dict_tuples[i] = cood

for i in range(len(nodes_dict)):                #Creating edges if distance less than 0.1 km
    for j in range(i,len(nodes_dict)):
        if(calculate_distance(nodes_dict_tuples[i],nodes_dict_tuples[j])<0.05):
            G.add_edge(i,j)    
