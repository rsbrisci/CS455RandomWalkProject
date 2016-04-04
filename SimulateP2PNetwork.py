# Author:
#   Ross Sbriscia, April 2016
import random
import sys
# Creates an empty graph with a number of supplied verticies
def createNetwork(numVerticies):
    network = {};
    index = 0;
    while (index < numVerticies):
        network[index] = [];
        index += 1;
    return network;

# Returns a connected graph with randomized edges.
# This simulates the reality of real p2p networks,
# as hosts very often come online and go offline.
def randomizeEdges(network):
    for node in network.iteritems():
        node.append()
    return network;

randomizeEdges(createNetwork(4));
