T = int(input())

for test_case in range(1, T + 1):
    word = input()

    result = ""
    for i in word:
        if not i in 'aeiou':
            result += i

    print(f"#{test_case} {result}")