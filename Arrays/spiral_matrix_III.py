def main():
    rows = 5
    cols = 6 
    rSta = 1
    cSta = 4
    a=optimalSpiralIII(rows,cols,rSta,cSta)
    print(a)


def spiralIII(row,col,rstart,cstart):
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    res=[]
    step=0
    dir=0
    res.append([rstart,cstart])
    while len(res)<row*col:
        if dir==0 or dir==2:
            step+=1
        for i in range(step):
            rstart+=directions[dir][0]
            cstart+=directions[dir][1]

            if 0<=rstart<row and 0<=cstart<col:
                res.append([rstart,cstart])

        dir=(dir+1)%4 
    return res      

def optimalSpiralIII(row,col,rstart,cstart):
    direction=[[0,1],[1,0],[0,-1],[-1,0]]
    n=row*col
    res=[[0,0] for _ in range(n)]
    step=1
    index=0
    res[0]=[rstart,cstart]
    count=1
    while count<n:
        for times in range(2):
            dr=direction[index%4][0] 
            dc=direction[index%4][1]
            for i in range(step):
                rstart+=dr
                cstart+=dc
                if 0<=rstart<row and 0<=cstart<col:
                    res[count]=[rstart,cstart]
                    count+=1
            index+=1
        step+=1
    return res                





if __name__=="__main__":
    main()    