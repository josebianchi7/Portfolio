def digit_sum(n):
    """
    Given an integer, without using string conversion, sum each digit place and return the sum
    :param n: integer
    :return: sum of each individual digit of integer argument
    """
    dig_sum = 0
    # Determine number size:
    digit_max = 10
    while digit_max < n:
        digit_max *= 10

    # Turn digit_max into one digit place less than argument
    digit_max //= 10

    # Floor divide argument by its 10 base
    # Add quotient to return sum
    # Bring argument down to next smallest 10 base and repeat loop
    while n > 10:
        if n > digit_max:
            num = (n // digit_max)
            dig_sum += num
            n -= num * digit_max

        # Push divisor down to next smallest 10 base
        digit_max //= 10

    # Once value is less than 10, add value in one's place to return sum
    dig_sum += n
    return dig_sum


answer = digit_sum(125)
print(answer)
