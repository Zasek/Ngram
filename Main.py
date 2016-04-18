#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from kai_1_gram_freq import one_gram_process
from kai_2_gram_freq import two_gram_process
from kai_3_gram_freq import thr_gram_process


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--one", help="Use one gram new word detection", action="store_true")
    parser.add_argument("--two", help="Use two gram new word detection", action="store_true")
    parser.add_argument("--three", help="Use three gram new word detection", action="store_true")
    parser.add_argument("-i", "--input", type=str, help="Input file name")
    parser.add_argument("-o", "--output", type=str, help="Output file name")

    args = parser.parse_args()
    if args.one:
        print("using one")
        print(" Input address: "+args.input)
        print(" Output address: "+args.output)
        one_gram_process(args.input, args.output)
        print("Finished!......")
    if args.two:
        print("using two")
        print(" Input address: "+args.input)
        print(" Output address: "+args.output)
        two_gram_process(args.input, args.output)
        print("Finished!......")
    if args.three:
        print("using three")
        print(" Input address: "+args.input)
        print(" Output address: "+args.output)
        thr_gram_process(args.input, args.output)
        print("Finished!......")
