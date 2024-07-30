def main():
    arr1=[3,1,-2,-5,2,-4]
    rearrange_optimal(arr1)


def rearrange_optimal(arr) :
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






if __name__=="__main__":
    main()    