print("369 369 369 369 start~")

for i in range(1,101):
    if i%10==3 or i%10==6 or i%10==9:
        print("박수",end=" ")
    elif i//10==3 or i//10==6 or i//10==9:
        print("박수",end=" ")
    else:
        print(i,end=" ")

print("\n성공입니다!")
     
