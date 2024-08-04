def main():
    A=[[1,2,3],[4,5,6],[7,8,9]]
    a=trans(A) 
    print(a)


def trans(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(row):
        left,right=0,row-1
        while left<right:
            matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
            left+=1
            right-=1

    return matrix  

def rotate(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each column
    for i in range(n):
        top, bottom = 0, n - 1
        while top < bottom:
            matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
            top += 1
            bottom -= 1      
if __name__=="__main__":
    main()    