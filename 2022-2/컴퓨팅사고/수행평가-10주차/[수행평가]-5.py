num = int(input("숫자 입력:"))

if(num<2):
    print("소수가 아닙니다.")
else:
    flag=True
    for i in range(2,num-1):
        if(num%i==0):
            print(f"{num}은(는) 소수가 아닙니다.")
            flag=False
            break
    if(flag==True):
        print(f"{num}은(는) 소수입니다.")
