movie_list=[("오징어게임",50.45),("이터널스",35.46),("그레비티",9.8),("노타임투다이",52.5),("스파이더맨",15.47)]
dictmovie_list=dict(movie_list)
ndml=sorted(dictmovie_list.values(),reverse=True)
print("영화제목\t예매율\t순위")
print("========\t=====\t====")

for k in range(5):
    for i,j in dictmovie_list.items():
        if j==ndml[k]:
            print(i,"\t",j,"\t",k+1)


