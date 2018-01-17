#include <iostream>
#include "optionparser.h"

enum  optionIndex { UNKNOWN, HELP, RUNS, EXPERIMENTS, TRIALS, OUTPUTNAME };
const option::Descriptor usage[] =
{
 {UNKNOWN, 0,"" , ""    ,option::Arg::None, "USAGE: example [options]\n\n"
                                            "Options:" },
 {HELP,    0,"" , "help",option::Arg::None, "  --help  \tPrint usage and exit." },
 {TRIALS,  0,"t", "trials",option::Arg::Optional, "  --trials, -t  \t(Default 100) Number of TRIALS (times graph will be re-built with new edges)" },
 {EXPERIMENTS,  0,"e", "experiments",option::Arg::Optional, "  --experiments, -e  \t(Default 50) Number of EXPERIMENTS per TRIAL (new start and end nodes, on network with same edges)" },
 {RUNS,  0,"r", "runs",option::Arg::Optional, "  --runs, -r  \t(Default 10) Number of RUNS per EXPERIMENTS (exact same start and end nodes, on network with same edges)" },
 {OUTPUTNAME,  0,"o", "output",option::Arg::Optional, "  --output, -o  \tSpecify output filename (end with .csv)" },
 {UNKNOWN, 0,"" ,  ""   ,option::Arg::None, "Examples:\n"
 "\n"
 "./SimulateP2PNetwork.py 30 randomwalk -o output.csv\n"
 "This will simulate a network of 30 vertices and use the random walk algorithm, outputs in output.csv\n"
 "\n"
 "./SimulateP2PNetwork.py 500 bfs -e 20\n"
 "This will simulate a network of 500 verticies, using the BFS algorithm, and run a"
 "new experiment (assign new start and end nodes) on each graph 20 times.\n"
 "\n"
 "./SimulateP2PNetwork.py 350 randomwalk -e 30 -t 200\n"
 "This will simulate a network of 500 verticies, using the randomwalk algorithm, run a"
 "new trial (assign new start and end nodes) on each graph 30 times and re-build (assign new edges) the graph 200 times.\n"
 "\n"
 "Output: a csv in the following form (one line per experiment);\n"
 "num vertices, num edges, algorithm used, average length of path found\n"
 "Ex:\n"
 "300,543,randomwalk,102,False\n"
 "300,543,randomwalk,34,False\n"
 "300,1120,randomwalk,3,True\n"
 ".\n"
 ".\n"
 "."},
 {0,0,0,0,0,0}
};

int main(int argc, char* argv[])
{
  argc-=(argc>0); argv+=(argc>0); // skip program name argv[0] if present
  option::Stats  stats(usage, argc, argv);
  option::Option *options = new option::Option[stats.options_max];
  option::Option *buffer = new option::Option[stats.buffer_max];
  option::Parser parse(usage, argc, argv, options, buffer);
  if (parse.error())
    return 1;

  if (options[HELP] || argc == 0) {
    option::printUsage(std::cout, usage);
    return 0;
  }

  for (option::Option* opt = options[UNKNOWN]; opt; opt = opt->next())
    std::cout << "Unknown option: " << opt->name << "\n";

  for (int i = 0; i < parse.nonOptionsCount(); ++i)
    std::cout << "Non-option #" << i << ": " << parse.nonOption(i) << "\n";
printf("It didnt work");
}
