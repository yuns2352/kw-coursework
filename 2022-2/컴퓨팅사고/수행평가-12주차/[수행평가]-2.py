def func_stat(num):
    result=1
    i=1
    while i <= num:
        result*=i
        i=i+1

    return result

num=int(input("숫자 입력:"))
print(f"{num}!={func_stat(num)}")


    
