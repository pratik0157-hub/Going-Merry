def matrix_multipy(arr1, arr2, r1, c1, r2, c2):
    if r2 == c1:
        final = [[0 for f in range(c2)]for u in range(r1)]
        for n in range(0, r1):
            for m in range(0,c2):
                for k in range(0, r2):
                    final[n][m]+=arr1[n][k]*arr2[k][m]
        
        return final
    
    else:
        print("Multiplication of these matric not possible")

rows1 = int(input("enter no of rows of first matrix: "))
cols1 = int(input("Enter no of columns of first matrix: "))

matrix1 = [[0 for j in range(cols1)]for i in range(rows1)]
print("Enter the data in First matrix: ")
for u in range(0,rows1):
    for m in range(0, cols1):
        matrix1[u][m]=int(input("row no: "+str(u+1)+" column no: "+str(m+1)+" data: "))

rows2 = int(input("enter no of rows of second matrix: "))
cols2 = int(input("Enter no of columns of second matrix: "))

matrix2 = [[0 for j in range(cols2)]for i in range(rows2)]
print("Enter the data in Second matrix: ")
for o in range(0,rows2):
    for p in range(0, cols2):
        matrix2[o][p]=int(input("row no: "+str(o+1)+" column no: "+str(p+1)+" data: "))

print("Product of two materials is: ")
print(matrix_multipy(matrix1,matrix2,rows1,cols1,rows2,cols2))
