# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 02:21:54 2014

@author: vamsi
"""

infile = open('map.txt', 'rt')
lines = infile.read().splitlines()
infile.close()
array = []
array_index = []
j = 0
l = 0
lat = []
lon = []
way_count =0

for i in range(len(lines)):
    if lines[i][0:3] != 'Way':
        array.append(lines[i])
        
nodes_dict = {}
nodes_dict_rev = {}
for k in range(len(array)):
    if (array[k] not in nodes_dict.values()):
        nodes_dict[l] = array[k]
        nodes_dict_rev[array[k]] = l
        l = l+1
        
#file = open("output.txt", "wt")
for m in range(len(nodes_dict)):
    latlon = nodes_dict[m].split(', ')
    lat.append(float(latlon[0]))
    lon.append(float(latlon[1]))
print sorted(lat)
print '\n\n\n\n', sorted(lon)
#print sorted(lat)[0], sorted(lat)[len(lat)-1],sorted(lon)[0], sorted(lon)[len(lon)-1]
##    print m, lat, lon
#    file.write('\n <node id=%d visible="true" version="5" changeset="15966089" timestamp="2013-05-03T21:19:45Z" user="Avi Flamholz" uid="753896" lat=%f lon=%f>' %(m, lat, lon))

"""for i in range(len(lines)):
    if lines[i][0:3] == 'Way':
        way_count = way_count + 1
        file.write('\n </way>\n <way id="%d" visible="true" version="1" changeset="21163108" timestamp="2014-03-17T20:58:06Z" user="Rub21_nycbuildings" uid="1781294">' %(way_count))
    else:
        file.write('\n  <nd ref="%d"/>' %(nodes_dict_rev[lines[i]]))

file.close()"""
