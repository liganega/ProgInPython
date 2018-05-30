# 문자열 포매팅(Formatting) 기능 공부
# 6장 주제인 모듈과는 무관함.
# 6장 예제코드에서 포매팅 기능이 사용됨

languages = ['Ruby', 'Python', 'Object C', 'Javascript', 'Java', 'HTML', 'C']

# Ruby : 100%
# Python : 90%
# Object C: 80
# 등등

def degree(lang):
    if lang in languages:
        ind = languages.index(lang)
        return (100 - ind * 10)

for lang in languages:
    print("%-10s는 배우기 쉬운 정도가 %3d%%입니다" % (lang, degree(lang)))








        
