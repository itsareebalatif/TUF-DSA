def main():

    A =[[1, 1, 1,1],         
        [0, 1, 1,1],     
        [0, 1, 0,1]]  
 
    #bruteforce(A,3,3)
    a=Optimal(A,3,3)
    print(a) 
#BRUTE FORCE APPROCH    
def bruteforce(matrix,row,col):
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                markrow(matrix,row,col,i)
                markcol(matrix,row,col,j) 

    for i in range(row):
        for j in range(col):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix            

def markrow(matrix,row,col,i):
    for j in range(col):
        if matrix[i][j]!=0:
            matrix[i][j]=-1

def markcol(matrix,row,col,j):
    for i in range(row):
        if matrix[i][j]!=0:
            matrix[i][j]=-1

#BETTER SOLUTION
def better(matrix,n,m):
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1

    for i in range(n):
        for j in range(m):
            if row[i] or col[j] ==1:
                matrix[i][j]=0

    return matrix   


#OPTIMAL SOLUTION
def Optimal(matrix,n,m):
    firstrow=False
    firstcol=False
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                if i==0:
                    firstrow=True
                if j==0:
                    firstcol =True
                matrix[0][j]=0
                matrix[i][0]=0

    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if firstrow:
        for j in range(m):
            matrix[0][j]=0

    if firstcol:
        for i in range(n):
            matrix[i][0]=0

    return matrix        





if __name__=="__main__":
    main()
                    
   





