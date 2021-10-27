N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
count = 0

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            sum_value = numbers[i] + numbers[j] + numbers[k]
            if sum_value <= M:
                result = max(result, sum_value)



print(result)
