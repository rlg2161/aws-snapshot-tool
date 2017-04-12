#!/usr/bin/env python

import sys
import json

def main():

    filename = sys.argv[1]
    report_file = open(filename, 'r')
    line = report_file.readline()

    report_dict = {}

    while line:
        splitLine = line.split(" ")
        if (splitLine[0] == "Total"):
            if "created" in line:
                report_dict['created'] = splitLine[-1].rstrip()
            if "errors" in line:
                report_dict['errored'] = splitLine[-1].rstrip()
            if "deleted" in line:
                report_dict['deleted'] = splitLine[-1].rstrip()
        line = report_file.readline()

    report_file.close()
    print "{\"text\": " + json.dumps(report_dict) + "}"

main()
