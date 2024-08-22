def main():
    array=[1,2]
    a=OPTIMAL(array)
    print(a)

def OPTIMAL(arr):
    n=len(arr)
    ans=[]
    for i in range(n):
        if len(ans)==0 or ans[0]!=arr[i]:
            count=0
            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1
            if count > (n/3):
                ans.append(arr[i])
        if len(ans)==2:
          break
    return ans            


if __name__=="__main__":
    main()    