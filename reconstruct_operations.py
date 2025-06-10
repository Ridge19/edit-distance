# -------------------------------------------------
# File to beautify transformation of s1->s2
#
# __author__ = 'Edward Small'
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------

def reconstruct_operations(s1, s2, table, cost):
    """
    Shows how s1 transform into s2, according to the backtracking through the table
    :param s1: string we start with
    :param s2: string we transform into
    :param table: the DP table
    :param cost: cost of replacing a letter
    :return: a list of operations
    """
    i, j = len(s1), len(s2)
    operations = []
    current = list(s1)

    def format_step(op, cur):
        return f"{op.ljust(35)}→ {''.join(cur)}"

    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
            operations.append(format_step(f"Match '{s1[i]}'", current))
        elif i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + cost:
            current[i - 1] = s2[j - 1]
            operations.append(format_step(f"Substitute '{s1[i - 1]}' with '{s2[j - 1]}'", current))
            i -= 1
            j -= 1
        elif j > 0 and table[i][j] == table[i][j - 1] + 1:
            current.insert(i, s2[j - 1])
            operations.append(format_step(f"Insert '{s2[j - 1]}' at pos {i}", current))
            j -= 1
        elif i > 0 and table[i][j] == table[i - 1][j] + 1:
            operations.append(format_step(f"Delete '{current[i - 1]}' at pos {i - 1}", current))
            del current[i - 1]
            i -= 1
        else:
            break

    return operations