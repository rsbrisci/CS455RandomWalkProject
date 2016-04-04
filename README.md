# CS455RandomWalkProject
NOT YET FEATURE COMPLETE

The purpose of this project is to examine the performance consequences of using random-walk based algorithms in p2p filesharing networks.

## Requirements
1. Python https://www.python.org/downloads/
2. R-Base https://cran.cnr.berkeley.edu/

## Usage
```
python SimulateP2PNetwork.py -h

usage: SimulateP2PNetwork.py [-h] [-t T] [-e E] vertices {randomwalk,normal}

Simulates a P2P network with random dynamic connectivity and examines runtime and space complexity of varius algorithms.

positional arguments:
  vertices             Number of vertices in the simulated network (Recommend
                       <= 1000)
  {randomwalk,normal}  Choose an algorithm to use in the simulation

optional arguments:
  -h, --help           show this help message and exit
  -t T                 (Default 50) Number of trials to run per graph (with
                       same edges)
  -e E                 (Default 100) Number of times graph will be re-built
                       with new edges

Examples:

python SimulateP2PNetwork.py 30 randomwalk
This will simulate a network of 30 vertices and use the random walk algorithm.

python SimulateP2PNetwork.py 500 normal -t 20
This will simulate a network of 500 verticies, using the normal algorithm, and run a new trial (assign new start and end nodes) on each graph 20 times.

python SimulateP2PNetwork.py 350 randomwalk -t 30 -e 200
This will simulate a network of 500 verticies, using the normal algorithm, run a new trial (assign new start and end nodes) on each graph 30 times and re-build (assign new edges) the graph 200 times.

Output: a csv in the following form (one line per run);
num vertices, num edges, algorithm used, length of path found, space needed per host (in vertices)
Ex:
300,543,randomwalk,102,40
300,543,randomwalk,34,13
300,50000,randomwalk,4000,443
.
.
.
```

###### Credit Github User: bwbaugh for the random connected graph generation script "random_connected_graph.py"!
