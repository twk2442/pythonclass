#조건문 중첩

id = 'sj'
pw = '1234'
input_id = input('id:')
input_pw = input('pw:')


if input_id == id :
    if input_pw == pw:
        print('login success')
    else:
        print('password is not correct')
else:
    print('id is not correct')
    