import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-u', type=str, default=None)
args = parser.parse_args()
print (args.u)
