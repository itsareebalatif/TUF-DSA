
def main():

    arr1 = ["d","b","c","b","c","a"]

    a=find_kth_distinct(arr1,2)
    print(a)

def brute(arr,k):
    n=len(arr)
    extra=[]
    
    for i in range(n):
        isdistinct=True
        for j in range(n):
            if i!=j and arr[i]==arr[j]:
                isdistinct=False
                break
        if isdistinct:
            extra.append(arr[i])

    res=extra[k-1]        

    return res          

    
def find_kth_distinct(arr, k):
    n = len(arr)
    
    for i in range(n):
        isdistinct = True
        
        # Check if arr[i] is a duplicate
        for j in range(n):
            if i != j and arr[i] == arr[j]:
                isdistinct = False
                break
        
        # If it is distinct, decrement k
        if isdistinct:
            k -= 1
            if k == 0:
                return arr[i]
    
    return None     



if __name__=="__main__":
    main()

            

         