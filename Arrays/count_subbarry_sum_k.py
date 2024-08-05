from collections import defaultdict
def main():

    arr = [1,3,2,4]
    # 1, 3, 6, 10, 2, 5, 9, 3, 7, 4.
    a=optimal(arr,6)
    print(a)

#BETTER APPROACH
def bruteforce(nums,k):
    count=1
    for i in range(len(nums)):
        summ=0
        for j in range(i,len(nums)):
            summ+=nums[j]
        if summ==k:
            count+=1 
    return count 


#OPTIMAL APPROACH
def optimal(arr,k):
    n=len(arr)
    presum=0
    count=0
    mpp=defaultdict(int)
    mpp[0]=1
    for i in range(n):
        presum+=arr[i]
        remove=presum-k
        count+=mpp[remove]
        mpp[presum]+=1
    return count    






if __name__=="__main__":
    main()

            