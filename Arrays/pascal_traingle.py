def main():
   #nCr(2,0)
   nthrow(4)


#VERSIN 1
#we need to find out the element at position (r,c). 
def nCr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res//(i+1)
    return res  
    
#VERSION 2
# Print nth row
def nthrow(row):
    for i in range(1,row+1):
        print(nCr(row-1,i-1),end=" ") 
    print()       
      


    

if __name__=="__main__":
    main()    