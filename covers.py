from itertools import combinations

def get_column(matrix, c):
    '''
        Selects the column in position c.
    '''
    return [x[c] for x in matrix]

def columns_cover(columns, v, t):
    '''
        For the selected columns, check
        if they have all possible v-tuples.
    '''
    found_combinations = []
    for i in range(t):
        input = [c[i] for c in columns]
        if input not in found_combinations:
            found_combinations.append(input)
    return len(found_combinations) == v*v

def covers(matrix, v, k, t):
    '''
        Given a matrix computes the covering
        check for all v-sets of columns.
    '''
    validity = []
    for c in combinations([i for i in range(k)], v):
        c = list(c)
        columns = [get_column(matrix, col) for col in c]
        validity.append(columns_cover(columns, v, t))
    return False not in validity
