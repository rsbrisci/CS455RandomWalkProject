# Author:
#   Ross Sbriscia, April 2016
import random
import sys
import os
# Creates an empty graph with a number of supplied verticies


def createNetwork(numVerticies):
    network = {};
    index = 0;
    while (index < numVerticies):
        network[index] = [];
        index += 1;
    return network;

os.system("script2.py 1")
# Returns a connected graph with randomized edges.
# This simulates the reality of real p2p networks,
# as hosts very often come online and go offline.
