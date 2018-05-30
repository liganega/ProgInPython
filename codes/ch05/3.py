#-*- coding: utf-8 -*- 

# 입력값
s = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
s_splitted = s.split(';')

items = ['Number', 'Name', 'Nation', 'Record', 'BoardType', 'Age']

s_dict = {}

for item in items:
    item_index = items.index(item)
    s_dict[item] = s_splitted[item_index]



# 리턴값
# {'번호': '101', '이름': "Johnny 'wave-boy' Jones", '국적': 'USA', '기록': '8.32', '보드타입': 'Fish', '나이': '21'}

# print 함수의 숨은 인자 중에서 sep 키워드 인자를 활용하면
# 인자들 사이에 오는 문자열을 조정할 수 있다.

# 포매팅 기술을 활용

for key in s_dict:
    print("%-10s %s"  %  (key+':', s_dict[key]))









    
