def main():
    A=[[1,2,3],[4,5,6],[7,8,9]]
    a=trans(A) 
    print(a)


def transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    transposed=[[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            transposed[i][j]=matrix[j][i]
    return transposed


def trans(matrix):
    row=len(matrix)
    col=len(matrix[0])
    for i in range(row):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix        



if __name__=="__main__":
    main()


       