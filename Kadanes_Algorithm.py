import sys
def main():
    arr1 = [-2,1,-3,4,-1,2,1,-5,4] 
    a=maxsum(arr1)
    print(a)

def brute(arr):
    n=len(arr)
    maxi=-sys.maxsize-1
    for i in range(n):
        for j in range(i,n):
            summ=0
            for k in range(i,j+1):
                summ+=arr[k]
            maxi=max(maxi,summ) 
    return maxi           


def better(arr):
    n=len(arr)
    mexi=-sys.maxsize-1
    for i in range(n):
        summ=0
        for j in range(i,n):
            summ+=arr[j]
            mexi=mexi(mexi,summ)
            return mexi
    return -1        



def maxsum(arr):
    n=len(arr)
    maxi=-sys.maxsize-1
    summ=0
    for i in range(n):
        summ+=arr[i]
        if summ>maxi:
            maxi=summ
        if summ<0:
            summ=0
    return maxi        





if __name__=="__main__":
    main()
