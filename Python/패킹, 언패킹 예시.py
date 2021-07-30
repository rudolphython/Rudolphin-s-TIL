#  패킹
def get_numbers(a, *args):
    return a, args

print(get_numbers(1))
print(get_numbers(1, 2, 3))

# 언패킹
x = [1, 2, 3]
print(get_numbers(x))
print(get_numbers(*x))
print(get_numbers(*[1,2,3]))