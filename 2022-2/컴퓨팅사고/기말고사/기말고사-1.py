mymoney=100000

clothes=int(input("옷 값:"))

rest=mymoney-clothes

manone=rest//10000
ohchon=(rest-10000*manone)//5000
chon=(rest-10000*manone-ohchon*5000)//1000
ohbaek=(rest-10000*manone-ohchon*5000-chon*1000)//500
baek=(rest-10000*manone-ohchon*5000-chon*1000-ohbaek*500)//100
chip=(rest-10000*manone-ohchon*5000-chon*1000-ohbaek*500-baek*100)//10

if clothes>=50000:
    clothes=clothes*0.9
elif chip>=0:
    baek+=1

print(f"10000\t:{manone}")
print(f"5000 \t:{ohchon}")
print(f"1000 \t:{chon}")
print(f"500  \t:{ohbaek}")
print(f"100  \t:{baek}")
