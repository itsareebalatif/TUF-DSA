def main():
    arr1=[3,1,-2,-5,2,-4]
    #rearrange_brute(arr1)
    rearrange_optimal(arr1)


def rearrange_brute(arr) :
    n=len(arr)
    
    positive_arr=[]
    negative_arr=[]
    for i in range(len(arr)):
        if arr[i]>0:
            positive_arr.append(arr[i])
        else:    
            negative_arr.append(arr[i])
    print("positive:",positive_arr)
    print("negative:",negative_arr)

    for i in range(int(len(arr)/2)):
        arr[i*2]=positive_arr[i]
        arr[i*2+1]=negative_arr[i]
    print("arr:",arr)    






def rearrange_optimal(arr):
    n=len(arr)
    ans=[]
    positive_index=0
    negative_index=1
    for i in range(n):
        if arr[i]<0:
            ans[negative_index]=arr[i]
            negative_index+=2
            print(ans)
        else:
            ans[positive_index]=arr[i]
            positive_index+=2
            print(ans)    
    print("new:",ans)            



if __name__=="__main__":
    main()    