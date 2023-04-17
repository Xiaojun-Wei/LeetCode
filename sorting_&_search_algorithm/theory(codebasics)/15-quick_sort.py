def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

    return arr


def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(arr, start, end)

    swap(arr, pivot_index, end)

    return end


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    print(quick_sort(elements, 0, len(elements)-1))