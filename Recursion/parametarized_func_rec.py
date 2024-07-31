def main():
    a=summofno(5)
    print(a)

def summofno(N): 
    if N==0:
        return 0
    return N+summofno(N-1)




if __name__=="__main__":
    main()
    