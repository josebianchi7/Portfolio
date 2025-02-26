# Jose Bianchi
# CS 325 Practice File

def bottom_up_dis_helper(buckets, x, b_table=None):
    """
    Distribute quantity x among buckets of different sizes found in
    array buckets. Find combination with the least amount of buckets
    to sum up to x. Return optimal solution.

    :param buckets:
    :param x:
    :param b_table:
    :return:
    """
    # Fill solution array with overly high values (case if x was split into x+1 buckets)
    if b_table is None:
        b_table = (x+1)*[x+1]
    # Set base case
    b_table[0] = 0

    # Create bucket used array to track optimal solution
    buckets_used = [0 for _ in range(x+1)]

    # Solve for all solutions from 1 to x (len(b_table))
    for curr_x in range(1, len(b_table)):
        # Set overly high solution value for placeholder
        solution = b_table[curr_x]

        # Try out all bucket sizes
        for b in buckets:
            if b <= curr_x:
                # Compare previous bucket distribution with curr distribution
                prev_b_solution = curr_x - b
                curr_b_count = 1 + b_table[prev_b_solution]
                # If current bucket distribution count is less than current solution, reassign solution value
                if curr_b_count < solution:
                    solution = curr_b_count
                    # Update solution table
                    b_table[curr_x] = solution
                    buckets_used[curr_x] = b

    print(b_table)
    result = -1
    if b_table[x] < x:
        result = b_table[x]

    # For the total amount, return coins at optimal amounts from total to 0
    while x > 0:
        print(buckets_used[x])
        x = x - buckets_used[x]

    return result


def top_down_dis_helper(buckets, x, b_memo=None):
    """
    Distribute quantity x among buckets of different sizes found in
    array buckets. Find combination with the least amount of buckets
    to sum up to x. Return optimal solution.

    :param buckets:
    :param x:
    :param b_memo:
    :return:
    """
    if b_memo is None:
        b_memo = (x+1)*[0]

    # Data validation
    if x < 0:
        return -1

    if x == 0:
        return 0

    if b_memo[x] != 0:
        return b_memo[x]

    # Establish large comparison value for initial comparison
    min_buckets = x + 1

    for b in buckets:
        # Attempt all combinations with all buckets
        curr_combination = top_down_dis_helper(buckets, x - b, b_memo)

        # Compare current combination and increment bucket count
        if 0 <= curr_combination < min_buckets:
            min_buckets = 1 + curr_combination

    # Return -1 if no combination found and unreasonable amount of buckets is still min
    if min_buckets > x:
        b_memo[x] = -1
    else:
        b_memo[x] = min_buckets

    return b_memo[x]


if __name__ == '__main__':
    a = 6
    coins = [5, 3, 1]
    print(bottom_up_dis_helper(coins, a))
    print(top_down_dis_helper(coins, a))

