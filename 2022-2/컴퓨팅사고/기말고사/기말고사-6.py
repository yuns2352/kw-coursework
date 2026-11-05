f=open("C:\\python_work\\info_sum.txt","w",encoding="utf-8")

info_name = ("홍길동", "김유신", "최영호", "유관순", "강감찬")
info_score = [(100,80,70), (80,80,85), (70,50,70), (85,85,85), (100,100,90)]

Linfo_name=list(info_name)

newinfo_score=sorted(info_score.items(), key=lambda x:x[0], reverse=True)

file=dict(zip(Linfo_name,newinfo_score))

for i,j in file:
    f.write(f"{i},{j}")
f.close()
