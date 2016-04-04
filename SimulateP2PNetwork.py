# Author:
# Ross Sbriscia, April 2016
import random
import sys
import traceback
import os
import math
import argparse

# Parses Arguments
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
description='Simulates a P2P network with random dynamic connectivity in order to examines runtime \
and space complexity of search algorithms.',
epilog="Examples:\n\
\n\
python SimulateP2PNetwork.py 30 randomwalk\n\
This will simulate a network of 30 vertices and use the random walk algorithm.\n\
\n\
python SimulateP2PNetwork.py -e 20 500 normal\n\
This will simulate a network of 500 verticies, using the normal algorithm, and run a \
new experiment (assign new start and end nodes) on each graph 20 times.\n\
\n\
python SimulateP2PNetwork.py -t 30 -e 200 350 randomwalk\n\
This will simulate a network of 500 verticies, using the randomwalk algorithm, run a \
new trial (assign new start and end nodes) on each graph 30 times and re-build (assign new edges) the graph 200 times.\n\
\n\
Output: a csv in the following form (one line per RUN);\n\
num vertices, num edges, algorithm used, average length of path found, space needed per host (in vertices)\n\
Ex:\n\
300,543,randomwalk,102,40\n\
300,543,randomwalk,34,13\n\
300,1120,randomwalk,3,443\n\
.\n\
.\n\
.")
parser.add_argument('vertices', type=int,
                   help='Number of vertices in the simulated network (Recommend <= 1000)')
parser.add_argument('algorithm',choices=['randomwalk', 'normal'],
                   help='Choose an algorithm to use in the simulation')
parser.add_argument('-r', type=int,
                   help='(Default 10) Number of RUNS per EXPERIMENTS (exact same start and end nodes, on network with same edges)')
parser.add_argument('-e', type=int,
                   help='(Default 50) Number of EXPERIMENTS per TRIAL (new start and end nodes, on network with same edges)')
parser.add_argument('-t', type=int,
                   help='(Default 100) Number of TRIALS (times graph will be re-built with new edges)')
args = parser.parse_args()
# Code Starts Here!

# Returns the maximum possible number of edges of an undirected graph with n verticies
def maxEdges(n):
    return (n * (n - 1)) / 2;

# Returns a connected graph with randomized edges.
# This simulates the reality of real p2p networks,
# as hosts very often come online and go offline.
def generateNetwork(numVerticies):
    edges = random.randrange(numVerticies - 1, maxEdges(numVerticies));
    print "Generating a graph with %d vertices and %d edges..." % (numVerticies, edges);
    os.system("python random_connected_graph.py -p -e " +
              str(edges) + " " + str(numVerticies) + " > edges.txt");
    print "Done!";

try:
    generateNetwork(int(sys.argv[1]));
except (ValueError, IndexError):  # In case of keyboard cat
    print '\033[91m' +"\nThis call takes a single integer (Number of Verticies) as argument\n" + '\033[0m';
    traceback.print_exc(file=sys.stdout);
