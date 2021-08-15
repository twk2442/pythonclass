#dictionary 
#반복문 중쳡 
persons = {'name':'egoing','address':'seoul','age':'23'} #dictionary형 

print(persons['name'])  
print('---------------')

html = [{'name':'tw','address':'illsan','age':'26'},{'name':'ja','address':'seoul','age':'29'},{'name':'sj','address':'seoul','age':'25'}]

for key in html:  #이중반복문을 통해 리스트안에 모든 데이터 출력
    for data in key:
        print(data ,':', key[data])     
    print('--------------------')
