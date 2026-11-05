money=int(input("부모님으로부터 받은 용돈:"))
cookie=3550
rest=money-cookie
five_hundred=rest//500
one_hundred=(rest-five_hundred*500)//100
fifty=(rest-five_hundred*500-one_hundred*100)//50
print(f"거스름돈 : {rest}원")
print(f"500원짜리 거스름돈 : {five_hundred}개")
print(f"100원짜리 거스름돈 : {one_hundred}개")
print(f"50원짜리 거스름돈 : {fifty}개")
