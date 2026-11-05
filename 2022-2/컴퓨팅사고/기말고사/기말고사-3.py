All = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

List1=[]
List2=[]
List3=[]
result=[]

List1.append('D')
List1.append('C')
List1.append('J')
List1.append('K')

List2.append('B')
List2.append('H')
List2.append('E')

List3.append('L')

result=All-List1-List2-List3

print("Result=",result)

