# 191
# 문제 설명 : 데이터 리스트의 요소들한테 수수료 0.14% 붙이고 리스트를 2차원 배열로 표현

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]


list2 = [] 
for i in data:
    list1 = []
    #빈 리스트가 두 번째 리스트가 생기기 전에 시작되어야 함.
    for j in i:
        j = j * 1.014
        list1.append(j)
    list2.append(list1)

print(list2)      

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1, len(ohlc)):
    if ohlc[i][3] > 150:
        print(ohlc[i][3])

# 224
def print_keys(dic):
    for key in dict.keys():
        print(key)

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(a, b):
    return (a[b])

print(print_value_by_key(my_dict, '10/26'))

# 226
string = "아이엠어보이유알어걸"
i = 0
while i < len(string) :
    print(string[i:i+3])
    i += 3

# 232

result1 = 'www.'
result2 = '.com'
print(result1 + 'naver' + result2)

# 234
my_list = [3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, my_list))
print(result)






