# -*- coding: utf-8 -*-

# regular
import sys
import os
import argparse
import json
from gems import composite
from functools import partial
import types

from . import __version__
import __init__ as library


# parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


# version
parser_version = subparsers.add_parser('version')
parser_version.set_defaults(func=lambda x: sys.stderr.write(__version__ + '\n'))


# subcommands
def run(args, func=len):
    largs, kwargs = [], {}
    for arg in args.args:
        if arg.count('=') == 1:
            k, v = arg.split('=')
            try:
                v = float(v)
            except ValueError:
                pass
            kwargs[k] = v
        else:
            largs.append(arg)
    print func(*largs, **kwargs)
    return


for name in dir(library):
    command = getattr(library, name)
    if name[0] != '_' and isinstance(command, types.FunctionType):
        sub = subparsers.add_parser(name)
        sub.add_argument('args', nargs='+', help='Arguments to sequtils method.')
        subrun = partial(run, func=command)
        sub.set_defaults(func=subrun)


# exec
def main():
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
