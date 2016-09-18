#!/usr/bin/env python3

import io
import sys
import enchant
from argparse import ArgumentParser, FileType, Action

from checker import sanitizer, prompt

def generate_parser():
    parser = ArgumentParser(description='Process spell-check of an input file\
            and put the result in an output file')
    parser.add_argument('-i', '--input', metavar='INPUT', type=FileType('r'),
            help="input file", default=sys.stdin)
    parser.add_argument('-o', '--output', metavar='OUTPUT', type=FileType('w'),
            help="output file -- default stdout", default=sys.stdout)
    parser.add_argument('--lang', metavar='LANG', default='en_US',
            help="Specify the language to spell check")
    parser.add_argument('-l', '--list', help='Show available languages',
            action="store_true")
    return parser

class Writer:
    output = None
    buffer = ""

    def __init__(self, file):
        self.output = file

    def bufferize(self, content):
        self.buffer += content

    def flush(self):
        self.output.write(self.buffer)

def read_input(file):
    lines = file.read().splitlines()
    file.close()
    return lines

if __name__ == "__main__":
    parser = generate_parser()
    args = parser.parse_args()
    if args.list:
        print(enchant.list_languages())
        exit(0)

    lines = read_input(args.input)
    output = Writer(args.output)
    prompt = prompt.Prompt(lines)
    checker = enchant.Dict(args.lang)
    for line in lines:
        words = line.split(' ')
        index = 0
        for word in words:
            san = sanitizer.Sanitizer(word)
            if len(san.get_word()) > 0 and not checker.check(san.get_word()):
                prompt.prompt(san.get_word(), checker.suggest(san.get_word()))
            index += 1
            output.bufferize(san.get_prefix())
            output.bufferize(san.get_word())
            output.bufferize(san.get_suffix())
            if index != len(words):
                output.bufferize(' ')
        output.bufferize('\n')
    output.flush()
