import sys

from collections import Counter
from pywc_modules.utils import *
from pywc_modules.operations import *


def main(arguments):
    if arguments.has_key("help"):
        print readfile("help.txt")
        sys.exit()

    statDict = {}
    filteredStatDict = {}

    fileContent = readfile(arguments["inputfile"])
    statDict["nbLines"] = len(fileContent.splitlines())
    statDict["nbChars"] = numberOfChar(fileContent.lower())

    # Removes non alphanumerical word
    word_list = stripNonAlphaNum(fileContent.lower())
    statDict["nbWords"] = len(word_list)

    # Count word and sort
    statDict["wordcount"] = Counter(word_list).most_common()

    # Filter result do display
    filteredStatDict = filterStatDict(statDict, arguments)

    if arguments.has_key("outputfile"):
        exportStat(filteredStatDict, arguments["outputfile"], statDict["nbWords"])
    else:
        displayStat(filteredStatDict, statDict["nbWords"])


if __name__ == "__main__":
    main(getargs(sys.argv[1:]))
