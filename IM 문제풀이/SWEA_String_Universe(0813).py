T = int(input())

for test_case in range(1, T + 1):
    N = input()
    my_list = input().split()
    my_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    for c in my_list:
        my_dict[c] += 1

    result = ""
    for key, value in my_dict.items():
        test = ' '.join([key] * value)
        result += test + ' '

    print("#{test_case} {result[:len(result) - 1]}")