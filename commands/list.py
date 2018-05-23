import argparse
import fs


def __args__(parser):
	parser.add_argument('-m','--message',default="",help="commit message")
	

def __exec__(args):
	fs.commit(message=args.message)

