# CS455RandomWalkProject
NOT YET FEATURE COMPLETE

The purpose of this project is to examine the performance consequences of using random-walk based algorithms in p2p filesharing networks.

## Requirements
1. Python https://www.python.org/downloads/
2. R-Base https://cran.cnr.berkeley.edu/

## Usage
```
python SimulateP2PNetwork.py -h
usage: SimulateP2PNetwork.py [-h] [-r R] [-e E] [-t T]
                             vertices {randomwalk,normal}

Simulates a P2P network with random dynamic connectivity in order to examines runtime and space complexity of search algorithms.

positional arguments:
  vertices             Number of vertices in the simulated network (Recommend
                       <= 1000)
  {randomwalk,normal}  Choose an algorithm to use in the simulation

optional arguments:
  -h, --help           show this help message and exit
  -r R                 (Default 10) Number of RUNS per EXPERIMENTS (exact same
                       start and end nodes, on network with same edges)
  -e E                 (Default 50) Number of EXPERIMENTS per TRIAL (new start
                       and end nodes, on network with same edges)
  -t T                 (Default 100) Number of TRIALS (times graph will be re-
                       built with new edges)

Examples:

python SimulateP2PNetwork.py 30 randomwalk
This will simulate a network of 30 vertices and use the random walk algorithm.

python SimulateP2PNetwork.py -e 20 500 normal
This will simulate a network of 500 verticies, using the normal algorithm, and run a new experiment (assign new start and end nodes) on each graph 20 times.

python SimulateP2PNetwork.py -t 30 -e 200 350 randomwalk
This will simulate a network of 500 verticies, using the randomwalk algorithm, run a new trial (assign new start and end nodes) on each graph 30 times and re-build (assign new edges) the graph 200 times.

Output: a csv in the following form (one line per RUN);
num vertices, num edges, algorithm used, average length of path found, space needed per host (in vertices)
Ex:
300,543,randomwalk,102,40
300,543,randomwalk,34,13
300,1120,randomwalk,3,443
.
.
.
```

###### Credit Github User: bwbaugh for the random connected graph generation script "random_connected_graph.py"!
