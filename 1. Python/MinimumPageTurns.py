# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: A desired page number of a book, and total page count of a book are given.
    # Function pageCount() returns minimum number of pages needed to get to target page,
    # after calculating if turning pages from the end is shorter or turning from beginning is shorter.
    # They turn 1 page at a time, revealing two pages.
    # Note, function assumes page 1 always starts on right page in beginning of book.


def pageCount(n, p):
    """
    param n: amount of pages in book
    param p: page user must turn to
    
    return: minimum number of pages turns needed for user to arrive at p.
    """
    book = (n+1)*[0]
    
    book[p] = 1
    # Special cases:
    # If goal is page 1 or last page, no turns required
    if p == 1 or p==n:
        return 0
    
    # If goal is second to last page, and last page is odd, no turns required
    elif p == (n-1) and n % 2 != 0:
        return 0

    # If above cases do not apply, some page turning required
    # Count turns from beginning, every page flip reveals two pages
    start_counter = 0
    for num in range(2, n, 2):
        start_counter += 1
        even_page = book[num]
        odd_page = book[num + 1]
        if even_page == 1 or odd_page == 1:
            break

    # Count turn from end, but per case if book length is odd or even:
    if n % 2 != 0:
        end_counter = 0
        for num in range((n), 0, -2):
            even_page = book[num - 1]
            odd_page = book[num]
            if even_page == 1 or odd_page == 1:
                break
            end_counter += 1

    elif n % 2 == 0:
        end_counter = 1
        for num in range((n-1), 0, -2):
            even_page = book[num -1]
            odd_page = book[num]
            if even_page == 1 or odd_page == 1:
                break       
            end_counter += 1

    # If turning pages from end is shorter:
    if end_counter < start_counter:
        print("Starting from end is shorter.")
        return end_counter
    
    # Otherwise, return page turn counter from beginning of book:
    print("Starting from beginning is shorter.")
    return start_counter


if __name__ == '__main__':
    result = pageCount(5, 3)
    print(result)
