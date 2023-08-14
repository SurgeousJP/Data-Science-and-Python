
def Selection_Sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        temp = array[i]
        array[i] = array[min_idx]
        array[min_idx] = temp


def Interchange_Sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp


def Bubble_Sort(array):
    for i in range(len(array)):
        j = len(array) - 1
        while j >= i + 1:
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            j -= 1


def Heapify(arr, n, i):
    largest = i  # initialize largest as root
    left = 2 * i + 1  # left child of root
    right = 2 * i + 2 # right child of root
    # See if left child of root is exist and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left
    # See if right child of root is exist and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        Heapify(arr, n, largest)


def Heap_Sort(arr):
    n = len(arr)
    # Build a max heap
    for i in range(n//2 - 1, -1, -1):
        Heapify(arr, n, i)
    # One by one extract element
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        Heapify(arr, i, 0)


def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        Merge_Sort(L)
        Merge_Sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def QuickSort(arr, left, right):
    pivot = arr[left + (right - left) // 2]
    i = left
    j = right
    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    if i < right:
        QuickSort(arr, i, right)
    if j > left:
        QuickSort(arr, left, j)


def Insertion_Sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


lst = [2, 3, 7, 6, 5, 8]
print(lst)
Insertion_Sort(lst)
print(lst)

