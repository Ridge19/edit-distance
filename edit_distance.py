# -------------------------------------------------
# File to run edit distance functions
#
# __author__ = 'Edward Small'
# __copyright__ = 'Copyright 2025, RMIT University'
# -------------------------------------------------

import sys
import csv
import re
import time
import random
import string
from top_down_edit_distance import edit_distance_td
from bottom_up_edit_distance import edit_distance_bu
from reconstruct_operations import reconstruct_operations

# Set a seed for reproducibility - comment out the below if you want randomness
random.seed(42)
def sanitize_filename(s):
    """
    Ensure filename is safe to use by removing special characters, etc
    :param s: filename
    :return: safe filename
    """
    return re.sub(r'[^a-zA-Z0-9_-]', '_', s)


def save_table_to_csv(table, method, s1_arg, s2_arg, s1, s2):
    """
    saves the dynamic programming table as a csv
    :param table: the DP we are saving
    :param method: the method we used (TD vs BU)
    :param s1: the string we started with
    :param s2: the string we transformed into
    """
    safe_s1 = sanitize_filename(s1_arg)
    safe_s2 = sanitize_filename(s2_arg)
    filename = f"edit_distance_{method}_{safe_s1}_{safe_s2}.csv"

    # Build the header row: ['', '', s2[0], s2[1], ..., s2[n]]
    header_row = [''] + [''] + list(s2)

    # Build the table with s1 as the first column (with empty top-left corner)
    table_with_labels = [header_row]
    for i in range(len(table)):
        row_label = s1[i - 1] if i > 0 else ''
        table_with_labels.append([row_label, *table[i]])

    # Write to CSV
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(table_with_labels)


def main():
    if len(sys.argv) != 5:
        print("Usage: python edit_distance.py <method> <string1> <string2> <save_flag>")
        sys.exit(1)

    method = sys.argv[1]
    cost = 1
    s1_arg = sys.argv[2]
    s2_arg = sys.argv[3]
    # Check if both are digits — then generate random strings
    if s1_arg.isdigit() and s2_arg.isdigit():
        len1, len2 = int(s1_arg), int(s2_arg)
        s1 = ''.join(random.choices(string.ascii_lowercase, k=len1))
        s2 = ''.join(random.choices(string.ascii_lowercase, k=len2))
    else:
        s1, s2 = s1_arg, s2_arg
    save_flag = sys.argv[4]

    # Start timer
    start_time = time.time()

    # calculate the edit distance
    if method == 'TD':
        distance, table = edit_distance_td(s1, s2, cost)
    elif method == 'BU':
        distance, table = edit_distance_bu(s1, s2, cost)
    else:
        print("Invalid method. Use 'TD' for top-down or 'BU' for bottom-up.")
        sys.exit(1)
    # End timer
    end_time = time.time()

    if distance == float('inf'):
        print(f"{method} not yet implemented.")
        sys.exit(1)

    construction = reconstruct_operations(s1, s2, table, cost)

    # supress the print if we exceed some number of characters
    if len(s1) * len(s2) <= 1000:
        print(f"{'Original string'.ljust(35)}→ {s1}")
        for op in construction:
            print(op)

    print("Edit Distance:", distance)
    print(f"Execution time for {method}: {end_time - start_time:.6f} seconds")

    if save_flag:
        # Convert integers to strings and keep "#" where needed
        formatted_table = [
            [cell if isinstance(cell, str) else str(cell) for cell in row]
            for row in table
        ]
        save_table_to_csv(formatted_table, method, s1_arg, s2_arg, s1, s2)


if __name__ == '__main__':
    main()
