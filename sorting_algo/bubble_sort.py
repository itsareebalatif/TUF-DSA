def main():
    arr1 = [3, 1, 2, 4, 1, 5, 2, 6]
    a = bubble(arr1)
    print(a)


def bubble(arr):
    n = len(arr)
    for i in range(n - 1, 1, -1):
        for j in range(0, i - 1, 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    main()
