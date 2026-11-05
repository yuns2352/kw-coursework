word=input("문자열을 입력하시오:")
banword=input("금지어를 입력하시오:")

i=word.split(" ")
k=banword.split(" ")

if k in i:
    banword="***"

print(f"{word}")
    
