name=input("이름:")
height=int(input("키(cm):"))
weigh=int(input("체중(kg):"))
bmi=weigh/(height*0.01)**2
if bmi>=30:
    subj="비만"
elif bmi>=25:
    subj="과체중"
elif bmi>=20:
    subj="정상"
else:
    subj="저체중"
print(f"{name}님의 BMI 결과는 키:{height:.1f}cm, 체중:{weigh:.1f}kg, BMI지수:{bmi:.2f}이며, 판정은 {subj}이다.")
