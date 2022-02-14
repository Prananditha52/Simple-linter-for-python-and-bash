import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("path", help="Filepath")
parser.add_argument("--show", help="outputs the line numbers and lines that start with tabs",
                    action="store_true")
parser.add_argument("--fix", help=" replaces the leading tabs with two spaces and outputs on stdout.",
                    action="store_true")
args = parser.parse_args()
test = open(args.path)
if args.show:
    count=0
    for line in test:
        line=line.rstrip()
        count+=1
        if re.search('^\t',line):
            print("["+str(count)+"]"+line)
if args.fix:
    for line in test:
        line=line.rstrip()
        if re.search('^\t',line):
            txt=re.sub('^\t',"  ",line,)
            print(txt)
        else:
            print(line)


