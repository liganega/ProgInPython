# -*- coding:utf-8 -*-

'''
사람이 일을 처리하는 과정:
* 파일을 열어야 함
* 1, 2, 3등 점수를 눈으로 확인해야 함
'''

# 파일 열기 도구
# open 함수 활용

file = open("results.txt")

# 기억해야 하는 데이터의 개수에 상관 없이
# 일률적으로 처리하는 방법
# 하나의 해답: 리스트 활용

# 리스트: 여러 개의 값을 동시에 들고 다니는 값

score_list = []

for line in file:
    (name, score) = line.split()
    score_list.append(score)

score_list.pop(0)
score_list.sort()
score_list.reverse()

print(score_list[0])
print(score_list[1])
print(score_list[2])




