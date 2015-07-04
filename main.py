'''
    Main file to use the library.
'''
from parser import read_file_to_array
from parser import get_parameters_from_name
from validator import covers
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python main.py <input_file>"
        sys.exit()
    filename = sys.argv[1]
    N, array = read_file_to_array(filename)
    t, v, k = get_parameters_from_name(filename)
    print "Valid" if covers(array, v, k, N) else "Invalid"
