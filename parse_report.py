#!/usr/bin/env python

import sys
import json
import os
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

def main():

    filename = sys.argv[1]
    report_file = open(filename, 'r')
    line = report_file.readline()

    report_string = ""

    successfulBackup = True

    while line:
        splitLine = line.split(" ")
        if (splitLine[0] == "Total"):
            if "created" in line:
                report_string = report_string + "created: " + splitLine[-1].rstrip() + ",\n "
            if "errors" in line:
                report_string = report_string + "errored: " + splitLine[-1].rstrip() + ",\n "
                if (int(splitLine[-1].rstrip()) != 0):
                    successfulBackup = False
            if "deleted" in line:
                report_string = report_string + "deleted: " + splitLine[-1].rstrip()
        line = report_file.readline()

    report_file.close()
    print "{\"text\": \"AWS SNAPSHOT TOOL:\n environment: " + os.environ['ENVIRONMENT'] + ",\n " + report_string + "\"}"

    # Report successful backups to prometheus
    # Don't report unsuccessful ones... this ay we can alert on missing multiple reports in a row (easiest way to do it)
    if (successfulBackup):
        job_name = "AWS Snapshot Tool " + os.environ['ENVIRONMENT']
        registry = CollectorRegistry()
        g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
        g.set_to_current_time()
        push_to_gateway('prometheus:9091', job=job_name, registry=registry)

main()
