def main():

    A =[[1, 1, 1],         
        [0, 1, 1],     
        [1, 1, 1]]   
 
    bruteforce(A,3,3)
    
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



if __name__=="__main__":
    main()
                    
   





