def main():
    array=[1,2,2,3,4,2,1,2,2]
    a=optimal(array)
    print(a)

def Brute(arr):
    n=len(arr)
    
    for i in range(n):
        count=0
        for j in range(n): 
            if arr[i]==arr[j]:
                count+=1
        if count>=(n/2):
            return arr[i] 
    return -1     

#BETTER APPROACH
def Better(arr):
    n=len(arr)
    dic={}
    for i in range(n):
        if arr[i] in dic:
            dic[arr[i]]+=1
        elif arr[i] not in dic:
            dic[arr[i]]=1

    for key,value in dic.items():
        if value>=(n//2):
            return key
    return -1          

#OPTIMAL APPROACH
def optimal(arr):
    n=len(arr)
    count=0
    #algo
    for i in range(n):
        if count==0:
            element=arr[i]
            count=1
        elif element==arr[i]:
            count+=1
        else:
            count-=1
    count1=0
    for i in range(n):
        if arr[i]==element:
            count1+=1

    if count1>(n//2):
        return element
    return -1                




if __name__=="__main__":
    main()         