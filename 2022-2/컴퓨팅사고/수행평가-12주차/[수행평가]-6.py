langStr=("Python","Java","Web","C","R")
langStrl=list(map(lambda x:len(x),langStr))
newList=sorted(zip(langStr,langStrl),key=lambda x:x[1],reverse=True)
for i,j in newList:
        print(f"{i}\t{j}")

        



