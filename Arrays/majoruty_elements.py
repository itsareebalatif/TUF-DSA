def main():
    arr1 = [3,3,4]
    a=majorityElement(arr1)
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


def maj_ele_better(arr):
    n=len(arr)
    dic={}
    for i in arr:
        if i in dic:
             dic[i]+=1
        else:
             dic[i]=1

    for num,count in dic.items():
         if count>(n//2):
              return num         
    return -1             



def majorityElement(arr):
    n=len(arr)
    element=None
    count1=0
    for i in range(n):
        if count1==0:
            count1=1
            element=arr[i]
        elif element==arr[i]:
            count1+=1
        else:
             count1-=1
    
    count2=0
    for i in range(n):
        if arr[i]==element:
            count2+=1
    if count2>(n/2):
        return element
    return -1
              
              

             
             
              
     




if __name__=="__main__":
     
     main()    