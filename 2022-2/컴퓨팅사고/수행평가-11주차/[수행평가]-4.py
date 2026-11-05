inputData=[('Java',15000),('Python',25000),('C',18000),('Java',19000)]
B=[]
C=[]
for i,j in inputData:
    if i not in C:
        B.append((i,j))
        C.append(i)
for i,j in B:
    print(i,"\t",j)



