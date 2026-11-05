def check_mail():

    
    for i in mail:
        if '@' in (check_mail(i)):
            result.append(i)

    print(result)

mail = ['jack@naver.com', '12345', 'abc@', 'abc@gmail.com', '@hanmail.net']
result = []

check_mail()
