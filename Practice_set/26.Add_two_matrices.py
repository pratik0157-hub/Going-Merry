def matrix_add(arr1, arr2, r, c):
    final = [[0 for f in range(c)]for u in range(r)]
    for n in range(0,r):
        for m in range(0, c):
            final[n][m]=arr1[n][m]+arr2[n][m]
    return final

rows = int(input("enter no of rows of matrix: "))
cols = int(input("Enter no of columns of matrix: "))

matrix1 = [[0 for j in range(cols)]for i in range(rows)]
print("Enter the data in First matrix: ")
for n in range(0,rows):
    for m in range(0, cols):
        matrix1[n][m]=int(input("row no: "+str(n+1)+" column no: "+str(m+1)+" data: "))

matrix2 = [[0 for j in range(cols)]for i in range(rows)]
print("Enter the data in Second matrix: ")
for o in range(0,rows):
    for p in range(0, cols):
        matrix2[o][p]=int(input("row no: "+str(n+1)+" column no: "+str(m+1)+" data: "))

print("Sum of the two Matrix: ")
print(matrix_add(matrix1,matrix2,rows,cols))