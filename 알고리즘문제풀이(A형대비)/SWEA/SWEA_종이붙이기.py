T = int(input())

for i in range(1, T+1):
    num = int(input())
    result = num // 10
    dp = [0] * 301
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    for i in range(3, 301):
        dp[i] = dp[i-1] + dp[i-2]*2

    print(dp[result])