dp = [0]*301    # dp의 길이 31로 해도 가능할 듯
dp[1] = 1   # 가로의 길이가 1일 때, 경우의 수는 10
dp[2] = 3   # 가로의 길이가 2일 때, 경우의 수는 3(10*3, 20(가로)+10, 20(정사각형)+10
dp[3] = 6

for i in range(4, 301):
    dp[i] = dp[i-1] + dp[i-2]*2     # 규칙을 알아낼려면 최소 dp[3]까진 해야되는 거 아닌가..?

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    print(dp[N//10])