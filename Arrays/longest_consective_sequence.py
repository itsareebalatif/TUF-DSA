def main():
    a = [100, 200, 1, 2, 3, 4]
    ans=optimal(a)
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


def Better_sol(arr):
    n=len(arr)
    arr.sort()
    lastSmaller = arr[0]
    cnt = 1
    longest = 1

    # Find longest sequence
    for i in range(1, n):
        if arr[i] == lastSmaller + 1:
            # a[i] is the next element of the current sequence
            cnt += 1
            lastSmaller = arr[i]
        elif arr[i] != lastSmaller:
            # a[i] is a new element, start a new sequence
            cnt = 1
            lastSmaller = arr[i]
        longest = max(longest, cnt)
    
    return longest  



def optimal(arr):
    n=len(arr)
    if n==0:
        return 0
    st=set()
    cnt=0
    longest=1
    for num in arr:
        st.add(num)
    for item in st:
        if item-1 not in st:
            x=item
            cnt=1
            while x+1 in st:
                x+=1
                cnt+=1
            longest=max(longest,cnt) 
    return longest               



if __name__=="__main__":
    main()
    