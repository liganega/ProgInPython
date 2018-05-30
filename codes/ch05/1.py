# -*- coding:utf-8 -*-

'''
사람이 일을 처리하는 과정:
* 파일을 열어야 함
* 1, 2, 3등 점수를 눈으로 확인해야 함
'''

# 파일 열기 도구
# open 함수 활용

file = open("results.txt")

score_dict = {}

for line in file:
    (name, score) = line.split()
    try:
        score_dict[float(score)] = name
    except:
        continue

count  = 1
    
for key in sorted(score_dict.keys(), reverse=True):
    print(str(count) + "등은", score_dict[key], "이고 점수는", key, "입니다.")
    count = count + 1
