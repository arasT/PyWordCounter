# Strips non alpha numeric char
def stripNonAlphaNum(text):
    import re
    return re.compile(r"\W+", re.UNICODE).split(text)

# Returns file content
def readfile(filepath):
    import os, sys

    if not os.path.isfile(filepath):
        print "File path : " ,filepath, " does not exist!"
        sys.exit(2)

    with open(filepath) as fp:
        return fp.read()

# Returns number of char into a list of strigns
def numberOfChar(stringList):
    return sum(len(s) for s in stringList)

# Returns arguments into dict
def getargs(argv):
    import sys, getopt

    argsDict = {}
    try:
        opts, args = getopt.getopt(argv, "hi:l:n:o:", ["ifile=","lword=", "nword=", "ofile="])
    except getopt.GetoptError:
        print "main.py -i <inputfile> -l <lengthword> -n <wordoccur> -o <outputfile>"
        sys.exit(2)
    if len(opts) == 0:
        print "main.py -i <inputfile> -l <lengthword> -n <wordoccur> -o <outputfile>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            #print "main.py -i <inputfile> -l <lengthword> -n <wordoccur> -o <outputfile>"
            argsDict["help"] = "Display help"
        elif opt in ("-i", "--ifile"):
            argsDict["inputfile"] = arg
        elif opt in ("-l", "--lword"):
            try:
                argsDict["lengthword"] = int(arg)
            except:
                print "Error: -l (--lword) argument must be a number!"
                sys.exit(2)
        elif opt in ("-n", "--nword"):
            try:
                argsDict["wordoccur"] = int(arg)
            except:
                print "Error: -n (--nword) argument must be a number!"
                sys.exit(2)
        elif opt in ("-o", "--ofile"):
            argsDict["outputfile"] = arg

    return argsDict