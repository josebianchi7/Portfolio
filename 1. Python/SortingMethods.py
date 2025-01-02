import random

# Insertion Sort
def insertion_sort(arr) -> object:
    """
    Sort an unsorted array in non-descending order, 
    by inserting elements from an unsorted section
    into the assumed sorted section iteratively.
    Time complexity = O(n^2)

    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    for i in range(1, len(arr)):
        j = i - 1
        currElement = arr[i]
        prevElement = arr[j]
        
        while j >= 0 and currElement < prevElement:
            # Compare current element to all previous and insert into lower position as needed.
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1 
            i -= 1   
            currElement = arr[i]
            prevElement = arr[j]
    return arr

# Selection Sort
def selection_sort(arr) -> object:
    """
    Sort an unsorted array, by finding the min and repeatedly
    sorting from min value to end of array. Time complexity = O(n^2)
    
    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    for currSlot in range(len(arr) - 1):
        currMinIndex = currSlot

        # Search for current Min in unsorted portion of array
        for j in range(currSlot + 1, len(arr)):
            if arr[j] < arr[currMinIndex]:
                currMinIndex = j
        # Make swap once reaching end of unsorted portion
        arr[currSlot], arr[currMinIndex] = arr[currMinIndex], arr[currSlot]

    return arr       

# Counting Sort
def counting_sort(arr) -> object:
    """
    Sort an unsorted array of integers by creating a count array, 
    then filling in a new array with the sorted elements, where 
    indices correspond to an offset of element values. 
    Time complexity = O(n + k), k = range of values
    
    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    # Determine min and max from array
    min = arr[0]
    max = min
    for element in arr:
        if element < min:
            min = element
        if element > max:
            max = element           

    # Create count array with size equal to range from min to max
    countArraySize = (max - min) + 1
    countArr = countArraySize * [0]
    
    # Populate count array
    for element in arr:
        countArr[element - min] += 1

    
    # Export elements from count array into return array in sorted order
    newArr = []
    for i in range(len(countArr)):
        while countArr[i] > 0:
            newArr.append(i + min)
            countArr[i] -= 1
    return newArr


# Heapsort
def heapsort(arr) -> object:
    """
    Heapify an array, then coduct a heapsort to complete
    sorting the array. Min heap is used for a nondescending array.
    Time complexity = O(n * log(n))
    
    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    # Create helper function to percolate a node down tree when needed, 
    # so code does not need to be written twice.
    def _percolate_down(arr1: object, i: int, heap_length: int) -> None:
        """
        Helper function to percolate elements down tree when needed

        :param arr1: current array object
        :param i: current index that may need to percolate down
        """
        while i < heap_length:
            currParent = arr[i]
            # Get child node elements if they exist
            leftChildIndex = (2*i) + 1
            rightChildIndex = (2*i) + 2 
            leftChild = currParent
            rightChild = leftChild
            if leftChildIndex < heap_length:
                leftChild = arr[leftChildIndex]
            if rightChildIndex < heap_length: 
                rightChild = arr[rightChildIndex]

            # Swap if a child is less than parent 
            # Swap with left if right and left are equal
            if leftChild < currParent and leftChild <= rightChild:
                arr[i], arr[leftChildIndex] = arr[leftChildIndex], arr[i]
                # Ensure heap property is still followed  further down tree 
                # after swap by checking newly swapped child next
                i = leftChildIndex

            elif rightChild < currParent:
                arr[i], arr[rightChildIndex] = arr[rightChildIndex], arr[i]
                i = rightChildIndex

            # If no swap is needed, element conforms to heap property, return    
            else:
                return

    # Step 1: Heapify Array by treating array like a binary tree 
    n = len(arr)
    # i = parent index, beginning with last parent
    i = (len(arr)//2) - 1          
    while i >= 0:
        _percolate_down(arr, i, n)
        i -= 1

    # Step 2: Complete Heapsort (array will initially be sorted in non-ascending order)   
    # k = last index of heap portion of array that is unsorted
    k = n - 1
    # Percoloate current element down to proper position, 
    # then swap root (index = 0) again with new last element in heap portion
    while k >= 0:
        arr[0], arr[k] = arr[k], arr[0]
        _percolate_down(arr, 0, k)
        k -= 1

    # Step 3: Reverse array for non-descending order
    # j = last element pointer
    j = n - 1
    for i in range(n//2):
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1    

    return arr        

# Shellsort
def shellsort(arr) -> object:
    """
    Performs sorting similar to Insertion Sort, but utilizes
    a starting gap of half of array size to compare elements.
    Gap is decremented after each iteration.
    Time complexity dependent on active sequence
    
    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    n = len(arr)
    gapSequence = []
    k = 1

    # Ensure only one of below options is active code. 
    # Option 1 for len(arr) <= 200
    # Option 2 for len(arr) > 200

    # Option 1: Hibbard Sequence, Time complexity = O(n^(3/2))
    # currGap = (2**k) - 1

    # Option 2: Sedgewick Sequence (manually insert 1), Time complexity = O(n^(4/3))
    gapSequence.append(1)
    currGap = (4**k) + 3*(2**(k-1)) + 1

    while currGap < n:
        gapSequence.append(currGap) 
        k += 1
        # Confirm correct gap sequence is active below
        # currGap = (2**k) - 1
        currGap = (4**k) + 3*(2**(k-1)) + 1
    print(gapSequence)

    # Coduct shellsort with gap sequence reversed
    g = len(gapSequence) - 1
    gap = gapSequence[g]  
    j = gap
    while g >= 0:
        # Compare element with previous elements offset by gap 
        i = j - gap
        elementCurr = arr[j]
        elementPrev = arr[i]
        
        # Swap when needed, and proceed to check if further swap earlier in arr is needed
        if elementCurr < elementPrev:
            arr[i], arr[j] = arr[j], arr[i]
            # If an earlier gap element exists, check it. 
            # Offset to i - 1, so next line of code puts j at correct index
            if i - gap >= 0:
                j = i - 1 
        j += 1

        # Once end of array is reached, proceed to next lowest gap in gapSequence
        if j == len(arr):
            g -= 1
            gap = gapSequence[g]  
            j = gap

    return arr

# Mergesort
def mergesort(arr: object) -> object:
    """
    Creates an additional array of equal size to given array.
    Recursively breaks array into halves and merges after splitting.
    Subarrays are sorted into a copy array.
    When there is only one sub array remaining, the list is sorted.
    Time complexity = O(n * log n), but requires additional space and 
    uses recursion.
    
    :param arr: unsorted array

    :return arr: sorted array in nondescending order.
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    # Step 1: Divide list in half
    mid = n // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Step 2: Recursively sort each half
    leftHalf = mergesort(leftHalf)
    rightHalf = mergesort(rightHalf)

    # Step 3: Merge sorted halves back together    
    return _merge(leftHalf, rightHalf)

# Mergesort helper function
def _merge(leftArr, rightArr) -> object:
    """
    :param leftArr: current left half of subarray
    :param rightArr: current right half of subarray

    :return object: sorted array in non-descending order
    """
    soredArr = []
    i = 0
    j = i

    # Step 4: Merge two halves into sorted positions in new array
    while i < len(leftArr) and j < len(rightArr):
        leftElement = leftArr[i]
        rightElement = rightArr[j]
        if leftElement < rightElement:
            soredArr.append(leftElement)
            i += 1
        else:
            soredArr.append(rightElement)    
            j += 1

    # Append remianing elements if they exist
    while i < len(leftArr):
        soredArr.append(leftArr[i])
        i += 1
    while j < len(rightArr):
        soredArr.append(rightArr[j])
        j += 1

    return soredArr

if __name__ == '__main__':
    arr1 = [1, 0]
    arr2 = [1]
    arr3 = [9, 8, 5, 7, 2, 6, 1, 2]
    arr4 = []
    for i in range(10):
        arr4.append(random.randint(0, 100))
    arr5 = []
    for i in range(1000):
        arr5.append(random.randint(-10000, 10000))   
    arr6 = [100, 20, 6, 200, 90, 150, 300]
    arr7 = ['monkey', 'zebra', 'elephant', 'horse', 'bear']  
    result1 = mergesort(arr7)
    print(result1)
