# 딕셔너리 정리1

dict = {'메로나' : 1000, '폴라포' : 1200}
# 딕셔너리 생성

dict.update({'죠스바': 1500})
# 딕셔너리 요소 추가

print(dict['메로나'])
# 메로나 value 값 접근 및 출력

dict.pop("메로나")
print(dict)
# 메로나 삭제

# 딕셔너리 정리2

my_dict = {
    '메로나' : [300, 20],
    '비비빅' : [400, 3],
    '죠스바' : [250, 100]
}
print(my_dict)
# value 값이 2개 이상일 경우, 리스트로 정리

print(my_dict['메로나'][0])
# 메로나의 가격(value)에 접근

my_dict.update({'월드콘' : [500, 7]})
print(my_dict)
# 월드콘 추가

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
result = []
for key in icecream.keys():
    result.append(key)

print(result)
# 1. for문으로 key값 리스트로 받기

price = icecream.values()
print(list(price))
# 2. 그냥 받아버리기

print(sum(list(price)))

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# 업데이트하는 법

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)
# zip 함수 쓰기

