import argparse

APP_Description = "This is a visual network topology tool for those who want to analyze and manage the overall network status. \
    It includes generating topology diagrams, \
    analyzing network status, and giving appropriate suggestions."

#initialize parser
parser = argparse.ArgumentParser(description=APP_Description)

# Adding optional argument
parser.add_argument("-d", "--dest", help = "Enter target domain name")
parser.add_argument("-p", "--ping", help = "Enter target domain name")
parser.add_argument("-s", "--save", help = "Enter the storage path of the generated topology diagram")

args = parser.parse_args()

if __name__ == '__main__':
    if args.dest:
        print("Target domain name: %s" % args.dest)
    if args.ping:
        print("Target domain name: %s" % args.ping)
    if args.save:
        print("Target domain name: %s" % args.save)
