## 데이터 구조 개념정리 및 연습문제 풀이

```python
# 1. 피타고라스의 정리
my_list = []
for i in range(1, 51):
    for j in range(1, 51):
        for t in range(1, 51):
            if i ** 2 + j ** 2 == t ** 2 and i < j < t:
                my_list.append((i, j, t))
                
print(my_list)

# 2. 피타고라스의 정리를 리스트 내포로 재정리
new_list = [(i, j, t) for i in range(1, 51) for j in range(1, 51) for t in range(1, 51) if i ** 2 + j ** 2 == t ** 2 and i < j < t]
print(new_list)

# 3. 모음 제거하기
vowels = 'aeiou'
words = 'Life is too short, you need python!'

my_list = []
for x in words:
    if x not in vowels:
        my_list.append(x)

print(" ".join(my_list))

# 4. 코딩테스트의 기본!
my_list = list(map(int, input().split( )))
print(my_list)

# 5. 모든 위치
def my_find(text, alphabet):
    my_list = []
    for idx, key in enumerate(text):
        if key == alphabet:
            my_list.append(idx)
    if my_list == []:
        return -1
    else : 
        return my_list
        
print(my_find('apple', 'p'))
print(my_find('a', 'p'))

# 6. 출석 체크
def check(n, students):
    my_list = list(map(int, students.split()))
    student_list = list(range(1, n + 1, 1))
    final_list = []
    for i in student_list:
        if i not in my_list:
            final_list.append(i)
    result = ""
    for i in final_list:
        result += "%d " % i
    return result.rstrip()

print(check(7, '1 3 5'))

# 7. 딕셔너리 내포 사용하기
dusts = {'서울': 72, '인천': 82, '제주': 29, '동해': 45}

print(dict({key : value for key, value in dusts.items() if value > 80}))
print(dict({key: '나쁨' if value > 80 else '보통' for key, value in dusts.items()}))

result = {key : '매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통' if value > 30 else '좋음' for key, value in dusts.items()}
print(result)
```
