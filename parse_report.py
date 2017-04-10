import sys

def main():

    filename = sys.argv[1]
    report_file = open(filename, 'r')
    line = report_file.readline()

    while line:
        splitLine = line.split(" ")
        if (splitLine[0] == "Total"):
            print line,
        line = report_file.readline()

    report_file.close()

main()
