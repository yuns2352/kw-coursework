def fibo(num):
    a=1
    b=1
    result=[1]
    if num==1 or num==2:
        return 1
    for i in range(1,num):
        a,b=b,b+a
        result.append(a)
 
    return result
    
num=int(input("숫자:"))
for i in fibo(num):
    print(i)



    
        
