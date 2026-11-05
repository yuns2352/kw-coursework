for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print(i+j+1,end="")
    print("\n")
