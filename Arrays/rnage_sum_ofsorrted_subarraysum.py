def main():

    arr = [1, 2, 3, 4]
    # 1, 3, 6, 10, 2, 5, 9, 3, 7, 4.
    a = bruteforce(arr, 1, 5)
    print(a)


def bruteforce(nums, left, right):
    res = []
    for i in range(len(nums)):
        summ = 0
        for j in range(i, len(nums)):
            summ += nums[j]
            res.append(summ)

    res.sort()
    sum = 0

    for i in range(left - 1, right):
        sum += res[i]

    return sum


if __name__ == "__main__":
    main()
