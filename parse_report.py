#!/usr/bin/env python

import sys
import json
import os

def main():

    filename = sys.argv[1]
    report_file = open(filename, 'r')
    line = report_file.readline()

    report_string = ""

    while line:
        splitLine = line.split(" ")
        if (splitLine[0] == "Total"):
            if "created" in line:
                report_string = report_string + "created: " + splitLine[-1].rstrip() + ",\n "
            if "errors" in line:
                report_string = report_string + "errored: " + splitLine[-1].rstrip() + ",\n "
            if "deleted" in line:
                report_string = report_string + "deleted: " + splitLine[-1].rstrip()
        line = report_file.readline()

    report_file.close()
    print "{\"text\": \"AWS SNAPSHOT TOOL:\n environment: " + os.environ['ENVIRONMENT'] + ",\n " + report_string + "\"}"

main()
