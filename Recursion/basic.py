def main():
    
    #name5time(5)
    #Nto0(0,5)
    NTO0(5)

    
def name5time(n):
    if n==0:
        return
    print("Areeba")
    name5time(n-1)


def Nto0(i,N):
    if i==N:
        return
    print(i)
    Nto0(i+1,N)



count=0
def NTO0(N):
    global count
    if count==N:
        return
    print(count)
    count+=1
    NTO0(N)




if __name__=="__main__":
    main()    