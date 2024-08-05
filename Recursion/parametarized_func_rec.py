def main():
    SUMMOFNO(3, 0)


def summofno(N):
    if N == 0:
        return 0
    return N + summofno(N - 1)


def SUMMOFNO(n, sum):
    if n == 0:
        print(sum)
        return 0
    return SUMMOFNO(n - 1, sum + n)


if __name__ == "__main__":
    main()
