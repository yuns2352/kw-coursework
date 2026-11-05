usage=int(input("용도 : 1:주택용, 2:공업용, 3:산업용?"))
list=[1,2,3]
if usage in list:
  use=int(input("사용량(kwh)?"))
  if usage==1:
    subj=910+88*use
  elif usage==2:
    subj=1600+182*use
  elif usage==3:
    subj=7300+275*use
  print(f"용도:{usage},사용량:{use:.2f},전기요금:{subj:,.2f}원")
else:
     print("잘못된 입력입니다.")

