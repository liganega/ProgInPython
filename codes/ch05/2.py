#-*- coding: utf-8 -*- 

# 입력값
s = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
s_splitted = s.split(';')

s_dict = {}
s_dict = {'Number':'101'}
s_dict['Name'] = "Johnny 'wave-boy' Jones"
s_dict['Nation'] = 'USA'
s_dict['Record'] = '8.32'
s_dict['BoardType'] = 'Fish'
s_dict['Age'] = '21'


# 리턴값
# {'번호': '101', '이름': "Johnny 'wave-boy' Jones", '국적': 'USA', '기록': '8.32', '보드타입': 'Fish', '나이': '21'}

# print 함수의 숨은 인자 중에서 sep 키워드 인자를 활용하면
# 인자들 사이에 오는 문자열을 조정할 수 있다.

# 포매팅 기술을 활용

for key in s_dict:
    print("%-10s %s"  %  (key+':', s_dict[key]))









    
