"""

USAGE: lua stats.lua [OPTIONS] [-g ACTIONS]
  
OPTIONS:
  -b  --bootstrap     bootstrap value                       = 512
  -c  --cliff         cliff's delta threshold               = .4
  -cf  --conf         conf value                            = 0.05
  -co  --cohen        cohen value                           = .35
  -F  --Fmt           float string formatting value         = "{:2.2f}"
  -w  --width         width value                           = 40
  -g  --go            start-up action                       = nothing
  -h  --help          show help                             = False
  -s  --seed          random number seed                    = 937162211
ACTIONS:
"""
import getopt
import re
import sys

import TestEngine


def coerce(s):
    "coerce a string to some type"
    s = s.strip()
    if s == "False":
        return False
    elif s == "True":
        return True
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return s


def get_default():
    global the
    p = r"\n[\s]+-[\S]+[\s]+--([\S]+)[^\n]+= ([\S]+)"
    for k, v in re.findall(p, __doc__):
        the[k] = coerce(v)
    # return t


def update(opts, t):
    for opt, arg in opts:
        if opt in ("-d", "--dump"):
            t['dump'] = coerce(arg)
        if opt in ("-g", "--go"):
            t['go'] = coerce(arg)
        if opt in ("-h", "--help"):
            t['help'] = coerce(arg)
        if opt in ("-s", "--seed"):
            t['seed'] = coerce(arg)
    return t


# Stores arguments in the variable
# use python3 Main.py --[options]
the = {}
if __name__ == "__main__":
    get_default()
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, ":dghs", ["dump=", "go=", "help=", "seed="])
    except getopt.GetoptError:
        print('Please provide appropriate arguments')
        sys.exit(2)
    the = update(opts, the)
    if the['help']:
        print(__doc__)
        sys.exit(2)
    sys.exit(TestEngine.run(the))
