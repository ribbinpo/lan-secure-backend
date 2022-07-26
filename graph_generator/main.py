from GraphGenerator import construct_graph
from Visualization import *

fileName = 'a004_20220210_000001'
stat, V, E = construct_graph('../assets/pcaps/'+fileName+'.pcap')
print(stat)
print(V)
print(E)
# visualize(V, E, fileName)
