#!/usr/bin/python3

'''
  -h, --help            show this help message and exit,
  -p PATH, --path PATH  path of the direcotry, default path is "."
  -r, --relative        Print relative path instead of absolute
'''

import argparse

from glob import iglob
from os.path import realpath, isfile

def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', '--path', action='store', default=".",
                       help='''path of the direcotry''')

    parse.add_argument('-r', '--relative', action='store_true', default=False,
                       help='''Print relative path instead of absolute''')
    return parse.parse_args()


def get_first_line(file_):
    with open(file_) as f:
        data = f.readlines()
    if data:
        return data[0].strip()
    else:
        return ' '

def get_meta_data(file_, path, relative=True):
    meta = {}
    if not relative:
        meta['path'] = realpath(file_)
    else:
        meta['path'] = file_

    if isfile(file_):
        meta['data'] = get_first_line(file_)
        meta['type'] = 'file'
    else:
        meta['data'] = '-'
        meta['type'] = 'dir'
    return meta


def main():
    args = parse_args()
    path = args.path
    relative = args.relative

    print('{}{:>10}{:>70}'.format("Type",
                                  "Path",
                                  "Data"))
    for file_ in iglob('{}/**'.format(path), recursive=True):
        meta = get_meta_data(file_, path, relative)
        print('{}\t{:>10}{}{}'.format(meta['type'],
                                      meta['path'],"\t"*6,
                                      meta['data']))

if __name__ == '__main__':
    main()
