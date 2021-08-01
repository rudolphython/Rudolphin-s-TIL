## SWEA 최종 문제 풀이

```python
# 딕셔너리 연습문제 4
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
b.update(a)
result = set(filter(lambda item: item[1] >= 3000, b.items()))
print(result)

# 문자열 연습문제 5
my_list = list(map(str, input("단어를 입력하시오:").split()))
new_list = sorted(my_list)
result = ''
for i in new_list:
    result += "%s," % i
print(result[:-1])

# 리스트 연습문제 18
my_list = list(map(int, input('숫자를 입력하세요: ').split(',')))
a , b = my_list[0], my_list[1]
temp = []
for i in range(a):
    result = []
    for j in range(b):
        result.append(i*j)
    temp.append(result)
print(temp)

# 리스트 연습문제 19
a, b, c = 2, 3, 4
result = []
for x in range(a):
    temp = []
    for y in range(b):
        temp.append(c*[0])
    result.append(temp)
print(result)
```