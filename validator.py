from itertools import combinations
from multiprocessing import Pool

def get_column(matrix, c):
    '''
        Selects the column in position c.
    '''
    return [x[c] for x in matrix]

def columns_cover(args=[]):
    '''
        For the selected columns, check
        if they have all possible v-tuples.
    '''
    columns = args[0]
    v = args[1]
    t = args[2]
    found_combinations = []
    for i in range(t):
        input = [c[i] for c in columns]
        if input not in found_combinations:
            found_combinations.append(input)
    return len(found_combinations) == v**v

def covers(matrix, v, k, t):
    '''
        Given a matrix computes the covering
        check for all v-sets of columns.
    '''
    p = Pool(k)
    args = []
    for c in combinations([i for i in range(k)], v):
        c = list(c)
        args.append([[get_column(matrix, col) for col in c], v, t])
    validity = [p.map(columns_cover, args)]
    p.close()
    p.join()
    return False not in validity
