def main():
    prices = [7, 1, 5, 3, 6, 4]
    a = optimal_stock_price(prices)
    print(a)


def stock_price(arr):
    minprice = 0
    maxpro = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                maxpro = max(maxpro, arr[j] - arr[i])
    return maxpro


def optimal_stock_price(arr):
    minprice = float("inf")
    maxpro = 0
    n = len(arr)
    for i in range(n):
        minprice = min(minprice, arr[i])
        maxpro = max(maxpro, arr[i] - minprice)
    return maxpro


if __name__ == "__main__":
    main()
