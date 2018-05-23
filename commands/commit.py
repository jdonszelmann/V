import argparse
import fs


def __args__(parser):
	parser.add_argument('date',default=".",nargs='?',help="specifies in which directory V should initialize")


def __exec__(args):
	fs.list()

