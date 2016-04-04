# Author:
#   Ross Sbriscia, April 2016
import random
import sys
import traceback
import os
import math


def maxEdges(n):
    return (n * (n - 1)) / 2

# Returns a connected graph with randomized edges.
# This simulates the reality of real p2p networks,
# as hosts very often come online and go offline.


def generateNetwork(numVerticies):
    edges = random.randrange(numVerticies - 1, maxEdges(numVerticies))
    print "Generating a graph with %d vertices and %d edges..." % (numVerticies, edges)
    os.system("python random_connected_graph.py -p -e " +
              str(edges) + " " + str(numVerticies) + " > edges.txt")
    print "Done!"

try:
    generateNetwork(int(sys.argv[1]))
except (ValueError, IndexError):  # In case of keyboard cat
    print '\033[91m' +"\nThis call takes a single integer (Number of Verticies) as argument\n" + '\033[0m'
    traceback.print_exc(file=sys.stdout)
