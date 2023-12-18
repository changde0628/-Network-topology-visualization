import argparse
from traceroute import traceroute_main
from utilize import printLog
from genDiagram import GenDigraph

APP_Description = "This is a visual network topology tool for those who want to analyze and manage the overall network status. \
    It includes generating topology diagrams, \
    analyzing network status, and giving appropriate suggestions."

#initialize parser
parser = argparse.ArgumentParser(description=APP_Description)

# Adding optional argument
parser.add_argument("-d", "--dest", help = "Enter target domain name")
parser.add_argument("-n", "--name", help = "Enter the file name of the generated topology diagram")
parser.add_argument("-p", "--path", help = "Enter the storage path of the generated topology diagram")

args = parser.parse_args()

if __name__ == '__main__':
    try:
        if not args.name:
            args.name = 'log_traceroute'
        if not args.path:
            args.path = 'result'
        traceroute_main(args.dest,'./'+args.path+'/'+args.name+'.log')
        printLog('./'+args.path+'/'+args.name+'.log')
        GenDigraph('./'+args.path+'/'+args.name+'.log')
    except:
        print("Please enter the correct arguments!")