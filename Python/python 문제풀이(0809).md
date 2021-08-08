### 객체지향 연습문제 풀이


```python
# 객체지향 연습문제 1
class Scores:
    def __init__(self, kor, eng):
        self.kor = kor
        self.eng = eng

    def my_sum(self):
        return self.kor + self.eng

p1 = Scores(89, 100)
print(p1.my_sum())

# 객체지향 연습문제 2
class Nation:
    def __init__(self, na):
        self.na = na

    @staticmethod
    def lala():
        return "대한민국"

p1 = Nation("대한민국")
print(p1.lala())
print(p1.na)


# 객체지향 연습문제 4
class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return 0

class Square(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def calc_area(self):
        return self.length**2

p1 = Square(5, 5)
print(p1.calc_area())

# 객체지향 연습문제
class Person:
    def __init__(self, sex):
        self.sex = sex

    def talk_sex(self):
        return "Unknown"

class Male(Person):
    def __init__(self, sex):
        super().__init__(sex)

    def talk_sex(self):
        return self.sex

p1 = Male("Female")
print(p1.talk_sex())
```