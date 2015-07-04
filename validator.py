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
    all_possible_combs = args[1]
    N = args[2]
    found_combinations = []
    for i in range(N):
        input = [c[i] for c in columns]
        if input not in found_combinations:
            found_combinations.append(input)
            if len(found_combinations) == all_possible_combs:
                return True
    return False

def covers(matrix, v, k, N):
    '''
        Given a matrix computes the covering
        check for all v-sets of columns.
    '''
    # Lets fix the number of processes
    p = Pool(min(k, 6))
    args = []
    for c in combinations([str(i) for i in range(k)], v):
        c = list(c)
        args.append([[get_column(matrix, int(col)) for col in c], v**v, N])
    validity = p.map(columns_cover, args)
    p.close()
    p.join()
    return False not in validity
