"""
Dynamic topology
================
This example shows how to generate a topology, an event schedule and a traffic
matrix.
In this specific example we create a Waxman topology and create an event
schedule listing random link failures and restores and generate a static
traffic matrix.
This scenario could be used to assess the performance of a routing algorithm
in case of frequent link failures.
"""
import fnss
import random
import sys
import argparse
import traceback
import time
import math

# Parses Arguments
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='Creates the network used by SimP2PNetV2.py',
                                 epilog="Examples:\n\
\n\
python generate_network.py 2000\n\
Generates a network of 2,000 hosts, and an event_schedule of random failiures, outputs in XML form.\n\
\n\
python generate_network.py 0 -r\n\
Generates a new event_schedule for topology.xml\n\
.")
parser.add_argument('vertices', type=int,
                    help='Number of vertices in the simulated network (Recommend <= 1000)')
parser.add_argument('-r', action="store_true",
                    help='(Default 10) Number of RUNS per EXPERIMENTS (exact same start and end nodes, on network with same edges)')
args = parser.parse_args()
numberOfVertices = args.vertices

if args.r: # Output NEW EventSchedule
    topology = (fnss.read_topology("topology.xml"))
    def rand_failure(links):
        link = random.choice(links)
        return {'link': link, 'action': 'down'}

    # Create schedule of link failures
    event_schedule = fnss.poisson_process_event_schedule(
                            avg_interval=0.5,               # 0.5 min = 30 sec
                            t_start=0,                      # starts at 0
                            duration= 60,                   # 2 hours
                            t_unit='min',                   # minutes
                            event_generator= rand_failure,  # event gen function
                            links=topology.edges(),         # 'links' argument
                            )

    # Now let's create a schedule with link restoration events
    # We assume that the duration of a failure is exponentially distributed with
    # average 1 minute.
    restore_schedule = fnss.EventSchedule(t_start=0, t_unit='min')
    for failure_time, event in event_schedule:
        link = event['link']
        restore_time = failure_time + random.expovariate(1)
        restore_schedule.add(time=restore_time,
                             event={'link': link, 'action': 'up'},
                             absolute_time=True
                             )
    # Now merge failure and restoration schedules
    # After merging events are still chronologically sorted
    event_schedule.add_schedule(restore_schedule)
    fnss.write_event_schedule(event_schedule, 'event_schedule.xml')
else: # Make new everthing
    # generate a Waxman1 topology with numberOfVertices nodes
    topology = fnss.waxman_1_topology(n=numberOfVertices, alpha=0.2, beta=0.1, L=1)

    # assign constant weight (1) to all links
    fnss.set_weights_constant(topology, 1)

    # set delay equal to 1 ms to all links
    fnss.set_delays_constant(topology, 1, 'ms')

    # set varying capacities among 10, 100 and 1000 Mbps proprtionally to edge
    # betweenness centrality
    fnss.set_capacities_edge_betweenness(topology, [10, 100, 1000], 'Mbps')

    # Write topology, event schedule and traffic matrix to files
    fnss.write_topology(topology, 'topology.xml')
