
def insertion_sort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current

    return arr


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    print(insertion_sort(elements))