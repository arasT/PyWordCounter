import sys

from collections import Counter
from pywc_modules.utils import *
from pywc_modules.operations import *


def main(arguments):
    if arguments.has_key("help"):
        print readfile("help.txt")
        sys.exit()
    if arguments.has_key("inputfile") and arguments.has_key("url"):
        print "Error: Cannot have inputfile -i (--ifile) and url -u (--url) at the same time!"
        sys.exit(2)

    statDict = {}
    filteredStatDict = {}
    textData = ""

    if arguments.has_key("inputfile"):
        textData = readfile(arguments["inputfile"])
    else:
        textData = readurl(arguments["url"])

    statDict["nbLines"] = len(textData.splitlines())
    statDict["nbChars"] = numberOfChar(textData.lower())

    # Removes non alphanumerical word
    word_list = stripNonAlphaNum(textData.lower())
    statDict["nbWords"] = len(word_list)

    # Count word and sort
    statDict["wordcount"] = Counter(word_list).most_common()

    # Filter result do display
    filteredStatDict = filterStatDict(statDict, arguments)

    if arguments.has_key("outputfile"):
        exportStat(filteredStatDict, arguments["outputfile"])
    else:
        displayStat(filteredStatDict)


if __name__ == "__main__":
    main(getargs(sys.argv[1:]))
