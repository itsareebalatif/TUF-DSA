def main():
    arr1 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
    # rearrange_brute(arr1)
    # rearrange_optimal(arr1)
    a = rearrange(arr1, len(arr1))
    print(a)


def rearrange_brute(arr):
    n = len(arr)

    positive_arr = []
    negative_arr = []
    for i in range(len(arr)):
        if arr[i] > 0:
            positive_arr.append(arr[i])
        else:
            negative_arr.append(arr[i])
    print("positive:", positive_arr)
    print("negative:", negative_arr)

    for i in range(int(len(arr) / 2)):
        arr[i * 2] = positive_arr[i]
        arr[i * 2 + 1] = negative_arr[i]
    print("arr:", arr)


def rearrange_optimal(arr):
    n = len(arr)
    ans = [0] * n
    positive_index = 0
    negative_index = 1
    for i in range(n):
        if arr[i] < 0:
            if negative_index < n:
                ans[negative_index] = arr[i]
                negative_index += 2
        else:
            if positive_index < n:
                ans[positive_index] = arr[i]
                positive_index += 2

    print("new:", ans)


def rearrange(arr, n):
    positive = []
    negative = []
    n = len(arr)
    ans = [0] * n
    for i in range(n):
        if arr[i] < 0:
            negative.append(arr[i])
        elif arr[i] >= 0:
            positive.append(arr[i])

    if len(positive) < len(negative):
        for i in range(len(positive)):
            ans[i * 2] = positive[i]
            ans[i * 2 + 1] = negative[i]
        index = len(positive) * 2
        for i in range(len(positive), len(negative), 1):
            ans[index] = negative[i]
            index += 1
    else:
        for i in range(len(negative)):
            ans[i * 2] = positive[i]
            ans[i * 2 + 1] = negative[i]
        index = len(negative) * 2
        for i in range(len(negative), len(positive), 1):
            ans[index] = positive[i]
            index += 1
    return ans


if __name__ == "__main__":
    main()
