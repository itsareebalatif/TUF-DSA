def main():
    arr1=[10,22,12,3,0,6]
    a=leader(arr1)
    print(a)

def leader(arr):
    ans=[]
    n=len(arr)
    ans.append(arr[n-1])
    for i in range(n):
        for j in range(i+1,n):
            leader=False
            if arr[i]>arr[j]:
                leader=True
        if leader:
            ans.append(arr[i])   
    return ans           



def Leader(arr):
    n=len(arr)
    max_element=arr[n-1]
    ans=[]
    ans.append(arr[n-1])
    for i in range(n-2,0,-1):
        if arr[i]>max_element:
            ans.append(arr[i])
            max_element=arr[i]
    return ans            





if __name__=="__main__":
    main()    