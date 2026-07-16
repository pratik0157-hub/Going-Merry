#!/usr/bin/env python3

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="Enter the name of the city")
    args = parser.parse_args()
    return args.city