# HOW To using
# type this ======> python join_img_label.py <=======

import argparse
import os,errno
import string
import sys

def parse_arguments():
    """
        Parse the command line arguments of the program
    """

    parser = argparse.ArgumentParser(description='Join label to txt file')
    parser.add_argument(
        "-i",
        "--input_file",
        type=str,
        help="When set, this argument uses a specified text file as source for the text",
        default="test.txt"
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        help="generate txt string line to count num",
        default=10
    )
    
    return parser.parse_args()

def create_strings_from_file(filename, count):
    """
        Create all strings by reading lines in specified files
    """

    strings = []

    with open('original_text/'+filename, 'r', encoding="utf8") as f:
        lines = [l[0:200] for l in f.read().splitlines() if len(l) > 0]

        if len(lines) == 0:
            raise Exception("No lines could be read in file")

        while len(strings) < count:
            if len(lines) >= count - len(strings):
                strings.extend(lines[0:count - len(strings)])
            else:
                strings.extend(lines)

    print("Create string")
    return strings

def join_string_to_string(filename,strings):
    """
        Create file that have joined string
    """

    # Format 1 : img-000001.jpg [data]
    with open('copy_text/new_'+filename,'w',encoding="utf8") as f:
        i = 0
        for s in strings:
            data = 'img-'+str(i).zfill(6)+'.jpg '+s +'\n'
            f.write(data)
            i += 1  #index incresement 1++
    
    print("Make text file")

def main():
    """
        Description: Main function
    """
    # Argument parsing
    args = parse_arguments()

    # Create the directory if it does not exist.
    try:
        os.makedirs('copy_text')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    strings = create_strings_from_file(args.input_file, args.count)
    join_string_to_string(args.input_file, strings)

if __name__ == '__main__':
    main()
