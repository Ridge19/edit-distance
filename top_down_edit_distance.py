# -------------------------------------------------
# File to calculate top down edit distance
# CHANGE THIS FILE
#
# __author__ = 'Edward Small' & <YOUR NAME HERE>
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------

def edit_distance_td(s1: str, s2: str, cost: int = 1):
    """
    gives the edit distance (minimal changes) for two strings s1 and s2 according to the cost
    :param s1: string we have
    :param s2: string we are transforming into
    :param cost: cost of replacing a letter
    :return: the edit distance and the dynamic programming table using a top-down approach
    """
    # used for backtracking - remember what solutions we took when calculating each entry.
    memo = {}
    # set up DP table
    m, n = len(s1), len(s2)
    table = [['#' for _ in range(n + 1)] for _ in range(m + 1)]

    # initial conditions for the first row
    table[0] = list(range(n + 1))

    distance = float('inf')

    """
    IMPLEMENT ME
    """

    # function to calculate the edit distance recursively
    def recurse(i: int, j: int) -> int:
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:
            return j
        if j == 0:
            return i
        if s1[i - 1] == s2[j - 1]:
            cost = 0
        else:
            cost = 1
        memo[(i, j)] = min(
            recurse(i - 1, j) + 1,  # deletion
            recurse(i, j - 1) + 1,  # insertion
            recurse(i - 1, j - 1) + cost  # substitution
        )
        return memo[(i, j)]

    distance = recurse(m, n)

    # fill the table with the calculated values
    for i in range(m + 1):
        for j in range(n + 1):
            if (i, j) in memo:
                table[i][j] = memo[(i, j)]
            else:
                table[i][j] = recurse(i, j)
    
    # backtrack to fill the table with the actual operations
    for i in range(m + 1):
        for j in range(n + 1):
            if (i, j) in memo:
                table[i][j] = memo[(i, j)]
            else:
                table[i][j] = recurse(i, j)
    
    # fill the first column
    for i in range(1, m + 1):
        table[i][0] = i
    
    # fill the first row
    for j in range(1, n + 1):
        table[0][j] = j

    # fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(
                    table[i - 1][j] + 1,  # deletion
                    table[i][j - 1] + 1,  # insertion
                    table[i - 1][j - 1] + cost  # substitution
                )

    return distance, table
