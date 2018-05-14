# -*- coding:utf-8 -*-

'''
사람이 일을 처리하는 과정:
* 파일을 열어야 함
* 1, 2, 3등 점수를 눈으로 확인해야 함
'''

# 파일 열기 도구
# open 함수 활용

file = open("results.txt")

highst_score = 0

# 예외처리(try ... except ...)

for line in file:
    record = line.split()
    try:
        if highst_score < float(record[1]):
            highst_score = float(record[1])
        else:
            pass
    except:
        pass
    
print(highst_score)
