def main():
    
    #name5time(5)
    #Nto0(0,5)
    #NTO0(5)
    #one_N(5)
    #ONE_N(5)
    NTOONE(0)

    
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

count=1
def one_N(N):
    global count
    if count==N:
        return
    print(count)
    count+=1
    one_N(N)

def ONE_N(N):
    if N==0:
        return
    ONE_N(N-1)
    print(N-1)

def NTOONE(N):
    if N==5:
        return
    NTOONE(N+1)
    print(N+1)  


if __name__=="__main__":
    main()    