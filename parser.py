def get_parameters_from_name(name):
    '''
        Gets matrix's parameters from file name.
    '''
    r1 = name.split(".")
    t = int(r1[1])
    r2 = r1[2].split("^")
    v = int(r2[0])
    k = int(r2[1])
    return t, v, k

def parse_line_into_vector(line):
    '''
        Parses one line of the file
    '''
    return ['0' if x == '-' else x for x in line.split()]

def read_file_to_array(fileName):
    '''
        Parses the array from an input file.
        Also returns the t.
    '''
    array = []
    f = open(fileName, 'r')
    t = int(f.readline())
    for i in range(t):
        array.append(parse_line_into_vector(f.readline()))
    return t, array
