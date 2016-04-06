#include "optionparser.h"
#include <iostream>

enum  optionIndex { UNKNOWN, HELP, PLUS };
const option::Descriptor usage[] =
{
  {UNKNOWN, 0,"", "",option::Arg::None, "USAGE: example [options]\n\n"
   "Options:" },
  {HELP,    0,"", "help",option::Arg::None, "  --help  \tPrint usage and exit." },
  {PLUS,    0,"p", "plus",option::Arg::None, "  --plus, -p  \tIncrement count." },
  {UNKNOWN, 0,"",  "",option::Arg::None, "\nExamples:\n"
   "  example --unknown -- --this_is_no_option\n"
   "  example -unk --plus -ppp file1 file2\n" },
  {0,0,0,0,0,0}
};

int main(int argc, char *argv[])
{

  return 0;
}
