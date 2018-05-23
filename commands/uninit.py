import argparse
import fs

def __args__(parser):
	parser.add_argument('location',default=".",nargs='?',help="specifies in which directory V should initialize")
	

def __exec__(args):
	fs.remove_V_dir(args.location)

