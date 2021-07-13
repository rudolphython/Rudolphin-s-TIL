## 7월 14일 문제풀이

# python

```
# 셋과 딕셔너리 연습문제 1
dic = {"홍길동": "010-1111-1111", "이순신": "010-1111-2222", "강감찬": "010-1111-3333"}
print("아래 학생들의 전화번호를 조회할 수 있습니다.")
for key in dic.keys():
    print(key)
a = input("전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.: ")
if a in dic:
    print("{0}의 전화번호는 {1}입니다.".format(a, dic[a]))

# 셋과 딕셔너리 연습문제 2
import operator

dic = {"TV": "2000000","냉장고": "1500000", "책상": "350000", "노트북": "1200000", "가스레인지": "200000", "세탁기": "1000000"}
# operator.itemgetter(0)으로하면 키를 기준으로 1로하면 값을 기준으로 정렬
# 기본은 오름차순 정렬이므로 내림차순을 하려면 reverse를 True해야한다.
# 이 기능을 사용하기 위해서는 operator 모듈을 import해야한다.
dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
for key, value in dic.items():
   print("{0}: {1}".format(key, value))

# 백준 10950번

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    x, y = map(int, input().split())
    print(x+y)
```

    


