import sys
def main():
    arr1 = [-2,1,-3,4,-1,2,1,-5,4] 
    a=brute(arr1)
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






if __name__=="__main__":
    main()
