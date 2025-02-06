# Author: Jose Bianchi
# GitHub username: josebianchi7


def intToBinaryUnsigned(x : int):
    """
    Function to convert unsigned integer to binary string.
    param x (int): unsigned integer

    return (str): binary representation of x
    """
    b = ""
    while x > 1:
        r = x % 2
        b = str(int(r)) + b
        x = int(x/2)

    # Avoid infinite loop by adding last 1 bit outside of loop when x = 1
    b = str(1) + b
    return b

if __name__ == '__main__':
    num = 10
    print(intToBinaryUnsigned(num))
