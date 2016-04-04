# Author:
#   Ross Sbriscia, April 2016
import random
import sys
import os
import math

def maxEdges(n):
    return (n*(n-1))/2;

# Returns a connected graph with randomized edges.
# This simulates the reality of real p2p networks,
# as hosts very often come online and go offline.
def generateNetwork(numVerticies):
    edges = random.randrange(numVerticies-1,maxEdges(numVerticies));
    print edges
    verticies = open('labels.txt', 'w');
    os.system("python random_connected_graph.py -p -e " + str(edges) + " " + str(numVerticies) + " > edges.txt");


generateNetwork(300);
