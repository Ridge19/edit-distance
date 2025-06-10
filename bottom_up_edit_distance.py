# -------------------------------------------------
# File to calculate bottom up edit distance
# CHANGE THIS FILE
#
# __author__ = 'Edward Small' & <YOUR NAME HERE>
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------


def edit_distance_bu(s1: str, s2: str, cost: int = 1):
    """
    gives the edit distance (minimal changes) for two strings s1 and s2 according to the cost
    :param s1: string we have
    :param s2: string we are transforming into
    :param cost: cost of replacing a letter
    :return: the edit distance and the dynamic programming table using a bottom-up approach
    """
    # set up DP table
    m, n = len(s1), len(s2)
    table = [["#" for _ in range(n + 1)] for _ in range(m + 1)]
    distance = float('inf')

    """
    IMPLEMENT ME
    """

    # initial conditions for the first row
    for j in range(n + 1):
        table[0][j] = j  # cost of inserting j characters

    # initial conditions for the first column
    for i in range(m + 1):
        table[i][0] = i  # cost of deleting i characters

    # fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = cost

            table[i][j] = min(
                table[i - 1][j] + 1,  # deletion
                table[i][j - 1] + 1,  # insertion
                table[i - 1][j - 1] + cost  # substitution
            )

    distance = table[m][n]

    return distance, table
