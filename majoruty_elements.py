def main():
    arr1 = [2, 2, 1, 1, 1, 2, 2]
    a=maj_elem_brute(arr1)
    print(a)


def maj_elem_brute(arr):
    n=len(arr)
    for i in range(n):
        countof=0
        for j in range(n):
            if arr[i]==arr[j]:
                    countof+=1
        if  countof>(n//2):
            return arr[i]
    return -1            








if __name__=="__main__":
     
     main()    