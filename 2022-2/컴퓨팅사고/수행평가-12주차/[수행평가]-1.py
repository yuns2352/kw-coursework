import statistics

def func_stat(num):
    for i in num:
        print(i,end=" ")
    print()
    hap=sum(num)
    return hap

num=[15,25,33,17,88,25]
result=func_stat(num)
print(f"합계:{result}")


    

    
