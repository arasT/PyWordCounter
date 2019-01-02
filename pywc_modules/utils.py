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

# Returns url text content
def readurl(urlsite):
    import urllib2
    import re, sys

    tagHtml = re.compile(r"<[^>]+>")
    page = None

    # Approprriate headers to avoid any 403 forbidden errors
    hdr = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
           "Accept-Encoding": "none",
           "Accept-Language": "en-US,en;q=0.8",
           "Connection": "keep-alive"}

    # Perform a HTTP request by passing URL and setting headers
    req = urllib2.Request(urlsite, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except:
        print "Error: Cannot open url: ", urlsite, " !"
        sys.exit(2)

    # Read the response
    content = page.read()

    # Delete uneeded content
    contentNoScript = re.sub(r"(\<script)\s*[^\>]*\>([^\<]*\<\/script>)", "", content)
    contentNoScriptAndStyles = re.sub("r(\<style)\s*[^\>]*\>([^\<]*\<\/style>)", "", contentNoScript)
    contentNoTags = tagHtml.sub("", contentNoScriptAndStyles)
    contentUnescaped = re.sub(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));", " ", contentNoTags)

    return contentUnescaped

# Returns number of char into a list of strigns
def numberOfChar(stringList):
    return sum(len(s) for s in stringList)

# Returns arguments into dict
def getargs(argv):
    import sys, getopt

    argsDict = {}
    try:
        opts, args = getopt.getopt(argv, "hi:u:l:n:o:", ["ifile=","url=", "lword=", "nword=", "ofile="])
    except getopt.GetoptError:
        print "main.py -i|-u <inputfile>|<url> -l <lengthword> -n <wordoccur> -o <outputfile>"
        sys.exit(2)
    if len(opts) == 0:
        print "main.py -i|-u <inputfile>|<url> -l <lengthword> -n <wordoccur> -o <outputfile>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            #print "main.py -i <inputfile> -l <lengthword> -n <wordoccur> -o <outputfile>"
            argsDict["help"] = "Display help"
        elif opt in ("-i", "--ifile"):
            argsDict["inputfile"] = arg
        elif opt in ("-u", "--url"):
            argsDict["url"] = arg
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
