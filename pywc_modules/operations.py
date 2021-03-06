import utils

def displayStat(statDict):
    """
        Display formated result into screen
        args :
            - statDict (dict): data to display
    """

    totalOccur = sum(occur for word, occur in statDict["wordcount"])

    print "\n"
    print "{:<20} : {:>6}".format("Number of lines", statDict["nbLines"])
    print "{:<20} : {:>6}".format("Number of words", statDict["nbWords"])
    print "{:<20} : {:>6}".format("Number of characters", statDict["nbChars"])
    print "\n"

    print "-" * 46
    print "{:^27} {:^7s} {:^10s}".format("WORD", "TIMES", "SCORE(%)")
    print "-" * 46

    for word, occur in statDict["wordcount"]:
        print "{:<27} {:>7d} {:>10.2f}".format(word, occur, float(occur * 100)/totalOccur)

    print "\n"

def exportStat(statDict, outputfile):
    """
        Export stat to csv
        args :
            - statDict (dict) : data to export
            - outputfile (string) : output file's path
    """

    import csv

    totalOccur = sum(occur for word, occur in statDict["wordcount"])

    with open(outputfile, "w") as outputcsvfile:
        fieldnames = ["WORD", "TIMES", "SCORE%"]
        writer = csv.DictWriter(outputcsvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, occur in statDict["wordcount"]:
            writer.writerow({"WORD": word, "TIMES": occur, "SCORE%": float(occur * 100)/totalOccur})

        statWriter = csv.writer(outputcsvfile, delimiter=',')
        statWriter.writerow(['', '', ''])
        statWriter.writerow(['Number of lines', statDict["nbLines"]])
        statWriter.writerow(['Number of words', statDict["nbWords"]])
        statWriter.writerow(['Number of characters', statDict["nbChars"]])

def filterStatDict(statDict, arguments):
    """
        Return filtered result according to arguments
        args :
            - statDict (dict) : data to filter
            - arguments (dict) : contains word length and word occurence
        Return : dict
    """

    filteredStatDict = {
        "nbLines": statDict["nbLines"],
        "nbWords": statDict["nbWords"],
        "nbChars": statDict["nbChars"],
    }
    filtredWordcountList = []

    # Set default word length to display to 2
    if not arguments.has_key("lengthword"):
        arguments["lengthword"] = 2

    if arguments.has_key("lengthword") and arguments.has_key("wordoccur"):
        for word, occur in statDict["wordcount"]:
            if len(word) >= arguments["lengthword"] and occur >= arguments["wordoccur"]:
                filtredWordcountList.append((word, occur))
        filteredStatDict["wordcount"] = filtredWordcountList
        return filteredStatDict
    if arguments.has_key("lengthword"):
        for word, occur in statDict["wordcount"]:
            if len(word) >= arguments["lengthword"]:
                filtredWordcountList.append((word, occur))
        filteredStatDict["wordcount"] = filtredWordcountList
        return filteredStatDict
    if arguments.has_key("wordoccur"):
        for word, occur in statDict["wordcount"]:
            if occur >= arguments["wordoccur"]:
                filtredWordcountList.append((word, occur))
        filteredStatDict["wordcount"] = filtredWordcountList
        return filteredStatDict

    # if no filter was set, return all dict
    return statDict
