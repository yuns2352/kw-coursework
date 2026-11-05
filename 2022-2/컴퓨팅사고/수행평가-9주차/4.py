second=int(input("초를 입력하세요:"))
hour=second//3600
minute=second//60-hour*60
seconds=second-hour*3600-minute*60
print(f"입력받은 {second}초는 {hour}시간 {minute}분 {seconds}초이다.")
