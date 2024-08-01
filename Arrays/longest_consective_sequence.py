def main():
    a = [100, 200, 1, 2, 3, 4]
    ans=BruteForch(a)
    print(ans)


def linearsearch(arr,num):
    n=len(arr)
    for i in range(n):
        if arr[i]==num:
            return True
    return False 

def BruteForch(arr):
    n=len(arr)
    long_length=1
    for i in range(n):
        x=arr[i]
        cnt=1
        while linearsearch(arr,x+1):
            x+=1
            cnt+=1
        long_length=max(long_length,cnt)
    return long_length        




if __name__=="__main__":
    main()
    